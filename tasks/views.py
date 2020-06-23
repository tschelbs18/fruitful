from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.html import format_html

from .models import *

# Create your views here.
def index(request):
    context = {
    }
    # Change the line below to True for testing in prod
    if request.get_host() == "127.0.0.1:8000" or False:
        return render(request, "tasks/index.html", context)
    else:
        return render(request, "tasks/beta.html", context)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Logged in Successfully.")
            # Change this route to the tasks page?
            return HttpResponseRedirect(reverse("home"))
        else:
            messages.add_message(request, messages.ERROR, "Invalid Credentials.")
            return render(request, "tasks/login.html")
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "tasks/login.html")

def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Logged Out.")
    return HttpResponseRedirect(reverse("login"))

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        user_profile = UserProfile(user=user)
        user_profile.save()
        messages.add_message(request, messages.SUCCESS, f"Thank you for making an account, {first_name}. Login here.")
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "tasks/register.html")

def error_view(request):
    if not(request.user.is_authenticated):
        messages.add_message(request, messages.INFO, "You need to login first.")
        return render(request, "tasks/login.html")
    if request.method == "POST":
        subject = request.POST.get("subject")
        details = request.POST.get("description")
        reporter = request.user
        error = Error(reporter=reporter, subject=subject, details=details)
        error.save()
        messages.add_message(request, messages.INFO, "Thank you for your error report, we'll look into it.")
        return HttpResponseRedirect(reverse("tasks"))
    else:
        return render(request, "tasks/error.html")

def admin_errors_view(request):
    if not request.user.is_superuser:
        messages.add_message(request, messages.INFO, "You don't have access to this page.")
        return render(request, "tasks/index.html")
    else:
        context = {
            "active_errors": Error.objects.filter(handled=False),
            "fixed_errors": Error.objects.filter(handled=True)
        }
        return render(request, "tasks/admin_errors.html", context)

def handle_error(request, error_id):
    error = Error.objects.get(id=error_id)
    error.handled = True
    error.save()
    messages.add_message(request, messages.SUCCESS, f"Error handled.")
    return HttpResponseRedirect(reverse("admin_errors_view"))

def tasks_view(request):
    if request.user.is_authenticated:
        context = {
            "active_tasks": UserTask.objects.filter(status__in=('Incomplete','In Progress'),user=request.user)
        }
        return render(request, "tasks/tasks.html", context)
    else:
        messages.add_message(request, messages.INFO, "You need to login first.")
        return render(request, "tasks/login.html")

def add_task(request):
    if request.method == "POST":
        if len(UserTask.objects.filter(user=request.user, status="Incomplete")) >= 20:
            messages.add_message(request, messages.ERROR, "Sorry, you can't have more than 20 active tasks at any time. Delete or complete one to add a new one.")
            return HttpResponseRedirect(reverse("rewards"))
        task = request.POST.get("description")
        size = request.POST.get("size")
        new_task = UserTask(user=request.user, size=size, status="Incomplete", description=task)
        new_task.save()
        messages.add_message(request, messages.SUCCESS, f"Task added successfully")
        return HttpResponseRedirect(reverse("tasks"))
    else:
        return HttpResponseRedirect(reverse("tasks"))

def update_task(request, task_id):
    # TODO:
    pass

def delete_task(request, task_id):
    task = UserTask.objects.get(id=task_id)
    task.delete()
    messages.add_message(request, messages.INFO, "Task deleted, not completed.")
    return HttpResponseRedirect(reverse("tasks"))

def complete_task(request, task_id):
    task = UserTask.objects.get(id=task_id)
    task.status = 'Complete'
    task.save()
    points = task.get_points()
    profile = UserProfile.objects.get(user=request.user)
    profile.current_points += points
    profile.total_points += points
    profile.save()
    msg = format_html(f'Nice work! You just earned {task.get_points()} points. Go grab a <a href="{reverse("rewards")}">reward</a>')
    messages.add_message(request, messages.SUCCESS, msg)
    return HttpResponseRedirect(reverse("tasks"))

def past_tasks_view(request):
    if request.user.is_authenticated:
        context = {
            "completed_tasks": UserTask.objects.filter(status='Complete', user=request.user).order_by('-last_updated_dt')[:20]
        }
        return render(request, "tasks/past_tasks.html", context)
    else:
        messages.add_message(request, messages.INFO, "You need to login first.")
        return render(request, "tasks/login.html")

def rewards_view(request):
    if request.user.is_authenticated:
        context = {
            "standard_rewards": StandardReward.objects.all(),
            "custom_rewards": UserReward.objects.filter(user=request.user, status='Available'),
            "points": UserProfile.objects.get(user=request.user).current_points
        }
        return render(request, "tasks/rewards.html", context)
    else:
        messages.add_message(request, messages.INFO, "You need to login first.")
        return render(request, "tasks/login.html")

def add_reward(request):
    if request.method == "POST":
        if len(UserReward.objects.filter(user=request.user, status="Available")) >= 20:
            messages.add_message(request, messages.ERROR, "Sorry, you can't have more than 20 custom rewards at any time. Delete one to make a new one.")
            return HttpResponseRedirect(reverse("rewards"))
        description = request.POST.get("description")
        size = request.POST.get("size")
        new_reward = UserReward(user=request.user, size=size, status="Available", description=description)
        new_reward.save()
        messages.add_message(request, messages.SUCCESS, f"Reward added successfully")
        return HttpResponseRedirect(reverse("rewards"))
    else:
        return HttpResponseRedirect(reverse("rewards"))

def delete_reward(request, reward_id):
    reward = UserReward.objects.get(id=reward_id)
    reward.delete()
    messages.add_message(request, messages.INFO, f"{reward.description} deleted from available custom rewards.")
    return HttpResponseRedirect(reverse("rewards"))

def redeem_reward(request, reward_id):
    reward = UserReward.objects.get(id=reward_id)
    profile = UserProfile.objects.get(user=request.user)
    points = reward.get_points()
    if points > profile.current_points:
        messages.add_message(request, messages.ERROR, "You don't have enough points for that reward right now, go do some more tasks!")
        return HttpResponseRedirect(reverse("rewards"))
    past_reward = UserReward(user=request.user, size=reward.size, status="Used", description=reward.description)
    past_reward.save()
    profile = UserProfile.objects.get(user=request.user)
    profile.current_points -= points
    profile.save()
    messages.add_message(request, messages.SUCCESS, f"Awesome! {reward.description}")
    return HttpResponseRedirect(reverse("rewards"))

def redeem_standard_reward(request, reward_id):
    reward = StandardReward.objects.get(id=reward_id)
    profile = UserProfile.objects.get(user=request.user)
    points = reward.get_points()
    if points > profile.current_points:
        messages.add_message(request, messages.ERROR, "You don't have enough points for that reward right now, go do some more tasks!")
        return HttpResponseRedirect(reverse("rewards"))
    past_reward = UserReward(user=request.user, size=reward.size, status="Used", description=reward.description)
    past_reward.save()
    profile = UserProfile.objects.get(user=request.user)
    profile.current_points -= points
    profile.save()
    messages.add_message(request, messages.SUCCESS, f"Awesome! {reward.description}")
    return HttpResponseRedirect(reverse("rewards"))

def past_rewards_view(request):
    if request.user.is_authenticated:
        context = {
            "redeemed_rewards": UserReward.objects.filter(status='Used', user=request.user).order_by('-last_updated_dt')[:20],
        }
        return render(request, "tasks/past_rewards.html", context)
    else:
        messages.add_message(request, messages.INFO, "You need to login first.")
        return render(request, "tasks/login.html")

def scoreboard_total_view(request):
    context = {
        "leaders": UserProfile.objects.order_by('-total_points')[:25]
    }
    return render(request, "tasks/total_scoreboard.html", context)

def scoreboard_daily_view(request):
    # Go user by user and calculate points for tasks completed today. grab top 25 from that
    return render(request, "tasks/daily_scoreboard.html")

def about_view(request):
    return render(request, "tasks/about.html")

def faq_view(request):
    return render(request, "tasks/faq.html")

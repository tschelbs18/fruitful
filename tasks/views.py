from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages

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
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "tasks/register.html")

def error_view(request):
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
        task = request.POST.get("description")
        # Need to add size to form
        new_task = UserTask(user=request.user, size="Small", status="Incomplete", description=task)
        new_task.save()
        return HttpResponseRedirect(reverse("tasks"))
    else:
        return HttpResponseRedirect(reverse("tasks"))

def update_task(request, task_id):
    pass

def delete_task(request, task_id):
    task = UserTask.objects.get(id=task_id)
    task.delete()
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
    messages.add_message(request, messages.SUCCESS, f"Nice work! You just earned {task.get_points()} points.")
    return HttpResponseRedirect(reverse("tasks"))

def past_tasks_view(request):
    if request.user.is_authenticated:
        context = {
            "completed_tasks": UserTask.objects.filter(status='Complete', user=request.user)
        }
        return render(request, "tasks/past_tasks.html", context)
    else:
        messages.add_message(request, messages.INFO, "You need to login first.")
        return render(request, "tasks/login.html")

def rewards_view(request):
    if request.user.is_authenticated:
        context = {
            "standard_rewards": StandardReward.objects.all(),
            "custom_rewards": UserReward.objects.filter(status='Available'),
        }
        return render(request, "tasks/rewards.html", context)
    else:
        messages.add_message(request, messages.INFO, "You need to login first.")
        return render(request, "tasks/login.html")

def add_reward(request):
    if request.method == "POST":
        description = request.POST.get("description")
        size = request.POST.get("size")
        new_reward = UserReward(user=request.user, size=size, status="Available", description=description)
        new_reward.save()
        return HttpResponseRedirect(reverse("rewards"))
    else:
        return HttpResponseRedirect(reverse("rewards"))

def redeem_reward(request, reward_id):
    reward = UserReward.objects.get(id=reward_id)
    reward.status = 'Used'
    reward.save()
    points = reward.get_points()
    profile = UserProfile.objects.get(user=request.user)
    profile.current_points -= points
    profile.total_points -= points
    profile.save()
    messages.add_message(request, messages.SUCCESS, f"Awesome! Enjoy your reward.")
    return HttpResponseRedirect(reverse("rewards"))

def past_rewards_view(request):
    if request.user.is_authenticated:
        context = {
            "redeemed_rewards": UserReward.objects.filter(status='Used'),
        }
        return render(request, "tasks/past_rewards.html", context)
    else:
        messages.add_message(request, messages.INFO, "You need to login first.")
        return render(request, "tasks/login.html")

def scoreboard_total_view(request):
    pass

def scoreboard_daily_view(request):
    pass

def about_view(request):
    return render(request, "tasks/about.html")

def faq_view(request):
    return render(request, "tasks/faq.html")

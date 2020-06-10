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
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "tasks/error.html")

def tasks_view(request):
    # TODO:
    pass

def admin_tasks_view(request):
    # TODO:
    pass

def scoreboard_view(request):
    # TODO:
    pass

def about_view(request):
    # TODO:
    pass

def faq_view(request):
    # TODO:
    pass

def contact_view(request):
    # TODO:
    pass

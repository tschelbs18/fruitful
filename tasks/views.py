from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
    }
    if request.get_host() == "127.0.0.1:8000":
        print("Local testing")
        return render(request, "tasks/index.html", context)
    else:
        return render(request, "tasks/beta.html", context)

def login_view(request):
    # TODO:
    pass

def logout_view(request):
    # TODO:
    pass

def tasks_view(request):
    # TODO:
    pass

def register_view(request):
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

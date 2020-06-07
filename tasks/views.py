from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
    
    }
    return render(request, "tasks/index.html", context)

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

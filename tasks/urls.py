from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="home"),
  path("register", views.register_view, name="register"),
  path("login", views.login_view, name="login"),
  path("logout", views.logout_view, name="logout"),
  path("admin_tasks", views.admin_tasks_view, name="admin_tasks_view")
]

from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="home"),
  path("register", views.register_view, name="register"),
  path("login", views.login_view, name="login"),
  path("logout", views.logout_view, name="logout"),
  path("error_report", views.error_view, name="error"),
  path("faq", views.faq_view, name="faq"),
  path("about", views.about_view, name="about"),
  path("admin_tasks", views.admin_tasks_view, name="admin_tasks_view"),
  path("admin_errors", views.admin_errors_view, name="admin_errors_view")
]

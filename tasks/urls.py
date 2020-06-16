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
  path("tasks", views.tasks_view, name="tasks"),
  path("tasks/add", views.add_task, name="add_task"),
  path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),
  path("admin_errors", views.admin_errors_view, name="admin_errors_view")
]

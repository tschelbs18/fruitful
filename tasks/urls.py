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
  path("complete_task/<int:task_id>/", views.complete_task, name="complete_task"),
  path("past_tasks", views.past_tasks_view, name="past_tasks"),
  path("rewards", views.rewards_view, name="rewards"),
  path("rewards/add", views.add_reward, name="add_reward"),
  path("redeem_reward/<int:reward_id>/", views.redeem_reward, name="redeem_reward"),
  path("daily_scoreboard", views.scoreboard_daily_view, name="daily_scoreboard"),
  path("total_scoreboard", views.scoreboard_total_view, name="total_scoreboard"),
  path("handle_error/<int:error_id>/", views.handle_error, name="handle_error"),
  path("admin_errors", views.admin_errors_view, name="admin_errors_view")
]

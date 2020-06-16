from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Error(models.Model):
    reporter = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
    )
    handled = models.BooleanField(default=False)
    subject = models.CharField(max_length=256, default="")
    details = models.CharField(max_length=2000)

    def __str__(self):
        return f"Error #{self.id}: {self.subject}"

    def show_details(self):
        return f"Error #{self.id}: {self.subject} - {self.details}"

class UserTask(models.Model):
    size = models.CharField(max_length=64)
    description = models.CharField(max_length=2000)
    status = models.CharField(max_length=64,
        choices=[
            ('Incomplete', 'Incomplete'),
            ('In Progress', 'In Progress'),
            ('Complete', 'Complete')
        ])
    created_dt = models.DateTimeField(auto_now_add=True)
    last_updated_dt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE)

class StandardReward(models.Model):
    size = models.CharField(max_length=64)
    name = models.CharField(max_length=1000)

class UserReward(models.Model):
    size = models.CharField(max_length=64)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=64,
        choices=[
            ('Earned', 'Earned'),
            ('Used', 'Used')
        ])
    created_dt = models.DateTimeField(auto_now_add=True)
    last_updated_dt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE)

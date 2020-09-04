from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime, timezone

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    current_points = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    # Add a profile image?

    def __str__(self):
        return f"{self.user.username}"

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
            ('Complete', 'Complete')
        ])
    created_dt = models.DateTimeField(auto_now_add=True)
    last_updated_dt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.size}: {self.description}"

    def get_past_days_added(self):
        # Should probably return a dictionary with units and value
        if (datetime.now(timezone.utc) - self.created_dt).days >= 1:
            return {'units': 'days', 'value': (datetime.now(timezone.utc) - self.created_dt).days}
        elif (datetime.now(timezone.utc) - self.created_dt).hours >= 1:
            return {'units': 'hours', 'value': (datetime.now(timezone.utc) - self.created_dt).hours}
        elif (datetime.now(timezone.utc) - self.created_dt).minutes >= 1:
            return {'units': 'minutes', 'value': (datetime.now(timezone.utc) - self.created_dt).minutes}
        else:
            return {'units': 'seconds', 'value': (datetime.now(timezone.utc) - self.created_dt).seconds}

    def get_past_days_completed(self):
        return (datetime.now(timezone.utc) - self.last_updated_dt).days

    def get_points(self):
        points_map = {
            'Small': 100,
            'Medium': 300,
            'Large' : 500
        }
        return points_map.get(self.size)

class StandardReward(models.Model):
    size = models.CharField(max_length=64)
    description = models.CharField(max_length=1000)

    def get_points(self):
        points_map = {
            'Small': 100,
            'Medium': 300,
            'Large' : 500
        }
        return points_map.get(self.size)

    def __str__(self):
     return f"{self.size}: {self.description}"

class UserReward(models.Model):
    size = models.CharField(max_length=64)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=64,
        choices=[
            ('Available', 'Available'),
            ('Used', 'Used')
        ])
    created_dt = models.DateTimeField(auto_now_add=True)
    last_updated_dt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE)

    def __str__(self):
         return f"{self.size}: {self.description}"

    def get_past_days_added(self):
     return (datetime.now(timezone.utc) - self.created_dt).days

    def get_past_days_completed(self):
     return (datetime.now(timezone.utc) - self.last_updated_dt).days

    def get_points(self):
        points_map = {
            'Small': 100,
            'Medium': 300,
            'Large' : 500
        }
        return points_map.get(self.size)

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Fruit(models.Model):
    size = models.CharField(max_length=64)
    name = models.CharField(max_length=64)

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

class StandardTask(models.Model):
    size = models.CharField(max_length=64)
    name = models.CharField(max_length=2000)

class CustomTask(models.Model):
    size = models.CharField(max_length=64)
    name = models.CharField(max_length=2000)

class UserTask(models.Model):
    size = models.CharField(max_length=64)
    name = models.CharField(max_length=2000)
    status = models.CharField(max_length=64)

class StandardReward(models.Model):
    size = models.CharField(max_length=64)
    name = models.CharField(max_length=1000)

class CustomReward(models.Model):
    size = models.CharField(max_length=64)
    name = models.CharField(max_length=1000)

class UserReward(models.Model):
    size = models.CharField(max_length=64)
    name = models.CharField(max_length=1000)

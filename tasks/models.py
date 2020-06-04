from django.db import models

# Create your models here.
class Fruit(models.Model):
    size = models.CharField(max_length=64)
    name = models.CharField(max_length=64)

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

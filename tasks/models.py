from django.db import models

# Create your models here.
class Fruit(models.Model):
    size = models.CharField(max_length=64)
    name = models.CharField(max_length=64)

class StandardTask(models.Model):
    pass

class CustomTask(models.Model):
    pass

class UserTask(models.Model):
    pass

class StandardReward(models.Model):
    pass

class CustomReward(models.Model):
    pass

class UserReward(models.Model):
    pass

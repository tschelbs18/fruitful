from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(UserTask)
admin.site.register(StandardReward)
admin.site.register(UserReward)
admin.site.register(Error)
admin.site.register(UserProfile)

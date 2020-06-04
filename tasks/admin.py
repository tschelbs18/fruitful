from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(StandardTask)
admin.site.register(CustomTask)
admin.site.register(UserTask)
admin.site.register(StandardReward)
admin.site.register(CustomReward)
admin.site.register(UserReward)
admin.site.register(Fruit)

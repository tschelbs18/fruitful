# Generated by Django 3.0.7 on 2020-06-16 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0008_auto_20200616_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreward',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userreward',
            name='last_updated_dt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='userreward',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertask',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertask',
            name='last_updated_dt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='usertask',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

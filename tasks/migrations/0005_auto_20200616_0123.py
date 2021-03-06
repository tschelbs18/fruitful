# Generated by Django 3.0.7 on 2020-06-16 05:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20200616_0116'),
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
    ]

# Generated by Django 4.1.5 on 2023-04-01 22:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cal', '0053_alter_event_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='post_like',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

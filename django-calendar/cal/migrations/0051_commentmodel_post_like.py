# Generated by Django 4.1.5 on 2023-03-30 21:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cal', '0050_delete_likemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='post_like',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

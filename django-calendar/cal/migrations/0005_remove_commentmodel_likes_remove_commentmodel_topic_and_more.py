# Generated by Django 4.1.5 on 2023-03-01 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0004_commentmodel_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='commentmodel',
            name='topic',
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]

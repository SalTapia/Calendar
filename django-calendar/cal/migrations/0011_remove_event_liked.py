# Generated by Django 4.1.5 on 2023-03-09 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0010_remove_commentmodel_liked_event_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='liked',
        ),
    ]

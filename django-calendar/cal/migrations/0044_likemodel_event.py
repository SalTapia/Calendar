# Generated by Django 4.1.5 on 2023-03-30 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0043_likemodel_id_alter_likemodel_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='likemodel',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cal.event'),
        ),
    ]

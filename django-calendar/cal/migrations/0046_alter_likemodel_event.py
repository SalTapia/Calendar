# Generated by Django 4.1.5 on 2023-03-30 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0045_alter_likemodel_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likemodel',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cal.event'),
        ),
    ]

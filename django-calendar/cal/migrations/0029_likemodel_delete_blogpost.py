# Generated by Django 4.1.5 on 2023-03-26 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0028_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='likeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]

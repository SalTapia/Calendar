# Generated by Django 4.1.5 on 2023-03-24 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0016_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]

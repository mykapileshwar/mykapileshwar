# Generated by Django 4.0.1 on 2022-01-28 08:24

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='attachment',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-16 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_socialprofile_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='socialprofile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

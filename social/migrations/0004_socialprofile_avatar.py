# Generated by Django 4.1.5 on 2023-01-25 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_post_updated_at_socialprofile_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='social/images'),
        ),
    ]

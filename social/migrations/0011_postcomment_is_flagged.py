# Generated by Django 4.1.6 on 2023-02-06 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_postcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='is_flagged',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

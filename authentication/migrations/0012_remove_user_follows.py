# Generated by Django 4.2.7 on 2023-12-29 08:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0011_user_profile_photo_user_role"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="follows",
        ),
    ]

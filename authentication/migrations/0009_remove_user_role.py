# Generated by Django 4.2.7 on 2023-12-27 02:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0008_alter_user_follows"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="role",
        ),
    ]

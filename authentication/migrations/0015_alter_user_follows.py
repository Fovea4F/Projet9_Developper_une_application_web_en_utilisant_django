# Generated by Django 4.2.7 on 2024-01-03 10:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0014_user_follows_delete_userfollows"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="follows",
            field=models.ManyToManyField(
                to=settings.AUTH_USER_MODEL, verbose_name="suit"
            ),
        ),
    ]
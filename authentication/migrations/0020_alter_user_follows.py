# Generated by Django 4.2.7 on 2024-01-09 10:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0019_alter_user_follows"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="follows",
            field=models.ManyToManyField(
                related_name="followed",
                to=settings.AUTH_USER_MODEL,
                verbose_name="abonné",
            ),
        ),
    ]

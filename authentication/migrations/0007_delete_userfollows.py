# Generated by Django 4.2.7 on 2023-12-18 20:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0006_auto_20231218_2133"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserFollows",
        ),
    ]
# Generated by Django 4.2.7 on 2023-12-30 18:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("review", "0010_alter_review_body_alter_review_headline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="body",
            field=models.CharField(max_length=8192, verbose_name="Commentaire"),
        ),
        migrations.AlterField(
            model_name="review",
            name="headline",
            field=models.CharField(max_length=128, verbose_name="Titre"),
        ),
    ]

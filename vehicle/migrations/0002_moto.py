# Generated by Django 5.1.3 on 2024-11-19 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vehicle", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Moto",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=150, verbose_name="название")),
                ("description", models.TextField(verbose_name="описание")),
            ],
            options={
                "verbose_name": "мотоцикл",
                "verbose_name_plural": "мотоциклы",
            },
        ),
    ]
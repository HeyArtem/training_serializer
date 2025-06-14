# Generated by Django 4.2.1 on 2025-06-15 11:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hero",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=60, unique=True, verbose_name="Имя"),
                ),
                (
                    "alias",
                    models.CharField(
                        max_length=60, unique=True, verbose_name="Прозвище"
                    ),
                ),
                ("date_of_birth", models.DateField(verbose_name="Дата рождения")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
                ("content", models.TextField(unique=True, verbose_name="Oписание")),
            ],
            options={
                "verbose_name": "Герой",
                "verbose_name_plural": "Герои",
            },
        ),
    ]

# Generated by Django 4.2.10 on 2024-02-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
                ("job_title", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="team_img/")),
                ("description", models.TextField(verbose_name="О себе")),
                ("linkedin", models.CharField(max_length=1000)),
            ],
        ),
    ]

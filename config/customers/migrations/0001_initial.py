# Generated by Django 4.2.10 on 2024-02-21 12:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ApplicationsForCustomers",
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
                ("name", models.CharField(max_length=100, verbose_name="ФИО")),
                ("email", models.EmailField(max_length=200, verbose_name="Email")),
                (
                    "phone_number",
                    models.IntegerField(
                        help_text="Введите телефон клиента в формате: +996xxxxxxxxx",
                        verbose_name="Номер телефона",
                    ),
                ),
                ("company", models.CharField(max_length=200, verbose_name="Компания")),
                ("description", models.TextField(verbose_name="Описание")),
            ],
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OCRData",
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
                ("image_name", models.CharField(max_length=255)),
                ("extracted_text", models.TextField()),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

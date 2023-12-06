# Generated by Django 4.2.7 on 2023-11-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ImageModel",
            fields=[
                (
                    "uid",
                    models.IntegerField(
                        auto_created=True,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("description", models.CharField(blank=True, max_length=1024)),
                ("file", models.FileField(upload_to="storage")),
            ],
        ),
    ]
# Generated by Django 4.2.7 on 2023-11-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mcwall", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagemodel",
            name="file",
            field=models.ImageField(upload_to=""),
        ),
    ]

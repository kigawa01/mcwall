# Generated by Django 4.2.7 on 2023-11-19 14:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("mcwall", "0002_alter_imagemodel_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="imagemodel",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, editable=False
            ),
        ),
    ]

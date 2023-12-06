# Generated by Django 4.2.7 on 2023-11-20 17:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("mcwall", "0003_imagemodel_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagemodel",
            name="uid",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]

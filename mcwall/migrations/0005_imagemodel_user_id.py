# Generated by Django 4.2.7 on 2023-11-29 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mcwall", "0004_alter_imagemodel_uid"),
    ]

    operations = [
        migrations.AddField(
            model_name="imagemodel",
            name="user_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
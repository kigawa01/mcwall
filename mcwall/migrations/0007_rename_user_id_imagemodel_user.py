# Generated by Django 4.2.7 on 2023-11-29 10:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mcwall", "0006_alter_imagemodel_user_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="imagemodel",
            old_name="user_id",
            new_name="user",
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_alter_appuser_options_alter_appuser_managers_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="appuser",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="appuser",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]

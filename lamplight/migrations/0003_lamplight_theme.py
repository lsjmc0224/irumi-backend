# Generated by Django 4.2.5 on 2024-04-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lamplight", "0002_alter_lamplight_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="lamplight",
            name="theme",
            field=models.IntegerField(
                choices=[(1, "1"), (2, "2"), (3, "3")], default=1
            ),
        ),
    ]
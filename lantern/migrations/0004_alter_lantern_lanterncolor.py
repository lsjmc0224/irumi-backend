# Generated by Django 4.2.5 on 2024-04-18 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lantern", "0003_alter_lantern_lanterncolor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lantern",
            name="lanternColor",
            field=models.CharField(
                choices=[
                    ("pink", "pink"),
                    ("green", "green"),
                    ("purple", "purple"),
                    ("blue", "blue"),
                    ("yellow", "yellow"),
                ],
                default="pink",
                max_length=10,
            ),
        ),
    ]

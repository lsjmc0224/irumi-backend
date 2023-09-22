# Generated by Django 4.2.5 on 2023-09-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lantern", "0008_alter_report_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="lantern",
            name="is_liked",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="lantern",
            name="is_reported",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="report",
            name="key",
            field=models.CharField(default="pulfQ8fymA", max_length=10),
        ),
    ]
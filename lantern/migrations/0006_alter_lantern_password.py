# Generated by Django 4.2.5 on 2024-04-18 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lantern", "0005_alter_lantern_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lantern",
            name="password",
            field=models.CharField(max_length=4),
        ),
    ]

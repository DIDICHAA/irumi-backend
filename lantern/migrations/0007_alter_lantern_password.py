# Generated by Django 5.0.4 on 2024-04-18 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lantern', '0006_alter_lantern_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lantern',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lantern', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lantern',
            name='nickname',
            field=models.CharField(max_length=8),
        ),
    ]
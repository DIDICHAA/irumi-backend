# Generated by Django 5.0.4 on 2024-04-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lantern', '0008_alter_report_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lanternreaction',
            name='user_id',
            field=models.CharField(max_length=36, null=True),
        ),
    ]
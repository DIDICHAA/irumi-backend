# Generated by Django 4.2.5 on 2023-09-23 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lantern', '0010_alter_report_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='key',
            field=models.CharField(default='xuuiykZMU4', max_length=10),
        ),
    ]

# Generated by Django 2.2 on 2021-01-16 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeAndLaborApp', '0008_auto_20210116_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduler',
            name='clock_out',
            field=models.TimeField(null=True),
        ),
    ]

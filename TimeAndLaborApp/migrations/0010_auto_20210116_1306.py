# Generated by Django 2.2 on 2021-01-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeAndLaborApp', '0009_auto_20210116_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduler',
            name='clock_in',
            field=models.TimeField(null=True),
        ),
    ]

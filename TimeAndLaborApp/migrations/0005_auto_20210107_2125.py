# Generated by Django 2.2.4 on 2021-01-07 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeAndLaborApp', '0004_auto_20210107_2058'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pto',
            new_name='Requested',
        ),
        migrations.RenameField(
            model_name='requested',
            old_name='PaidTimeOff',
            new_name='RequestedTimeOff',
        ),
        migrations.AddField(
            model_name='user',
            name='Pto',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='TimeOff',
        ),
    ]
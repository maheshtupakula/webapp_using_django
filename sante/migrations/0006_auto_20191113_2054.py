# Generated by Django 2.2.7 on 2019-11-13 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sante', '0005_remove_sell_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmer',
            name='dob',
        ),
        migrations.AddField(
            model_name='farmer',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]

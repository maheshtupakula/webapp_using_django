# Generated by Django 2.2.7 on 2019-11-13 07:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sante', '0002_sell_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 13, 7, 23, 16, 620811, tzinfo=utc)),
        ),
    ]

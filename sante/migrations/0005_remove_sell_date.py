# Generated by Django 2.2.7 on 2019-11-13 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sante', '0004_auto_20191113_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell',
            name='date',
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-16 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sante', '0009_auto_20191115_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='p_type',
            field=models.CharField(default='', max_length=20),
        ),
    ]

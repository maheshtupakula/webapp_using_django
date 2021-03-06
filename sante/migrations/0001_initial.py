# Generated by Django 2.2.7 on 2019-11-13 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=200)),
                ('dob', models.DateField(default=None)),
                ('street', models.CharField(default='', max_length=30)),
                ('city', models.CharField(default='', max_length=30)),
                ('district', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='sell',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('f_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='famer', to='sante.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('f_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farmer', to='sante.farmer')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell', to='sante.sell')),
            ],
        ),
    ]

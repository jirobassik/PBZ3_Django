# Generated by Django 4.1.1 on 2022-09-24 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectmodel',
            name='season_date_close',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Сезонный день закрытия'),
        ),
        migrations.AlterField(
            model_name='objectmodel',
            name='season_date_open',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Сезонный день открытия'),
        ),
    ]

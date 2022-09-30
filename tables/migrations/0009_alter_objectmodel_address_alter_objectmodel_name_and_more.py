# Generated by Django 4.1.1 on 2022-09-29 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0008_alter_ownermodel_opening_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectmodel',
            name='address',
            field=models.CharField(max_length=50, verbose_name='Адресс объекта'),
        ),
        migrations.AlterField(
            model_name='objectmodel',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Название объекта'),
        ),
        migrations.AlterField(
            model_name='objectmodel',
            name='type_o',
            field=models.CharField(max_length=30, verbose_name='Тип объекта'),
        ),
    ]

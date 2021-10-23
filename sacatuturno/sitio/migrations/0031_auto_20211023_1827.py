# Generated by Django 3.2.6 on 2021-10-23 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0030_auto_20211023_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='confirmado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='turno',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 18, 27, 9, 335850), verbose_name='Fecha inicio'),
        ),
    ]
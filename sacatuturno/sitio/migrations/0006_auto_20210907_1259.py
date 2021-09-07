# Generated by Django 3.2.6 on 2021-09-07 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0005_alter_userprofile_key_expires'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='apellido',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nombre',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2021, 9, 7)),
        ),
    ]

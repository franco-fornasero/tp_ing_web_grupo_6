# Generated by Django 3.2.6 on 2021-09-28 17:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sitio', '0010_alter_userprofile_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicioprestado',
            name='descripcion',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='servicioprestado',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2021, 9, 28)),
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField(verbose_name='Fecha inicio')),
                ('fecha_fin', models.DateTimeField(verbose_name='Fecha fin')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.servicioprestado')),
            ],
        ),
    ]
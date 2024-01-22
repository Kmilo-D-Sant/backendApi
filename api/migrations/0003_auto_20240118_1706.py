# Generated by Django 3.2.12 on 2024-01-18 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20240118_0129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'usuario', 'verbose_name_plural': 'usuarios'},
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nivel',
        ),
        migrations.AddField(
            model_name='usuario',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='es_vendedor',
            field=models.BooleanField(default=False, verbose_name='Es vendedor'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 18, 17, 5, 55, 195139)),
        ),
    ]

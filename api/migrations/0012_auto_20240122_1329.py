# Generated by Django 3.2.12 on 2024-01-22 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20240122_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, default='', null=True, upload_to='imagenes/'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 22, 13, 29, 57, 886687)),
        ),
    ]

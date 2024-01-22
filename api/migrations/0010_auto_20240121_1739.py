# Generated by Django 3.2.12 on 2024-01-21 22:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20240121_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 21, 17, 39, 52, 440121)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='imagenes/'),
        ),
    ]
# Generated by Django 5.1.4 on 2025-01-09 09:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mayatplast', '0003_contactusmodel_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactusmodel',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Baxıldı'),
        ),
        migrations.AlterField(
            model_name='contactusmodel',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

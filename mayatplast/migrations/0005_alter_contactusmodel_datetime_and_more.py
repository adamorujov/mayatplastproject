# Generated by Django 5.1.4 on 2025-01-09 10:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mayatplast', '0004_contactusmodel_status_alter_contactusmodel_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusmodel',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Göndərildi'),
        ),
        migrations.AlterField(
            model_name='contactusmodel',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Ad, Soyad'),
        ),
        migrations.AlterField(
            model_name='contactusmodel',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Oxundu'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='logo',
            field=models.TextField(blank=True, null=True, verbose_name='Loqo'),
        ),
        migrations.AlterField(
            model_name='socialmediamodel',
            name='icon_name',
            field=models.TextField(verbose_name='İkon'),
        ),
    ]

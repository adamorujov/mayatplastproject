# Generated by Django 5.1.4 on 2025-01-09 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mayatplast', '0002_alter_bannermodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactusmodel',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 9, 9, 23, 40, 514356, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='about_banner',
            field=models.ImageField(blank=True, null=True, upload_to='page_banners/', verbose_name='Haqqımızda səhifəsi'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='about_image1',
            field=models.ImageField(blank=True, null=True, upload_to='about_images/', verbose_name='Foto 1'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='about_image2',
            field=models.ImageField(blank=True, null=True, upload_to='about_images/', verbose_name='Foto 2'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='photo_banner',
            field=models.ImageField(blank=True, null=True, upload_to='page_banners/', verbose_name='Foto səhifəsi'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='slogan',
            field=models.TextField(blank=True, null=True, verbose_name='Mətn'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='slogan_image',
            field=models.ImageField(blank=True, null=True, upload_to='slogans/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='slogan_title',
            field=models.TextField(blank=True, null=True, verbose_name='Başlıq'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='video_banner',
            field=models.ImageField(blank=True, null=True, upload_to='page_banners/', verbose_name='Video səhifəsi'),
        ),
    ]

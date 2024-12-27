# Generated by Django 5.1.4 on 2024-12-26 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mayatplast', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bannermodel',
            options={'verbose_name': 'Banner', 'verbose_name_plural': 'Bannerlər'},
        ),
        migrations.AlterModelOptions(
            name='settingsmodel',
            options={'verbose_name': 'Parametr', 'verbose_name_plural': 'Parametrlər'},
        ),
        migrations.AlterModelOptions(
            name='socialmediamodel',
            options={'verbose_name': 'Sosial media hesabı', 'verbose_name_plural': 'Sosial media hesabları'},
        ),
        migrations.AddField(
            model_name='settingsmodel',
            name='about_banner',
            field=models.ImageField(blank=True, null=True, upload_to='page_banners/', verbose_name='Haqqımızda banner'),
        ),
        migrations.AddField(
            model_name='settingsmodel',
            name='photo_banner',
            field=models.ImageField(blank=True, null=True, upload_to='page_banners/', verbose_name='Foto banner'),
        ),
        migrations.AddField(
            model_name='settingsmodel',
            name='video_banner',
            field=models.ImageField(blank=True, null=True, upload_to='page_banners/', verbose_name='Video banner'),
        ),
    ]

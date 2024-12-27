# Generated by Django 5.1.4 on 2024-12-26 18:41

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Başlıq')),
                ('text', models.TextField(verbose_name='Mətn')),
                ('image', models.ImageField(blank=True, null=True, upload_to='banner_images/', verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Bannerlər',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Ad')),
            ],
            options={
                'verbose_name': 'Kateqoriya',
                'verbose_name_plural': 'Kateqoriyalar',
            },
        ),
        migrations.CreateModel(
            name='ContactInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefon nömrəsi')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Ünvan')),
            ],
            options={
                'verbose_name': 'Əlaqə məlumatı',
                'verbose_name_plural': 'Əlaqə məlumatları',
            },
        ),
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ad, soyad')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Mesaj')),
            ],
            options={
                'verbose_name': 'Mesaj',
                'verbose_name_plural': 'Mesajlar',
            },
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photo_gallery/', verbose_name='Foto')),
                ('title', models.TextField(blank=True, null=True, verbose_name='Başlıq')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotolar',
            },
        ),
        migrations.CreateModel(
            name='NewsTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Xəbər teqi',
                'verbose_name_plural': 'Xəbər teqləri',
            },
        ),
        migrations.CreateModel(
            name='SettingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/', verbose_name='Loqo')),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='favicons/', verbose_name='İkon')),
                ('contact_number', models.CharField(blank=True, max_length=25, null=True, verbose_name='Əlaqə nömrəsi')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('about_text', models.TextField(blank=True, null=True, verbose_name='Biz kimik?')),
                ('about_image1', models.ImageField(blank=True, null=True, upload_to='about_images/', verbose_name='Haqqımızda foto 1')),
                ('about_image2', models.ImageField(blank=True, null=True, upload_to='about_images/', verbose_name='Haqqımızda foto 2')),
                ('slogan_title', models.TextField(blank=True, null=True, verbose_name='Sloqan başlığı')),
                ('slogan', models.TextField(blank=True, null=True, verbose_name='Sloqan mətni')),
                ('slogan_image', models.ImageField(blank=True, null=True, upload_to='slogans/', verbose_name='Sloqan foto')),
                ('keywords', models.TextField(blank=True, null=True, verbose_name='Açar sözlər')),
                ('description', models.TextField(blank=True, null=True, verbose_name='İzah')),
            ],
            options={
                'verbose_name': 'Parametrlər',
            },
        ),
        migrations.CreateModel(
            name='SocialMediaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_name', models.CharField(max_length=50, verbose_name='İkon adı')),
                ('link', models.URLField(verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Sosial medial hesabları',
            },
        ),
        migrations.CreateModel(
            name='StatisticsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_name', models.CharField(max_length=50, verbose_name='İkon adı')),
                ('title', models.TextField(verbose_name='Başlıq')),
                ('text', models.TextField(verbose_name='Mətn')),
            ],
            options={
                'verbose_name': 'Statistika',
                'verbose_name_plural': 'Statistikalar',
            },
        ),
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video_gallery/', verbose_name='Video')),
                ('title', models.TextField(blank=True, null=True, verbose_name='Başlıq')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videolar',
            },
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news_images/', verbose_name='Foto')),
                ('title', models.TextField(verbose_name='Başlıq')),
                ('short_text', models.TextField(verbose_name='Qısa mətn')),
                ('long_text', tinymce.models.HTMLField(verbose_name='Geniş mətn')),
                ('date', models.DateField(auto_now_add=True)),
                ('tags', models.ManyToManyField(related_name='tag_news', to='mayatplast.newstagmodel', verbose_name='Teqlər')),
            ],
            options={
                'verbose_name': 'Xəbər',
                'verbose_name_plural': 'Xəbərlər',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Başlıq')),
                ('about', models.TextField(verbose_name='Haqqında')),
                ('image', models.ImageField(upload_to='product_images/', verbose_name='Foto')),
                ('use_fields', tinymce.models.HTMLField(blank=True, null=True, verbose_name='İstifadə sahələri')),
                ('main_features', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Əsas xüsusiyyətlər')),
                ('dimensions', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Ölçülər')),
                ('dimension1', models.FloatField(blank=True, null=True, verbose_name='1-ci ölçü')),
                ('dimension2', models.FloatField(blank=True, null=True, verbose_name='2-ci ölçü')),
                ('dimension3', models.FloatField(blank=True, null=True, verbose_name='3-cü ölçü')),
                ('keywords', models.TextField(blank=True, null=True, verbose_name='Açar sözlər')),
                ('description', models.TextField(blank=True, null=True, verbose_name='İzah')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='mayatplast.categorymodel', verbose_name='Kateqoriya')),
            ],
            options={
                'verbose_name': 'Məhsul',
                'verbose_name_plural': 'Məhsullar',
            },
        ),
    ]

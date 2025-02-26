from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
from django.utils.functional import lazy
from django.utils.html import mark_safe

class SettingsModel(models.Model):
    #main
    logo = models.TextField("Loqo", blank=True, null=True)
    favicon = models.ImageField("İkon", upload_to="favicons/", blank=True, null=True)
    contact_number = models.CharField("Əlaqə nömrəsi", max_length=25, blank=True, null=True)
    email = models.EmailField("Email", max_length=50, blank=True, null=True)
    #about
    about_text = models.TextField("Biz kimik?", blank=True, null=True)
    about_image1 = models.ImageField("Foto 1", upload_to="about_images/", blank=True, null=True)
    about_image2 = models.ImageField("Foto 2", upload_to="about_images/", blank=True, null=True)
    #slogan
    slogan_title = models.TextField("Başlıq", blank=True, null=True)
    slogan = models.TextField("Mətn", blank=True, null=True)
    slogan_image = models.ImageField("Foto", upload_to="slogans/", blank=True, null=True)
    #page banners
    about_banner = models.ImageField("Haqqımızda səhifəsi", upload_to="page_banners/", blank=True, null=True)
    video_banner = models.ImageField("Video səhifəsi", upload_to="page_banners/", blank=True, null=True)
    photo_banner = models.ImageField("Foto səhifəsi", upload_to="page_banners/", blank=True, null=True)
    #meta
    keywords = models.TextField("Açar sözlər", blank=True, null=True)
    description = models.TextField("İzah", blank=True, null=True)

    class Meta:
        verbose_name = "Parametr"
        verbose_name_plural = "Parametrlər"

    def save(self, *args, **kwargs):
        if not self.id and SettingsModel.objects.all().count() >= 1:
            raise ValueError("Yeni obyekt yaradıla bilməz!")
        return super(SettingsModel, self).save(*args, **kwargs)
    def __str__(self):
        return "Parametrlər"
    
class SocialMediaModel(models.Model):
    icon_name = models.TextField("İkon")
    link = models.URLField("Link")

    class Meta:
        verbose_name = "Sosial media hesabı"
        verbose_name_plural = "Sosial media hesabları"
        ordering = ("-id",)

    def __str__(self):
        return self.icon_name
    
class BannerModel(models.Model):
    title = models.TextField("Başlıq")
    text = models.TextField("Mətn")
    image = models.ImageField("Foto", upload_to="banner_images/", blank=True, null=True)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlər"
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
class StatisticsModel(models.Model):
    icon_name = models.TextField("İkon")
    title = models.TextField("Başlıq")
    text = models.TextField("Mətn")

    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Statistikalar"
        ordering = ("-id",)

    def __str__(self):
        return self.title

class ContactInfoModel(models.Model):
    phone_number = models.CharField("Telefon nömrəsi", max_length=20, blank=True, null=True)
    email = models.EmailField("Email", max_length=100, blank=True, null=True)
    address = models.TextField("Ünvan", blank=True, null=True)

    class Meta:
        verbose_name = "Əlaqə məlumatı"
        verbose_name_plural = "Əlaqə məlumatları"
        ordering = ("-id",)

    def __str__(self):
        return self.phone_number
    
class CategoryModel(models.Model):
    name = models.TextField("Ad")

    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class DimensionModel(models.Model):
    dimension1 = models.FloatField("1-ci ölçü", blank=True, null=True)
    dimension2 = models.FloatField("2-ci ölçü", blank=True, null=True)
    dimension3 = models.FloatField("3-cü ölçü", blank=True, null=True)

    class Meta:
        verbose_name = "Ölçü"
        verbose_name_plural = "Ölçülər"
        ordering = ("-id",)

    def __str__(self):
        return "Ölçü " + str(self.id)

class ProductModel(models.Model):
    #main
    title = models.TextField("Başlıq")
    about = models.TextField("Haqqında")
    image = models.ImageField("Foto", upload_to="product_images/")
    use_fields = HTMLField("İstifadə sahələri", blank=True, null=True)
    main_features = HTMLField("Əsas xüsusiyyətlər", blank=True, null=True)
    dimensions = HTMLField("Ölçülər", blank=True, null=True)
    category = models.ForeignKey(CategoryModel, verbose_name="Kateqoriya", on_delete=models.CASCADE, related_name="products")
    #parameters
    product_dimensions = models.ManyToManyField(DimensionModel, verbose_name="Ölçü", related_name="d_products")
    #meta
    keywords = models.TextField("Açar sözlər", blank=True, null=True)
    description = models.TextField("İzah", blank=True, null=True)

    class Meta:
        verbose_name = "Məhsul"
        verbose_name_plural = "Məhsullar"
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
class NewsTagModel(models.Model):
    name = models.CharField("Tag", max_length=50)

    class Meta:
        verbose_name = "Xəbər teqi"
        verbose_name_plural = "Xəbər teqləri"
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class NewsModel(models.Model):
    image = models.ImageField("Foto", upload_to="news_images/")
    title = models.TextField("Başlıq")
    short_text = models.TextField("Qısa mətn")
    long_text = HTMLField("Geniş mətn")
    date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(NewsTagModel, verbose_name="Teqlər", related_name="tag_news")

    class Meta:
        verbose_name = "Xəbər"
        verbose_name_plural = "Xəbərlər"
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
class VideoModel(models.Model):
    video = models.FileField("Video", upload_to="video_gallery/")
    title = models.TextField("Başlıq", blank=True, null=True)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videolar"
        ordering = ("-id",)

    def __str__(self):
        return self.video.name

class ImageModel(models.Model):
    image = models.ImageField("Foto", upload_to="photo_gallery/")
    title = models.TextField("Başlıq", blank=True, null=True)

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotolar"
        ordering = ("-id",)

    def __str__(self):
        return self.image.name

class ContactUsModel(models.Model):
    name = models.CharField("Ad, Soyad", max_length=50)
    email = models.EmailField("Email", max_length=255)
    message = models.TextField("Mesaj")
    datetime = models.DateTimeField("Göndərildi", default=timezone.now)
    status = models.BooleanField("Oxundu", default=False)

    class Meta:
        verbose_name = "Mesaj"
        verbose_name_plural = "Mesajlar"
        ordering = ("status", "-id",)

    def __str__(self):
        return self.name


from django.db import models
from tinymce.models import HTMLField

class SettingsModel(models.Model):
    #main
    logo = models.ImageField("Loqo", upload_to="logos/", blank=True, null=True)
    favicon = models.ImageField("İkon", upload_to="favicons/", blank=True, null=True)
    contact_number = models.CharField("Əlaqə nömrəsi", max_length=25, blank=True, null=True)
    email = models.EmailField("Email", max_length=50, blank=True, null=True)
    #about
    about_text = models.TextField("Biz kimik?", blank=True, null=True)
    about_image1 = models.ImageField("Haqqımızda foto 1", upload_to="about_images/", blank=True, null=True)
    about_image2 = models.ImageField("Haqqımızda foto 2", upload_to="about_images/", blank=True, null=True)
    #slogan
    slogan_title = models.TextField("Sloqan başlığı", blank=True, null=True)
    slogan = models.TextField("Sloqan mətni", blank=True, null=True)
    slogan_image = models.ImageField("Sloqan foto", upload_to="slogans/", blank=True, null=True)
    #page banners
    about_banner = models.ImageField("Haqqımızda banner", upload_to="page_banners/", blank=True, null=True)
    video_banner = models.ImageField("Video banner", upload_to="page_banners/", blank=True, null=True)
    photo_banner = models.ImageField("Foto banner", upload_to="page_banners/", blank=True, null=True)
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
    icon_name = models.CharField("İkon adı", max_length=50)
    link = models.URLField("Link")

    class Meta:
        verbose_name = "Sosial media hesabı"
        verbose_name_plural = "Sosial media hesabları"

    def __str__(self):
        return self.icon_name
    
class BannerModel(models.Model):
    title = models.TextField("Başlıq")
    text = models.TextField("Mətn")
    image = models.ImageField("Foto", upload_to="banner_images/", blank=True, null=True)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlər"

    def __str__(self):
        return self.title
    
class StatisticsModel(models.Model):
    icon_name = models.CharField("İkon adı", max_length=50)
    title = models.TextField("Başlıq")
    text = models.TextField("Mətn")

    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Statistikalar"

    def __str__(self):
        return self.title

class ContactInfoModel(models.Model):
    phone_number = models.CharField("Telefon nömrəsi", max_length=20, blank=True, null=True)
    email = models.EmailField("Email", max_length=100, blank=True, null=True)
    address = models.TextField("Ünvan", blank=True, null=True)

    class Meta:
        verbose_name = "Əlaqə məlumatı"
        verbose_name_plural = "Əlaqə məlumatları"

    def __str__(self):
        return self.phone_number
    
class CategoryModel(models.Model):
    name = models.TextField("Ad")

    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"

    def __str__(self):
        return self.name

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
    dimension1 = models.FloatField("1-ci ölçü", blank=True, null=True)
    dimension2 = models.FloatField("2-ci ölçü", blank=True, null=True)
    dimension3 = models.FloatField("3-cü ölçü", blank=True, null=True)
    #meta
    keywords = models.TextField("Açar sözlər", blank=True, null=True)
    description = models.TextField("İzah", blank=True, null=True)

    class Meta:
        verbose_name = "Məhsul"
        verbose_name_plural = "Məhsullar"

    def __str__(self):
        return self.title
    
class NewsTagModel(models.Model):
    name = models.CharField("Tag", max_length=50)

    class Meta:
        verbose_name = "Xəbər teqi"
        verbose_name_plural = "Xəbər teqləri"

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

    def __str__(self):
        return self.title
    
class VideoModel(models.Model):
    video = models.FileField("Video", upload_to="video_gallery/")
    title = models.TextField("Başlıq", blank=True, null=True)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videolar"

    def __str__(self):
        return "Video (" + str(self.id) + ")"

class ImageModel(models.Model):
    image = models.ImageField("Foto", upload_to="photo_gallery/")
    title = models.TextField("Başlıq", blank=True, null=True)

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotolar"

    def __str__(self):
        return "Foto (" + str(self.id) + ")"

class ContactUsModel(models.Model):
    name = models.CharField("Ad, soyad", max_length=50)
    email = models.EmailField("Email", max_length=255)
    message = models.TextField("Mesaj")

    class Meta:
        verbose_name = "Mesaj"
        verbose_name_plural = "Mesajlar"

    def __str__(self):
        return self.name


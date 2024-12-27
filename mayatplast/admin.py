from django.contrib import admin
from mayatplast.models import (
    SettingsModel, SocialMediaModel, BannerModel, StatisticsModel, ContactInfoModel, 
    CategoryModel, ProductModel, NewsTagModel, NewsModel, VideoModel, ImageModel, ContactUsModel
)

admin.site.register(SettingsModel)
admin.site.register(SocialMediaModel)
admin.site.register(BannerModel)
admin.site.register(StatisticsModel)
admin.site.register(ContactInfoModel)
admin.site.register(CategoryModel)
admin.site.register(ProductModel)
admin.site.register(NewsTagModel)
admin.site.register(NewsModel)
admin.site.register(VideoModel)
admin.site.register(ImageModel)
admin.site.register(ContactUsModel)
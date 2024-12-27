from rest_framework import serializers
from mayatplast.models import (
    SettingsModel, SocialMediaModel, BannerModel, StatisticsModel, ContactInfoModel, 
    CategoryModel, ProductModel, NewsTagModel, NewsModel, VideoModel, ImageModel, ContactUsModel
)

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsModel
        fields = "__all__"

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaModel
        fields = "__all__"

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        fields = "__all__"

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatisticsModel
        fields = "__all__"

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfoModel
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = ProductModel
        fields = "__all__"

class NewsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTagModel
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    tags = NewsTagSerializer(many=True)
    class Meta:
        model = NewsModel
        fields = "__all__"

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoModel
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = "__all__"

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsModel
        fields = "__all__"

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from mayatplast.models import (
    SettingsModel, SocialMediaModel, BannerModel, StatisticsModel, ContactInfoModel, 
    CategoryModel, ProductModel, NewsTagModel, NewsModel, VideoModel, ImageModel, ContactUsModel
)
from mayatplast.api.serializers import (
    SettingsSerializer, SocialMediaSerializer, BannerSerializer, StatisticsSerializer, ContactInfoSerializer,
    CategorySerializer, ProductSerializer, NewsTagSerializer, NewsSerializer, VideoSerializer, ImageSerializer, ContactUsSerializer
)
from django.shortcuts import get_object_or_404
from django.db.models import Count, Q

class SettingsListAPIView(ListAPIView):
    queryset = SettingsModel.objects.all()
    serializer_class = SettingsSerializer

class SocialMediaListAPIView(ListAPIView):
    queryset = SocialMediaModel.objects.all()
    serializer_class = SocialMediaSerializer

class BannerListAPIView(ListAPIView):
    queryset = BannerModel.objects.all()
    serializer_class = BannerSerializer

class StatisticsListAPIView(ListAPIView):
    queryset = StatisticsModel.objects.all()
    serializer_class = StatisticsSerializer

class ContactInfoListAPIView(ListAPIView):
    queryset = ContactInfoModel.objects.all()
    serializer_class = ContactInfoSerializer

class CategoryListAPIView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class ProductListAPIView(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class CategoryProductListAPIView(ListAPIView):
    def get_queryset(self):
        category_id = self.kwargs.get("id")
        category = get_object_or_404(CategoryModel, id=category_id)
        return ProductModel.objects.filter(category=category)
    serializer_class = ProductSerializer

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

class NewsListAPIView(ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer

class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    lookup_field = "id"

class RelatedNewsListAPIView(ListAPIView):
    def get_queryset(self):
        id = self.kwargs.get("id")
        news = get_object_or_404(NewsModel, id=id)
        return NewsModel.objects.filter(
            tags__in=news.tags.all()
            ).exclude(id=news.id).distinct().annotate(
                matched_tag_count=Count('tags', filter=Q(tags__in=news.tags.all()))
            ).order_by('-matched_tag_count')
    serializer_class = NewsSerializer
    
class VideoListAPIView(ListAPIView):
    queryset = VideoModel.objects.all()
    serializer_class = VideoSerializer

class ImageListAPIView(ListAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer

class ContactUsCreateAPIView(CreateAPIView):
    queryset = ContactUsModel.objects.all()
    serializer_class = ContactUsSerializer

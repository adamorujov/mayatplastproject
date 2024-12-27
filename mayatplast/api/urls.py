from django.urls import path
from mayatplast.api import views

urlpatterns = [
    path('settings/', views.SettingsListAPIView.as_view(), name="settings"),
    path('socialmedia-list/', views.SocialMediaListAPIView.as_view(), name="socialmedia-list"),
    path('banner-list/', views.BannerListAPIView.as_view(), name="banner-list"),
    path('statistics-list/', views.StatisticsListAPIView.as_view(), name="statistics-list"),
    path('contactinfo-list/', views.ContactInfoListAPIView.as_view(), name="contactinfo-list"),
    path('category-list/', views.CategoryListAPIView.as_view(), name="category-list"),
    path('category-product-list/<int:id>/', views.CategoryProductListAPIView.as_view(), name="category-product-list"),
    path('product-retrieve/<int:id>/', views.ProductRetrieveAPIView.as_view(), name="product-retrieve"),
    path('news-list/', views.NewsListAPIView.as_view(), name="news-list"),
    path('news-retrieve/<int:id>/', views.NewsRetrieveAPIView.as_view(), name="news-retrieve"),
    path('related-news-list/<int:id>/', views.RelatedNewsListAPIView.as_view(), name="related-news-list"),
    path('video-list/', views.VideoListAPIView.as_view(), name="video-list"),
    path('image-list/', views.ImageListAPIView.as_view(), name="image-list"),
    path('contactus-create/', views.ContactUsCreateAPIView.as_view(), name="contactus-create"),
]
from django.contrib import admin, messages
from mayatplast.models import (
    SettingsModel, SocialMediaModel, BannerModel, StatisticsModel, ContactInfoModel, 
    CategoryModel, ProductModel, NewsTagModel, NewsModel, VideoModel, ImageModel, ContactUsModel, DimensionModel
)
from django.contrib.auth.models import Group

@admin.register(SettingsModel)
class SettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("SAYTIN ƏSAS PARAMETRLƏRİ", {'fields': ('logo', 'favicon', 'contact_number', 'email')}),
        ("HAQQIMIZDA", {'fields': ('about_text', 'about_image1', 'about_image2')}),
        ("SLOQAN", {'fields': ('slogan_title', 'slogan', 'slogan_image')}),
        ("SƏHİFƏ BANNERLƏRİ", {'fields': ('about_banner', 'photo_banner', 'video_banner')}),
        ("META PARAMETRLƏR", {'fields': ('keywords', 'description')}),   
    )

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

# admin.site.register(SettingsModel)
admin.site.register(SocialMediaModel)
admin.site.register(BannerModel)
admin.site.register(StatisticsModel)
admin.site.register(ContactInfoModel)
admin.site.register(CategoryModel)

@admin.register(DimensionModel)
class DimensionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "dimension1", "dimension2", "dimension3")

admin.site.register(ProductModel)
admin.site.register(NewsTagModel)
admin.site.register(NewsModel)
admin.site.register(VideoModel)
admin.site.register(ImageModel)

@admin.register(ContactUsModel)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "datetime", "status")
    readonly_fields = ("name", "email", "message", "datetime")
    actions = ['mark_as_read', 'mark_as_unread']

    def has_add_permission(self, request):
        return False
    
    @admin.action(description="Oxunmuş kimi işarələ")
    def mark_as_read(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, "Seçilmiş mesajlar oxunmuş kimi işarələndi.", messages.SUCCESS)

    @admin.action(description="Oxunmamış kimi işarələ")
    def mark_as_unread(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, "Seçilmiş mesajlar oxunmamış kimi işarələndi.", messages.SUCCESS)

    def changelist_view(self, request, extra_context=None):
        # Customize title for the model's list page
        extra_context = extra_context or {}
        extra_context['title'] = f"{self.model.objects.filter(status=False).count()} oxunmamış mesaj mövcuddur"
        return super().changelist_view(request, extra_context=extra_context)
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        # Customize title for the model's edit page
        extra_context = extra_context or {}
        obj = self.get_object(request, object_id)
        extra_context['title'] = f"Mesaj"
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


admin.AdminSite.site_header = "MAYAT Plast administrasiyası"
admin.AdminSite.site_title = "MAYAT Plast administrasiyası"
admin.AdminSite.index_title = "MAYAT Plast"
admin.site.unregister(Group)

def get_app_list(self, request, app_label=None):
        app_dict = self._build_app_dict(request)
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        for app in app_list:
            if app['app_label'] == 'mayatplast':
                ordering = {
                    "Parametrlər": 1,
                    "Sosial media hesabları": 2,
                    "Bannerlər": 3,
                    "Statistikalar": 4,
                    "Əlaqə məlumatları": 5,
                    "Kateqoriyalar": 6,
                    "Ölçülər": 7,
                    "Məhsullar": 8,
                    "Xəbər teqləri": 9,
                    "Xəbərlər": 10,
                    "Fotolar": 11,
                    "Videolar": 12,
                    "Mesajlar": 13
                }
                app['models'].sort(key=lambda x: ordering[x['name']])

        return app_list

admin.AdminSite.get_app_list = get_app_list
from django.contrib import admin
from django.contrib.admin.sites import AdminSite

from .models import Gallery, FAQ, Message, Product


AdminSite.site_header = "Ares Mushroom"
AdminSite.site_title = "Ares Mushroom"


class GalleryAdmin(admin.ModelAdmin):
    list_display = ["id", "caption", "upload_date", "credit"]


class FAQAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "upload_date"]


class MessageAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "title", "upload_date"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "weight"]


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Product, ProductAdmin)

from django.contrib import admin
from .models import Gallery, FAQ, Message


class GalleryAdmin(admin.ModelAdmin):
    list_display = ["id", "caption", "upload_date", "credit"]


class FAQAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "upload_date"]


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(FAQ, FAQAdmin)

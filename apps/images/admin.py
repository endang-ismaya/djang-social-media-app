from django.contrib import admin

from apps.images.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "image", "created"]
    list_filter = ["created"]
    search_fields = ["title", "slug", "description"]

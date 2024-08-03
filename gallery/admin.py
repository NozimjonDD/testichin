from django.contrib import admin
from . import models


@admin.register(models.PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'slug',
        'title_uz',
        'title_ru',
        'title_en',
        'title_oz',
        'is_active',
    ]
    list_display_links = [
        'id',
        'slug',
    ]


@admin.register(models.PhotoGalleryAttachment)
class PhotoGalleryAttachmentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'slug',
        'photo',
        'views',
        'position',
        'is_active',
    ]
    list_display_links = [
        'id',
        'slug',
    ]


@admin.register(models.VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'slug',
        'title_uz',
        'title_ru',
        'title_en',
        'title_oz',
        'poster',
        'is_active',
    ]
    list_display_links = [
        'id',
        'slug',
    ]


@admin.register(models.VideoGalleryAttachment)
class VideoGalleryAttachmentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'slug',
        'video',
        'frame_of_video',
        'views',
        'position',
        'is_active',
    ]
    list_display_links = [
        'id',
        'slug',
    ]


@admin.register(models.VideoGalleryUrl)
class VideoGalleryUrlsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'poster',
        'url',
    ]
    list_display_links = [
        'id',
    ]

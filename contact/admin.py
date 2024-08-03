from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'address',
        'email',
        'bus',
        'mini_bus',
        'subway',
        'reference_point',
        'phone',
        'fax',
        'office',
        'photo',
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday',
        'telegram_link',
        'youtube_link',
        'instagram_link',
        'facebook_link',
    )

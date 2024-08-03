from django.contrib import admin

from .models import Faq, FaqTheme


class FaqThemeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'is_active',
        'order'
    ]
    list_display_links = ['title']


class FaqAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'question',
        'theme',
        'is_active',
        'order'
    ]
    list_display_links = ['question']


admin.site.register(FaqTheme, FaqThemeAdmin)
admin.site.register(Faq, FaqAdmin)

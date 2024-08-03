from django.contrib import admin

from .models import Menu, MenuImage


class MenuImageInline(admin.TabularInline):
    model = MenuImage


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'group',
        'is_static',
        'is_active',
        'has_category',
        'position'
    )
    list_display_links = (
        'id',
        'title',
    )
    inlines = [MenuImageInline]
    search_fields = [
        'title_uz',
        'title_ru',
        'title_en',
        'title_oz',
        'title_qr',
        'content_uz',
        'content_ru',
        'content_en',
        'content_oz',
        'content_qr',
    ]


admin.site.register(Menu, MenuAdmin)

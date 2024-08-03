from django.contrib import admin

from .models import (
    Post,
    PostImage,
    PostAttachment,
    Tag,
    ContestButton,
)


class PostImageInline(admin.TabularInline):
    model = PostImage


class PostAttachmentInline(admin.TabularInline):
    model = PostAttachment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'menus',
        'menu_groups',
        'title',
        'slug',
        'short_content',
        'pub_date',
        'is_active',
        'on_slider',
        'all_tags',
        'position',
    ]
    list_display_links = (
        'id',
        'slug',
        'title',
    )
    inlines = (
        PostImageInline,
        PostAttachmentInline,
    )
    readonly_fields = [
        'id',
        'created_at',
        'updated_at',
    ]
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

    def all_tags(self, obj):
        return ", ".join([tag.title for tag in obj.tags.all()])

    def menus(self, obj):
        return ", ".join([str(menu.pk) for menu in obj.menu.all()])

    def menu_groups(self, obj):
        return ", ".join([str(menu.group) for menu in obj.menu.all()])


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug',)


@admin.register(ContestButton)
class ContestButtonAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'url',
        'position',
        'is_active',
    ]
    list_display_links = (
        'id',
        'title',
    )

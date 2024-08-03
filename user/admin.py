from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Common", {
            "fields": (
                'role',
                "middle_name",
                "image",
                "phone",
                "profession",
                "gender",
                "birth_date",
            )
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Main", {
            "fields": (
                "first_name",
                "middle_name",
                "last_name",
                "is_superuser",
                "is_staff",
                "is_active",
            )
        }),
    )
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'role',
        'date_joined',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    list_display_links = (
        'username',
    )
    list_filter = ['is_active', 'is_staff', 'is_superuser', 'role']
    ordering = ['-date_joined']
    search_fields = ('username', 'first_name', 'last_name',)


admin.site.register(User, CustomUserAdmin)

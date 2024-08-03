from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'status',
    )
    list_display_links = ['full_name']

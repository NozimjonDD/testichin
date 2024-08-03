from django.contrib import admin

from event_media_plan.models import (
    EventMediaPlan,
    EventType,
    EventMediaPlanAttachment,
    EventMediaPlanImage
)

admin.site.register(EventMediaPlan)
admin.site.register(EventType)
admin.site.register(EventMediaPlanAttachment)
admin.site.register(EventMediaPlanImage)

# @admin.register(EventMediaPlan)
# class Event_Media_planAdmin(admin.ModelAdmin):
#     list_display = [
#         'id',
#         'title',
#         'slug',
#         'content',
#         'event_name',
#         'event_type',
#         'position',
#         'type',
#         'event_begin',
#         'event_end',
#         'address',
#         'photo',
#         'organization',
#         'alias',
#         'is_status',
#         'is_active',
#     ]
#     list_display_links = [
#         'id',
#         'title',
#         'content',
#     ]

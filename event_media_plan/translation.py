from modeltranslation.translator import translator, TranslationOptions

from event_media_plan.models import EventMediaPlan, EventType, EventMediaPlanAttachment


class EventMediaPlanTranslationOptions(TranslationOptions):
    fields = [
        'title',
        'content',
        'event_name',
        'address',
        'organization',
    ]


class EventTypeTranslationOptions(TranslationOptions):
    fields = ['title']


class EventMediaPlanAttachmentTranslationOptions(TranslationOptions):
    fields = ['title']


translator.register(EventMediaPlan, EventMediaPlanTranslationOptions)
translator.register(EventType, EventTypeTranslationOptions)
translator.register(EventMediaPlanAttachment, EventMediaPlanAttachmentTranslationOptions)

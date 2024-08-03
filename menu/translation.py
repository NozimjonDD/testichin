from modeltranslation.translator import translator, TranslationOptions
from .models import Menu, MenuAttachment


class MenuTranslationOptions(TranslationOptions):
    fields = ['title', 'content']


class MenuAttachmentTranslationOptions(TranslationOptions):
    fields = ['title']


translator.register(Menu, MenuTranslationOptions)
translator.register(MenuAttachment, MenuAttachmentTranslationOptions)

from modeltranslation.translator import translator, TranslationOptions

from .models import Post, Tag, PostAttachment, ContestButton


class PostTranslationOptions(TranslationOptions):
    fields = ['title', 'content', 'short_content']


class TagTranslationOptions(TranslationOptions):
    fields = ['title']


class PostAttachmentTranslationOptions(TranslationOptions):
    fields = ['title']


class ContestButtonTranslationOptions(TranslationOptions):
    fields = ['title']


translator.register(Post, PostTranslationOptions)
translator.register(Tag, TagTranslationOptions)
translator.register(PostAttachment, PostAttachmentTranslationOptions)
translator.register(ContestButton, ContestButtonTranslationOptions)

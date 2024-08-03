from modeltranslation.translator import translator, TranslationOptions
from .models import FaqTheme, Faq


class FaqThemeTranslationOptions(TranslationOptions):
    fields = ['title']


class FaqTranslationOptions(TranslationOptions):
    fields = ['question', 'answer']


translator.register(FaqTheme, FaqThemeTranslationOptions)
translator.register(Faq, FaqTranslationOptions)

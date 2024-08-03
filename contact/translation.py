from modeltranslation.translator import translator, TranslationOptions
from .models import Contact


class ContactTranslationOptions(TranslationOptions):
    fields = ('address', 'reference_point', 'subway')


translator.register(Contact, ContactTranslationOptions)

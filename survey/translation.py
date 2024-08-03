from modeltranslation.translator import translator, TranslationOptions

from survey.models import Survey, SurveyVariant


class SurveyTranslationOptions(TranslationOptions):
    fields = ('question',)


class SurveyVariantTranslationOptions(TranslationOptions):
    fields = ('text',)


translator.register(Survey, SurveyTranslationOptions)
translator.register(SurveyVariant, SurveyVariantTranslationOptions)

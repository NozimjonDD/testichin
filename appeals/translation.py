from modeltranslation.translator import translator, TranslationOptions
from appeals.models import AppealResponse, AppealStatics


class AppealResponseTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


class AppealStaticsTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(AppealResponse, AppealResponseTranslationOptions)
translator.register(AppealStatics, AppealStaticsTranslationOptions)

from modeltranslation.translator import translator, TranslationOptions
from common import models


class RegionTranslationOptions(TranslationOptions):
    fields = ('title',)


class DistrictTranslationOptions(TranslationOptions):
    fields = ('title',)


class SubDistrictTranslationOptions(TranslationOptions):
    fields = ('title',)


class InteractiveServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(models.Region, RegionTranslationOptions)
translator.register(models.District, DistrictTranslationOptions)
translator.register(models.SubDistrict, SubDistrictTranslationOptions)
translator.register(models.InteractiveService, InteractiveServiceTranslationOptions)

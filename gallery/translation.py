from modeltranslation.translator import translator, TranslationOptions
from gallery import models


class PhotoGalleryTranslationOptions(TranslationOptions):
    fields = ('title', )


class VideoGalleryTranslationOptions(TranslationOptions):
    fields = ('title', )


translator.register(models.PhotoGallery, PhotoGalleryTranslationOptions)
translator.register(models.VideoGallery, VideoGalleryTranslationOptions)

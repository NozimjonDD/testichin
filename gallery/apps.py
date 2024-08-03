from django.apps import AppConfig
from watson import search as watson


class GalleryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gallery'

    def ready(self):
        watson.register(self.get_model('PhotoGallery'))
        watson.register(self.get_model('VideoGallery'))

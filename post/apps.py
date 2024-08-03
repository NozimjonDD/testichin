from django.apps import AppConfig
from watson import search as watson


class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'

    def ready(self):
        watson.register(self.get_model('Post').objects.filter(is_active=True))

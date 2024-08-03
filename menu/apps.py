from django.apps import AppConfig
from watson import search as watson


class MenuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu'

    def ready(self):
        from menu import signals  # DO NOT REMOVE THIS IMPORT !!!
        watson.register(self.get_model('Menu').objects.filter(is_active=True).exclude(parent__isnull=True))

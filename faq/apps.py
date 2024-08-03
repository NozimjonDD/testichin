from django.apps import AppConfig
from watson import search as watson


class FaqConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'faq'

    def ready(self):
        watson.register(self.get_model('Faq').objects.filter(is_active=True))
        watson.register(self.get_model('FaqTheme').objects.filter(is_active=True))

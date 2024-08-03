from django.apps import AppConfig
from watson import search as watson


class StructureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'structure'

    def ready(self):
        watson.register(self.get_model('Staff').objects.filter(is_active=True))
        watson.register(self.get_model('Management').objects.filter(is_active=True))
        watson.register(self.get_model('Department').objects.filter(is_active=True))
        watson.register(self.get_model('Division').objects.filter(is_active=True))
        watson.register(self.get_model('Organization').objects.filter(is_active=True))
        # watson.register(self.get_model('InnovationCenter').objects.filter(is_active=True))
        watson.register(self.get_model('InnovationTerritory').objects.filter(is_active=True))

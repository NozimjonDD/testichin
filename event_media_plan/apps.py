from django.apps import AppConfig
from watson import search as watson


class EventMediaPlanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'event_media_plan'

    # def ready(self):
    #     watson.register(self.get_model('EventMediaPlan').objects.filter(is_active=True))

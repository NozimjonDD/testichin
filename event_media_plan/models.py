from django.db import models
from autoslug import AutoSlugField

from common.static_data import EventMediaPlanChoices, EventLevelChoices
from mininnovation_backend.models import Base


class EventMediaPlan(Base):
    def get_populate(self):
        return self.title_uz

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=get_populate, always_update=True, unique=True, null=True)
    content = models.TextField()
    event_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    event_type = models.ForeignKey('EventType', on_delete=models.PROTECT, related_name='eventmediaplans')
    event_level = models.PositiveSmallIntegerField(choices=EventLevelChoices.choices)
    type = models.PositiveSmallIntegerField(choices=EventMediaPlanChoices.choices)
    event_begin_datetime = models.DateTimeField(blank=True, null=True)
    event_end_datetime = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=1)


class EventType(Base):
    def get_populate(self):
        return self.title_uz

    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from=get_populate, always_update=True, unique=True, null=True)
    is_active = models.BooleanField(default=False)


class EventMediaPlanAttachment(Base):
    eventmediaplan = models.ForeignKey(EventMediaPlan, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='eventmediaplan_attachments/')
    title = models.CharField(max_length=150, blank=True, null=True)


class EventMediaPlanImage(Base):
    eventmediaplan = models.ForeignKey(EventMediaPlan, on_delete=models.CASCADE, related_name='images')
    file = models.ImageField(upload_to='eventmediaplan_images/')
    is_active = models.BooleanField(default=False)

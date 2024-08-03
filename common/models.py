from autoslug import AutoSlugField
from django.db import models

from common.static_data import ServiceTypeChoices, SpecialityTypeChoices
from mininnovation_backend.models import Base


class Region(Base):
    """  Regions of Uzbekistan"""
    title = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)


class District(Base):
    """ Districts of particular region """
    title = models.CharField(max_length=255)
    region = models.ForeignKey('Region', on_delete=models.DO_NOTHING, related_name='districts')

    def __str__(self):
        return str(self.title)


class SubDistrict(Base):
    """ Sub districts of particular district """
    title = models.CharField(max_length=255)
    district = models.ForeignKey('District', on_delete=models.CASCADE, related_name='subdistricts')

    def __str__(self):
        return str(self.title)


class InteractiveService(Base):
    def get_populate(self):
        return self.title_uz

    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255, blank=True, null=True)
    icon = models.ImageField(upload_to='interactive_services/')
    group = models.CharField(max_length=100, blank=True, null=True)
    type = models.IntegerField(choices=ServiceTypeChoices.choices, default=ServiceTypeChoices.INTERACTIVE_SERVICE)
    slug = AutoSlugField(populate_from=get_populate, always_update=True, unique=True, null=True)
    content = models.TextField(blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=1)
    is_startup = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['order']


class InteractiveServiceImage(Base):
    interactive_service = models.ForeignKey(InteractiveService, on_delete=models.CASCADE, related_name='images')
    file = models.ImageField(upload_to='interactive_services/images/')
    is_active = models.BooleanField(default=False)


class InnovationIdea(Base):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    speciality_type = models.SmallIntegerField(choices=SpecialityTypeChoices.choices)
    title = models.CharField(max_length=255)
    innovation_idea = models.TextField()


class SpellingMistake(Base):
    mistake = models.CharField(max_length=150)
    description = models.CharField(max_length=150, blank=True, null=True)
    fixed = models.BooleanField(default=False)
    page_url = models.URLField()


class FileStore(Base):
    file = models.ImageField(upload_to='filestore/')

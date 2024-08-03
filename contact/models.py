from django.db import models

from mininnovation_backend.models import Base


class Contact(Base):
    address = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    bus = models.CharField(max_length=150, null=True, blank=True)
    mini_bus = models.CharField(max_length=150, null=True, blank=True)
    subway = models.CharField(max_length=150, null=True, blank=True)
    reference_point = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    fax = models.CharField(max_length=30, null=True, blank=True)
    office = models.CharField(max_length=30, null=True, blank=True)
    photo = models.ImageField(upload_to='contact_photo/', null=True, blank=True)
    monday = models.CharField(max_length=20, null=True, blank=True)
    tuesday = models.CharField(max_length=20, null=True, blank=True)
    wednesday = models.CharField(max_length=20, null=True, blank=True)
    thursday = models.CharField(max_length=20, null=True, blank=True)
    friday = models.CharField(max_length=20, null=True, blank=True)
    saturday = models.CharField(max_length=20, null=True, blank=True)
    sunday = models.CharField(max_length=20, null=True, blank=True)
    work_week = models.CharField(max_length=20, null=True, blank=True)
    lunch = models.CharField(max_length=20, null=True, blank=True)
    telegram_link = models.URLField(null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)

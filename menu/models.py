from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from autoslug import AutoSlugField

from mininnovation_backend.models import Base


class Menu(MPTTModel, Base):
    def get_populate(self):
        return self.title_uz

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=get_populate, always_update=True, max_length=255, unique=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')
    group = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    is_static = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    has_category = models.BooleanField(default=False)
    url = models.URLField(null=True, blank=True)
    position = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return str(self.title)


class MenuAttachment(Base):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='menu_attachments/')
    title = models.CharField(max_length=150, blank=True, null=True)


class MenuImage(Base):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='images')
    file = models.ImageField(upload_to='menu_images/')
    is_active = models.BooleanField(default=False)
    order = models.SmallIntegerField(default=1)

    class Meta:
        ordering = ['order', '-created_at']

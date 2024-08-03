from autoslug import AutoSlugField
from django.db import models

from common.static_data import ContestTypeChoices
from menu.models import Menu
from mininnovation_backend.models import Base
from structure.models import Organization, InnovationTerritory


class Post(Base):
    def get_populate(self):
        return self.title_uz

    title = models.CharField(max_length=500)
    slug = AutoSlugField(populate_from=get_populate, editable=True, max_length=500, unique=True, null=True)
    content = models.TextField()
    url = models.CharField(max_length=255, blank=True, null=True)
    short_content = models.TextField(null=True, blank=True)
    menu = models.ManyToManyField(Menu, related_name='posts', blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, related_name='posts', blank=True,
                                     null=True)
    innovation_territory = models.ForeignKey(InnovationTerritory, on_delete=models.SET_NULL, related_name='posts',
                                             blank=True, null=True)
    contest_type = models.SmallIntegerField(choices=ContestTypeChoices.choices, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    position = models.PositiveSmallIntegerField(default=1)
    views = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    on_slider = models.BooleanField(default=False)
    contest_tour = models.CharField(max_length=20, blank=True, null=True)
    contest_end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-pub_date', 'position']


class PostAttachment(Base):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='post_attachments/')
    title = models.CharField(max_length=150, blank=True, null=True)


class PostImage(Base):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    file = models.ImageField(upload_to='post_images/')
    is_active = models.BooleanField(default=False)
    order = models.SmallIntegerField(default=1)

    class Meta:
        ordering = ['order', '-created_at']


class Tag(Base):
    def get_populate(self):
        return self.title_uz

    title = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from=get_populate, always_update=True, max_length=150, unique=True, null=True)

    def __str__(self):
        return str(self.title)


class ContestButton(Base):
    title = models.CharField(max_length=255, blank=True)
    url = models.URLField()
    position = models.SmallIntegerField(default=1)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['position', '-created_at']

import uuid

from django.db import models
from django.core.validators import FileExtensionValidator

from common.utils import FrameCreator
from mininnovation_backend.models import Base
from autoslug import AutoSlugField


class PhotoGallery(Base):
    def get_populate(self):
        return self.title_uz

    title = models.CharField(max_length=255)
    photos = models.ManyToManyField('PhotoGalleryAttachment', blank=True)
    slug = AutoSlugField(populate_from=get_populate, always_update=True, unique=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)


class PhotoGalleryAttachment(Base):
    def get_populate(self):
        return

    photo = models.ImageField(upload_to='photo_gallery/', blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    position = models.PositiveIntegerField(default=1)
    slug = AutoSlugField(populate_from=get_populate, always_update=True, unique=True, null=True)
    is_active = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        id = uuid.uuid1()
        self.slug = id.hex
        return super().save()


class VideoGallery(Base):
    def get_populate(self):
        return self.title_uz

    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='video_gallery/', blank=True, null=True)
    videos = models.ManyToManyField('VideoGalleryAttachment', blank=True)
    urls = models.ManyToManyField('VideoGalleryUrl', blank=True)
    slug = AutoSlugField(populate_from=get_populate, always_update=True, unique=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)


class VideoGalleryAttachment(Base):
    def get_populate(self):
        return

    video = models.FileField(upload_to='video_gallery/', blank=True,
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['mov', 'avi', 'mp4', 'webm', 'mkv', 'm4a'])]
                             )
    frame_of_video = models.ImageField(upload_to='video_frames/', blank=True)
    views = models.PositiveIntegerField(default=0)
    position = models.PositiveIntegerField(default=1)
    slug = AutoSlugField(populate_from=get_populate, always_update=True, unique=True, null=True)
    is_active = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        id = uuid.uuid1()
        self.slug = id.hex

        frame_creator = FrameCreator(video_field=self.video)
        self.frame_of_video = frame_creator.get_frame(video_frame_time='00:00:15')
        return super(VideoGalleryAttachment, self).save()


class VideoGalleryUrl(Base):
    poster = models.ImageField(upload_to='video_gallery/', blank=True)
    url = models.URLField(max_length=255, blank=True)

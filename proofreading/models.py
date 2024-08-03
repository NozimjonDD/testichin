from django.db import models

from common.static_data import LanguageChoices
from mininnovation_backend.models import Base


class Proofreading(Base):
    author_full_name = models.CharField(max_length=255)
    author_phone = models.CharField(max_length=20)
    author_workplace = models.CharField(max_length=255, blank=True, null=True)
    author_email = models.EmailField(blank=True, null=True)
    language = models.SmallIntegerField(choices=LanguageChoices.choices, blank=True, null=True)
    article_name = models.CharField(max_length=255)
    journal_name = models.CharField(max_length=255, blank=True, null=True)
    author_comment = models.TextField()
    file = models.FileField(upload_to='proofreading_attachments/')
    other_files = models.FileField(upload_to='proofreading_other_attachments', blank=True, null=True)

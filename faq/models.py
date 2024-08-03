from django.db import models

from mininnovation_backend.models import Base


class FaqTheme(Base):
    title = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['order']


class Faq(Base):
    question = models.TextField()
    answer = models.TextField()
    theme = models.ForeignKey(FaqTheme, related_name='faqs', on_delete=models.PROTECT)
    order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.question)

    class Meta:
        ordering = ['order']

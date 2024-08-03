from django.db import models

from mininnovation_backend.models import Base


class Survey(Base):
    question = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.question)


class SurveyVariant(Base):
    id = models.CharField(max_length=150, unique=True, primary_key=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='variants')
    text = models.CharField(max_length=150)

    def __str__(self):
        return str(self.text)


class SurveyResult(Base):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='results')
    survey_variant = models.ForeignKey(SurveyVariant, on_delete=models.CASCADE, related_name='results')

from django.db import models

from common.static_data import FeedbackStatusChoices
from mininnovation_backend.models import Base
from structure.models import Management, Department


class Feedback(Base):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField(max_length=1200)
    management = models.ForeignKey(Management, related_name='feedbacks', on_delete=models.SET_NULL, blank=True,
                                   null=True)
    department = models.ForeignKey(Department, related_name='feedbacks', on_delete=models.SET_NULL, blank=True,
                                   null=True)
    status = models.PositiveSmallIntegerField(choices=FeedbackStatusChoices.choices, default=FeedbackStatusChoices.NEW)

    class Meta:
        ordering = ['-created_at']

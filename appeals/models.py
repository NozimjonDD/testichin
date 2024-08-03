from uuid import uuid4
from django.db import models

from common.models import Region, District
from common.static_data import AppealStatusChoices, AppealTypeChoices, AppealStatusTypeChoices, SummaryPersonChoices
from common.validators import file_type_validators, file_type_extra_validators, FileSizeValidators, \
    FileSizeExtraValidators
from structure.models import Staff
from user.models import User, Base, validate_phone


def short_uuid4():
    return uuid4().hex[:8]


class Appeal(Base):
    """Murojaatlar uchun model"""
    full_name = models.CharField(max_length=128)
    applicant = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='appeals')
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, related_name='appeals')
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, related_name='appeals')
    address = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=12, validators=[validate_phone])
    passport = models.CharField(max_length=9, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # applicant_status = models.SmallIntegerField(choices=ApplicantStatusChoices.choices)
    status = models.SmallIntegerField(choices=AppealStatusChoices.choices, default=AppealStatusChoices.ACCEPTED)
    appeal_type = models.SmallIntegerField(choices=AppealTypeChoices.choices)
    # whom = models.ForeignKey(Deputy, related_name='appeals', on_delete=models.DO_NOTHING, blank=True)
    content = models.TextField()
    key = models.CharField(max_length=32, default=short_uuid4, unique=True, editable=False)
    is_key_sent = models.BooleanField(default=False)
    error = models.TextField(editable=False, null=True, blank=True)

    def __str__(self):
        return self.content


class AppealResponse(Base):
    """Murojaatlar javoblari/natijalari uchun model"""
    appeal = models.ForeignKey(Appeal, on_delete=models.DO_NOTHING, related_name='responses')
    title = models.CharField(max_length=128, null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return str(self.title)


class AppealAttachment(Base):
    """Murojaat fayillari uchun model"""
    appeal = models.ForeignKey(Appeal, on_delete=models.DO_NOTHING, related_name='attachments')
    file = models.FileField(upload_to='appeal_attachments/')


class AppealResponseAttachment(Base):
    """Murojaat javoblari fayillari uchun model"""
    appeal_response = models.ForeignKey(AppealResponse, on_delete=models.DO_NOTHING, related_name='attachments')
    file = models.FileField(upload_to='appeal_attachments/response_attachments/')


class AppealStatus(Base):
    """Murojaat holati uchun"""
    appeal_id = models.IntegerField(unique=True, blank=True, null=True)
    appeal_full_name = models.CharField(max_length=100)
    content = models.TextField()
    status = models.SmallIntegerField(choices=AppealStatusChoices.choices)
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, related_name='appeals_status')
    # performer_full_name = models.CharField(max_length=100)
    # performer_phone = models.CharField(max_length=20)
    # performer_email = models.EmailField()
    appeal_received_date = models.DateTimeField()


class VirtualReception(Base):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, related_name='virtual_receptions')
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, related_name='virtual_receptions')
    message = models.TextField()


class AppealStatics(Base):
    title = models.CharField(max_length=255)
    appeal_type = models.SmallIntegerField(choices=AppealStatusTypeChoices.choices, unique=True, error_messages={
        'unique': "A type with that appeal type already exists."})
    accepted = models.PositiveIntegerField(blank=True, null=True)
    considering = models.PositiveIntegerField(blank=True, null=True)
    closed = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Appeal statics"
        verbose_name_plural = "Appeal statics"


class Summary(Base):
    """
    Xulosalarni berish bo'yicha onlayn arizalarni qabul qilish platformasi uchun
    """
    person_type = models.SmallIntegerField(choices=SummaryPersonChoices.choices)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    organization_file = models.FileField(upload_to='summary/organization_file', null=True, blank=True,
                                         validators=[file_type_validators, FileSizeValidators]
                                         )
    international_file_zip = models.FileField(upload_to='summary/documents_zip_file', null=True, blank=True,
                                              validators=[file_type_extra_validators, FileSizeExtraValidators]
                                              )
    first_number_file = models.FileField(upload_to='summary/first_document_file', null=True, blank=True,
                                         validators=[file_type_validators, FileSizeValidators]
                                         )

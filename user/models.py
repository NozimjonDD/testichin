import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

from common.static_data import UserRoleChoices, UserGenderChoices
from common.validators import validate_phone
from mininnovation_backend.models import Base
from django.utils.translation import gettext_lazy as _
from common.models import District


class User(AbstractUser, Base):
    """ Model for authorization """

    username = models.CharField(max_length=255, unique=True, error_messages={
        'unique': _("A user with that username already exists.")}, )
    address = models.TextField(blank=True, null=True)
    profession = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=30, choices=UserRoleChoices.choices, default=UserRoleChoices.USER)
    district = models.ForeignKey(District, on_delete=models.PROTECT, null=True, blank=True)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    phone = models.CharField(max_length=20, unique=True, error_messages={
        'unique': _('User with that phone already exists')
    }, null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=UserGenderChoices.choices, default=UserGenderChoices.MALE)
    birth_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']  # don't require email

    def __str__(self):
        return self.get_username()

    @property
    def full_name(self):
        return self.get_full_name()

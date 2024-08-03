from autoslug import AutoSlugField
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

from common.static_data import ManagementTypeChoices, DepartmentTypeChoices
from common.models import Region, District
from mininnovation_backend.models import Base


class Staff(Base):
    def get_populate(self):
        return self.full_name_uz

    full_name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from=get_populate, always_update=True, max_length=150, unique=True)
    biography = models.TextField(blank=True, null=True)
    obligation = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='staff_images/', blank=True, null=True)
    thumb = ImageSpecField(source='photo',
                           processors=[Thumbnail(300, 300, crop=False)],
                           format='JPEG',
                           options={'quality': 90})
    reception_days = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=40, blank=True, null=True)
    inner_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_vacant = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.full_name)


class Management(Base):
    def get_populate(self):
        return self.title_uz

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=get_populate, always_update=True, max_length=255, unique=True)
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    type = models.SmallIntegerField(choices=ManagementTypeChoices.choices)
    order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.staff.full_name)

    class Meta:
        ordering = ['order', 'type']


class Department(Base):
    def get_populate(self):
        return self.title_uz

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=get_populate, always_update=True, max_length=255, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    region = models.OneToOneField(Region, on_delete=models.SET_NULL, blank=True, null=True)
    boss = models.OneToOneField(Staff, on_delete=models.SET_NULL, blank=True, null=True)
    staffs = models.ManyToManyField(Staff, through='DepartmentStaffsWithOrder', related_name='departments', blank=True)
    order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['order']


class DepartmentStaffsWithOrder(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(default=1)


class Division(Base):
    def get_populate(self):
        return self.title_uz

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=get_populate, always_update=True, max_length=255, unique=True)
    department = models.ForeignKey(Department, related_name='divisions', on_delete=models.SET_NULL, blank=True,
                                   null=True)
    boss = models.OneToOneField(Staff, on_delete=models.SET_NULL, blank=True, null=True)
    staffs = models.ManyToManyField(Staff, through='DivisionStaffsWithOrder', related_name='divisions', blank=True)
    order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['order']


class DivisionStaffsWithOrder(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(default=1)


class Organization(Base):
    def get_populate(self):
        return self.title_uz

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=get_populate, always_update=True, max_length=255, unique=True)
    photo = models.ImageField(upload_to='organizations_photos/')
    thumb = ImageSpecField(source='photo',
                           processors=[Thumbnail(300, 300, crop=False)],
                           format='JPEG',
                           options={'quality': 100})
    boss = models.ForeignKey(Staff, related_name='organization_boss', on_delete=models.SET_NULL, blank=True,
                             null=True)
    staffs = models.ManyToManyField(Staff, blank=True)
    web = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=40, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    about = models.TextField()
    order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']


class InnovationCenter(Base):
    def get_populate(self):
        return self.title_uz

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=get_populate, always_update=True, max_length=255, unique=True)
    boss = models.OneToOneField(Staff, related_name='innovation_center_boss', on_delete=models.SET_NULL, blank=True,
                                null=True)
    region = models.ForeignKey(Region, related_name='innovation_centers', on_delete=models.PROTECT)
    district = models.ForeignKey(District, related_name='innovation_centers', on_delete=models.PROTECT)
    address = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']


class InnovationTerritory(Base):
    def get_populate(self):
        return self.title_uz

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=get_populate, always_update=True, max_length=255, unique=True)
    content = models.TextField()
    year = models.CharField(max_length=20, blank=True, null=True)
    region = models.ForeignKey(Region, related_name='innovation_territory', on_delete=models.PROTECT)
    district = models.ForeignKey(District, related_name='innovation_territory', on_delete=models.PROTECT)
    address = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='innovationterritory_images/', blank=True, null=True)
    thumb = ImageSpecField(source='photo',
                           processors=[Thumbnail(300, 300, crop=False)],
                           format='JPEG',
                           options={'quality': 100})
    population = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    created_workplace = models.CharField(max_length=255, blank=True, )
    innovation_projects = models.CharField(max_length=255, blank=True, null=True)
    technology_transfer = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=False)


class MininstryCouncil(Base):
    """
    Uz
    Vazirlik hay'ati uchun model

    Ru
    Модель для совета министерства
    """
    content = models.TextField()
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Ministry Council'

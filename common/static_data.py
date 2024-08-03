from django.db import models


class UserGenderChoices(models.IntegerChoices):
    MALE = 1, 'Male',
    FEMALE = 2, 'Female',


class UserRoleChoices(models.TextChoices):
    """
    Moderator2 faqat sitedan murojaat qilayotganlar uchun
    Moderator3 faqat postlar uchun Create Update Delete List
    """
    ADMIN = 'Admin', 'Admin'
    MODERATOR = 'Moderator', 'Moderator'
    MODERATOR2 = 'Moderator2', 'Moderator2'
    MODERATOR3 = 'Moderator3', 'Moderator3'
    USER = 'User', 'User'


class AppealStatusChoices(models.IntegerChoices):
    ACCEPTED = 1, 'Accepted',
    CONSIDERING = 2, 'Considering',
    CLOSED = 3, 'Closed',


class ApplicantStatusChoices(models.IntegerChoices):
    EMPLOYED = 1, 'Employed',
    UNEMPLOYED = 2, 'Unemployed',
    PENSIONER = 3, 'Pensioner',
    STUDENT = 4, 'Student',


class CommentStatusChoices(models.IntegerChoices):
    PENDING = 1, 'Pending',
    APPROVED = 2, 'Approved',
    BLOCKED = 3, 'Blocked',


class DepartmentTypeChoices(models.IntegerChoices):
    SIMPLE = 1, 'Simple department',
    REGIONAL = 2, 'Region department',


class ManagementTypeChoices(models.IntegerChoices):
    MINISTER = 1, 'Director',
    DEPUTY_MINISTER = 2, 'Deputy minister',
    ASSISTANT = 3, 'Assistant of the minister',
    ADVISOR = 4, 'Advisor of the minister',
    INTERNATIONAL_ADVISOR = 5, 'International advisor of the minister',
    SCIENTIFIC_SECRETARY = 6, 'Scientific secretary',


class AppealTypeChoices(models.IntegerChoices):
    TO_CHAIRMAN_OF_LEGISLATIVE_CHAMBER = 1, 'To chairman of the Legislative Chamber',
    TO_SPEAKER_OF_LEGISLATIVE_CHAMBER = 2, 'To speaker of the Legislative Chamber',
    TO_SUB_SPEAKER_OF_LEGISLATIVE_CHAMBER = 3, 'To sub-speaker of the Legislative Chamber',
    TO_CHAIRMAN_OF_FRACTION = 4, 'To chairman of the fraction',
    TO_CHAIRMAN_OF_COMMISSION = 5, 'To chairman of the commission',


class AppealStatusTypeChoices(models.IntegerChoices):
    VIRTUAL_RECEPTION = 1, 'Virtual reception',
    WEB_SITE = 2, 'Web site',
    BY_PHONE = 3, 'By phone',
    BY_WRITING = 4, 'By writing',
    BY_EMAIL = 5, 'By email',


class ServiceTypeChoices(models.IntegerChoices):
    INTERACTIVE_SERVICE = 1, 'Interactive service',
    USEFUL_LINK = 2, 'Useful link'
    DIGITALIZATION = 3, 'Digitalization'
    INFO = 4, 'Info'


class FeedbackStatusChoices(models.IntegerChoices):
    NEW = 1, 'New feedback',
    ANSWERED = 2, 'Answered'


class EventLevelChoices(models.IntegerChoices):
    INTERNATIONAL = 1, 'International',
    REGIONAL = 2, 'Regional'


class EventMediaPlanChoices(models.IntegerChoices):
    EVENT = 1, 'Event',
    MEDIA_PLAN = 2, 'Media_plan',


class SpecialityTypeChoices(models.IntegerChoices):
    INFORMATION_TECHNOLOGY = 1, 'Information Technology',
    AGRICULTURE = 2, 'Agriculture',
    HEALTHCARE = 3, 'Healthcare',
    SCIENCE = 4, 'Science',
    BUSINESS = 5, 'Business',
    POLITICS = 6, 'Politics',
    ECONOMICS = 7, 'Economics',
    ECOLOGY = 8, 'Ecology',
    TOURISM = 9, 'Tourism',


class LanguageChoices(models.IntegerChoices):
    BRITISH = 1, 'British',
    AMERICAN = 2, 'American',


class SummaryPersonChoices(models.IntegerChoices):
    PHYSICAL = 1, 'Physical',
    LEGAL = 2, 'Legal',


class ContestTypeChoices(models.IntegerChoices):
    PRACTICAL = 1, 'Practical',
    FUNDAMENTAL = 2, 'Fundamental',
    INNOVATION = 3, 'Innovation',
    STARTUP = 4, 'Startup',
    COOPERATION = 5, 'Cooperation',
    PRACTICAL_INNOVATION = 6, 'Practical innovation',

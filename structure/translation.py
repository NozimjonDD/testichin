from modeltranslation.translator import translator, TranslationOptions

from . import models


class StaffTranslationOptions(TranslationOptions):
    fields = (
        'full_name',
        'biography',
        'obligation',
        'position',
        'reception_days',
    )


class ManagementTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


class DepartmentTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'address',
    )


class DivisionTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


class OrganizationTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'address',
        'about',
    )


class InnovationCenterTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'address',
    )


class InnovationTerritoryTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'content',
        'address',
    )


class MininstryCouncilTranslationOptions(TranslationOptions):
    fields = (
        'content',
    )


translator.register(models.Staff, StaffTranslationOptions)
translator.register(models.Management, ManagementTranslationOptions)
translator.register(models.Department, DepartmentTranslationOptions)
translator.register(models.Division, DivisionTranslationOptions)
translator.register(models.Organization, OrganizationTranslationOptions)
translator.register(models.InnovationCenter, InnovationCenterTranslationOptions)
translator.register(models.InnovationTerritory, InnovationTerritoryTranslationOptions)
translator.register(models.MininstryCouncil, MininstryCouncilTranslationOptions)

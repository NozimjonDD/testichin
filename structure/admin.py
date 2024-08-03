from django.contrib import admin
from . import models

@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'full_name',
        'slug',
        'photo',
        'thumb',
        'phone_number',
        'inner_number',
        'inner_number',
        'email',
        'is_active',
    ]
    list_display_links = (
        'full_name',
        'slug',
    )


@admin.register(models.Management)
class ManagementAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'slug',
        'staff',
        'type',
        'order',
        'is_active',
    ]
    list_display_links = [
        'title',
        'slug',
    ]


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'slug',
        'address',
        'region',
        'boss',
        'staffs',
        'is_active',
    ]
    list_display_links = (
        'title',
        'slug',
    )


@admin.register(models.Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'slug',
        'department',
        'boss',
        'is_active',
    ]
    list_display_links = (
        'title',
        'slug',
    )


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'slug',
        'photo',
        'thumb',
        'boss',
        'web',
        'address',
        'is_active',
    ]
    list_display_links = (
        'title',
        'slug',
    )


@admin.register(models.InnovationTerritory)
class InnovationTerritoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'slug',
        'content',
        'region',
        'district',
        'address',
        'photo',
        'population',
        'area',
        'created_workplace',
        'innovation_projects',
        'technology_transfer',
        'order',
        'is_active',
    ]
    list_display_links = [
        'title',
        'slug',
    ]


@admin.register(models.MininstryCouncil)
class MininstryCouncilTerritoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'content',
        'is_active',
    ]



@admin.register(models.DepartmentStaffsWithOrder)
class DepartmentStaffsWithOrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
    ]





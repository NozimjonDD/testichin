from django.contrib import admin
from appeals import models
from appeals.models import AppealStatics


class AppealAttachmentInline(admin.StackedInline):
    model = models.AppealAttachment


class AppealResponseAttachmentInline(admin.StackedInline):
    model = models.AppealResponseAttachment


@admin.register(models.Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'applicant',
        # 'full_name',
        'region',
        'district',
        # 'address',
        # 'email',
        # 'phone_number',
        # 'passport',
        # 'birth_date',
        # 'applicant_status',
        'status',
        # 'whom',
        'content',
        'key',
        'is_key_sent',
    )
    inlines = (AppealAttachmentInline,)


@admin.register(models.AppealResponse)
class AppealResponseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'appeal',
        'title',
        'content',
    )
    inlines = (AppealResponseAttachmentInline,)


@admin.register(models.AppealStatus)
class AppealStatusAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'appeal_id',
        'appeal_full_name',
        # 'appeal_type',
        'content',
        'status',
        'staff',
        # 'performer_full_name',
        # 'performer_phone',
        # 'performer_email',
        'appeal_received_date',
    )
    list_display_links = (
        'id',
        'appeal_id',
        'appeal_full_name',
    )


@admin.register(models.VirtualReception)
class VirtualReceptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'phone_number',
        'email',
        'region',
        'district',
        'message',
    )
    list_display_links = (
        'id',
        'full_name',
    )


@admin.register(models.AppealStatics)
class VirtualReceptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'appeal_type',
        'accepted',
        'considering',
        'closed',
        'total',
    )
    list_display_links = (
        'id',
        'title',
    )

    def total(self, obj: AppealStatics):
        sum = 0
        if obj.accepted:
            sum += obj.accepted
        if obj.closed:
            sum += obj.closed
        if obj.considering:
            sum += obj.considering
        return sum


@admin.register(models.Summary)
class SummaryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'person_type',
        'full_name',
        'phone',
        'organization_name',
        'email',
        'organization_file',
        'international_file_zip',
        'first_number_file',
    ]
    list_display_links = [
        'id',
        'person_type',
        'full_name',
    ]

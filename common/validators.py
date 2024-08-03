from django.core.validators import RegexValidator, FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

validate_phone = RegexValidator(
    regex=r"^998\d{9}$",
    message="Phone number must begin with 998 and contain only 12 numbers",
)
file_type_validators = FileExtensionValidator(
    allowed_extensions=['pdf'],
    message=_(
        'File extension “%(extension)s” is not allowed. '
        'Allowed extensions are: %(allowed_extensions)s.'
    )
)
file_type_extra_validators = FileExtensionValidator(
    allowed_extensions=['zip', 'rar'],
    message=_(
        'File extension “%(extension)s” is not allowed. '
        'Allowed extensions are: %(allowed_extensions)s.'
    )
)


def FileSizeValidators(value):
    file_size = value.size
    limit_size = 5 * 1024 * 1024
    if file_size > limit_size:
        raise ValidationError("The maximum file size that can be uploaded is 5 MB")


def FileSizeExtraValidators(value):
    file_size = value.size
    limit_size = 20 * 1024 * 1024
    if file_size > limit_size:
        raise ValidationError("The maximum file size that can be uploaded is 20 MB")

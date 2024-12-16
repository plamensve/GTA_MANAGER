import re

from django.core.exceptions import ValidationError
from pip._internal.utils._jaraco_text import _


def email_validator(value):
    """
    Custom email validator to ensure the email format is valid.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, value):
        raise ValidationError(
            _('Invalid email address: %(value)s'),
            params={'value': value},
        )
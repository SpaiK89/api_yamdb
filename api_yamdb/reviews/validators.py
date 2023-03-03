import datetime as dt

from django.core.exceptions import ValidationError


def year_validator(value):
    year = dt.datetime.now().year
    if year < value:
        raise ValidationError(f'{value} - некорректный год издания'
                              f'произведения! Укажите год не более {year}')
    return value

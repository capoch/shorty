from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(value):
    url_validator = URLValidator()
    invalid1 = False
    invalid2 = False
    try:
        url_validator(value)
    except:
        invalid1 = True
    new_value = "http://" + value
    try:
        url_validator(new_value)
    except:
        invalid2 = True
    if invalid1 == False and invalid2 == False:
        raise ValidationError("Fuck off more")
    return value

def validate_dot_com(value):
    if not "com" in value:
        raise ValidationError("no .com biatch")
    return value

import os
import uuid
import base62
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

ENV = os.environ.get('ENV', 'DEV')
PREFIX = os.environ.get('PREFIX', 'shorty-link.onrender.com')  # default por si acaso

def generate_short_code():
    random_uuid = uuid.uuid4().int
    return base62.encode(random_uuid)[:7]

def build_short_url(code):
    return f'https://{PREFIX}/{code}'

def validate_url(url):
    validate = URLValidator()
    try:
        validate(url)
        return True
    except ValidationError:
        return False

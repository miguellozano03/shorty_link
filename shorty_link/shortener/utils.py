from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

import base62
import uuid

def generate_short_code():
    random_uiid = uuid.uuid4().int
    shorten_url = base62.encode(random_uiid)
    return shorten_url[:7]

def build_short_url(code, prefix: str = 'localhost:8000'):
    return f'http://{prefix}/{code}'

def valitate_url(url):
    validate = URLValidator()
    try:
        validate(url)
        return True
    except ValidationError:
        return False
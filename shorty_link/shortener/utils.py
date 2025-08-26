import base62
import uuid

def generate_short_code():
    random_uiid = uuid.uuid4().int

    shorten_url = base62.encode(random_uiid)

    return shorten_url[:7]

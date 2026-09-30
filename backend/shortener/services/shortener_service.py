from django.db import IntegrityError, transaction
from shortener.models import Url
from shortener.utils import generate_short_code


class ShortenerService:

    def get(self, code, user):
        """Return the URL owned by the user for the given short code.

        Intended for authenticated actions such as editing or deleting a URL.
        """
        return Url.objects.get(
            code=code,
            user_id=user.id,
        )

    def get_all(self, user):
        """Return all URLs owned by the user."""
        return Url.objects.filter(
            user_id=user.id,
        )

    def resolve(self, code):
        """Resolve a public short code to its original URL.

        Intended for redirect flows or public access.
        """
        return Url.objects.get(code=code)

    def create(self, long_url: str, user=None, *, title=None):
        """Create a new shortened URL."""
        for _ in range(5):
            code = generate_short_code()

            try:
                with transaction.atomic():
                    return Url.objects.create(
                        title=title,
                        long_url=long_url,
                        code=code,
                        user=user,
                    )

            except IntegrityError:
                continue

        raise RuntimeError("Could not generate a unique short code")

    def edit(self, code, user, *, title=None, long_url=None):
        """Update the URL data for the given code and user."""
        url = self.get(code, user)

        if title is not None:
            url.title = title

        if long_url is not None:
            url.long_url = long_url

        url.save(update_fields=["title", "long_url"])

        return url

    def delete(self, code, user):
        """Delete the URL for the given code and user."""
        url = self.get(code, user)
        url.delete()
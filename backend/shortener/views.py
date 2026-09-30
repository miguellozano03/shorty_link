import json

from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect

from .utils import build_short_url, valitate_url
from .services.shortener_service import ShortenerService
from .models import Url


service = ShortenerService()


def home_view(request):
    return render(request, "shortener/home.html")


def generate_short(request):
    if request.method != "POST":
        return JsonResponse( {"error": "Method not allowed"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse( {"error": "Invalid JSON"}, status=400)

    long_url = data.get("url")

    if not long_url:
        return JsonResponse({"error": "No URL provided"},status=400,)

    if not valitate_url(long_url):
        return JsonResponse({"error": "The URL is invalid"},status=400,)

    url = service.create(long_url=long_url)

    return JsonResponse({
        "short_url": build_short_url(url.code),
    })


def redirect_url(request, code):
    try:
        url = service.resolve(code)
    except Url.DoesNotExist:
        raise Http404("Short URL not found")

    return redirect(url.long_url)
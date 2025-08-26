from django.http import JsonResponse
from django.shortcuts import render
from .utils import generate_short_code

# Create your views here.

def url_shortener_view(request):
    code = generate_short_code()
    return JsonResponse({"short_url": f"http:/shorty.link/{code}"})


def home_view(request):
    return render(request, "shortener/home.html")
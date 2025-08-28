from .models import Url
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from .utils import build_short_url,generate_short_code , valitate_url

def home_view(request):
    return render(request, "shortener/home.html")

def generate_short(request):
    if request.method == 'GET':
        long_url = request.GET.get('long_url')

        if not long_url:
            return JsonResponse({"error": "No URL provided"}, status=400)
    
        if not valitate_url(long_url):
            return JsonResponse({"error": "The URL is invalid"}, status=400)
        
        code = generate_short_code()
        while Url.objects.filter(short_url=code).exists():
            code = generate_short_code()

        Url.objects.create(long_url=long_url, short_url=code)
        return JsonResponse({"short_url": build_short_url(code)})
    return JsonResponse({"error": "Method not allowed"}, status=405)


def redirect_url(request, short_code):
    original = Url.objects.filter(short_url = short_code).first()
    if original:
        return redirect(original.long_url)
    raise Http404("Short URL not found")
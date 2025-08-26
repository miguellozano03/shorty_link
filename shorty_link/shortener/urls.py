from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('shorten/', views.url_shortener_view, name='shorten_link')
    
]

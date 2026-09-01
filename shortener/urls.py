from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('generate_short/', views.generate_short, name='shorten_link'),
    
    path('<str:short_code>/', views.redirect_url, name='redirect_url')
]

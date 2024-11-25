# lista/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('nomes/', views.nomes, name='nomes'),
]

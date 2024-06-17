from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Définir la vue 'home' pour la route racine
]

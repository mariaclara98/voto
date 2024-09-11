from django.urls import path
from .views import votar

urlpatterns = [
    path('votar/', votar, name='votar'),
]

from django.urls import path
from .views import candidatos

urlpatterns = [
    path('candidatos_por_lista/', candidatos, name = 'candidatos' )
]
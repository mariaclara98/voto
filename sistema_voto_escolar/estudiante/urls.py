from django.urls import path
from .views import inicio_login, exit

urlpatterns = [
    path('', inicio_login, name = 'inicio_login' ),
    path('logout/', exit ,name='exit'), 
]
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estudiante.urls')),
    path('', include('candidato.urls')),
    path('', include('lista.urls')),
    path('', include('resultado.urls')),
    path('', include('voto.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

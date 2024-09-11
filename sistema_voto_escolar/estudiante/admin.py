from django.contrib import admin
from estudiante.models import Estudiante, Curso

admin.site.register([Estudiante, Curso])

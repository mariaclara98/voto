from django.contrib import admin

from candidato.models import Dignidad, Candidato

admin.site.register([Dignidad, Candidato])

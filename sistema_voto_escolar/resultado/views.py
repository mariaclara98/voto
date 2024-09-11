from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lista.models import Lista
from django.db.models import Count

def resultados(request):
    listas = Lista.objects.all().annotate(num_votos=Count('voto'))

    context = {
        'listas': listas,
    }

    return render(request, 'resultado/resultado.html', context)


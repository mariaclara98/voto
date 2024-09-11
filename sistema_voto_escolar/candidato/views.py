from django.shortcuts import render

def candidatos(request):
    return render(request, 'candidato/candidato.html', {})
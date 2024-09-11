# views.py
from django.shortcuts import render, redirect
from .models import Voto
from .forms import VotoForm

def votar(request):
    if request.method == 'POST':
        form = VotoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio_login')
        else:
            return #render(request, 'lista.html')
    else:
        form = VotoForm()
    
    #return render(request, 'lista.html', {'form': form})

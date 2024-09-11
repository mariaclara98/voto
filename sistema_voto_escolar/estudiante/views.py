from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout   #control de sesiones
from voto.models import Voto

def inicio_login(request):

    if request.method == 'POST':

        user_cedula = request.POST['cedula']
        user_pass = request.POST['password']
        errors = 'Credenciales incorrectas !!'

        usuario = authenticate(username = user_cedula, password = user_pass)
        realizo_voto = Voto.objects.filter(estudiante__user_id = usuario.id).count()

        if usuario and realizo_voto == 0:
            login(request, usuario)   #crea la sesion para el usuario "usuario"
            return redirect('listas')
        else:
            messages.error(request, errors)
            return redirect('inicio_login')
        
    else:
        #print(request.GET)
        return render(request, 'estudiante/inicio_login.html', {})


def exit(request):
    logout(request)
    return redirect('inicio_login')
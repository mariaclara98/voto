from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from candidato.models import *
from estudiante.models import Estudiante
from voto.models import Voto

@login_required(login_url= '/')      #requiere login
def listas(request):
    id_user = request.user.id
    #print(id_user)
    context = {

        'listas': Lista.objects.all(),
        'estudiante': Estudiante.objects.get(user_id=id_user)
    }
    #print(context['estudiante'])
    if request.GET.get('id_est') and request.GET.get('id_list'):
        id_est, id_list = request.GET['id_est'], request.GET['id_list']
        #print('estudiante: ', id_est)
        #print('lista: ', id_list)
        voto = Voto(estudiante_id = id_est, lista_id = id_list)
        voto.save()
        return redirect('/')
    return render(request, 'lista/lista.html', context)

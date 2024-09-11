
from django.db import models
from lista.models import Lista
from estudiante.models import Estudiante



class Voto(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=False)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, null=True, blank=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.lista}, {self.fecha_hora}'


from django.db import models

from lista.models import Lista



class Resultado(models.Model):
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, null=True, blank=True)
    blanco = models.PositiveBigIntegerField(default=0)
    nulo = models.PositiveBigIntegerField(default=0)
    total = models.PositiveBigIntegerField(default=0)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        if (self.lista):
            return f'{self.lista}: {self.total}'
        
        return f'Blancos: {self.blanco}, Nulos: {self.nulo}'
from django.db import models
from estudiante.models import Estudiante
from lista.models import Lista

DIGNIDADES = (
    ('Presidente', 'presidente'),
    ('Vicepresidente', 'vicepresidente'),
    ('Secretario/a', 'secretario/a'),
    ('Tesorero/a', 'tesorero/a'),
    ('Vocal-1', 'vocal-1'),
    ('Vocal-2', 'vocal-2'),
)

class Dignidad(models.Model):
    dignidad = models.CharField(default='presidente', choices=DIGNIDADES, null=False, blank=False, max_length=30)
    def __str__(self) -> str:
        return f'{self.dignidad}'


class Candidato(models.Model):
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, related_name='candidatos', null=False, blank=False)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=False, blank=False)
    foto = models.ImageField(upload_to='listas')
    dignidad = models.ForeignKey(Dignidad, on_delete=models.CASCADE, null=False, blank=False)


    def __str__(self) -> str:
        return f'{self.lista.numero}, {self.dignidad}'

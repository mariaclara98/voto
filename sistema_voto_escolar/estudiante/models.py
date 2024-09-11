from django.db import models
from django.contrib.auth.models import User

CURSOS = (
    ('Primero', 1),
    ('Segundo', 2),
    ('Tercero', 3),
    ('Cuarto', 4),
    ('Quinto', 5),
    ('Sexto', 6),
    ('Séptimo', 7),
)

PARALELOS = (
    ('A', 'a'),
    ('B', 'b'),
    ('C', 'c'),
    ('D', 'd'),
)

class Curso(models.Model):
    nivel = models.CharField(default='1', choices=CURSOS, max_length=10)
    paralelo = models.CharField(max_length=1, default='a', choices=PARALELOS)

    def __str__(self) -> str:
        return f'{self.nivel}-{self.paralelo}'


class Estudiante(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}, {self.curso}'

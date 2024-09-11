from django.db import models

class Lista(models.Model):
    numero = models.CharField(max_length=5, unique=True)
    nombre = models.CharField(max_length=25, unique=True)
    propuesta = models.TextField(max_length=500, default='')
    foto = models.ImageField(upload_to='listas')
    
    def __str__(self) -> str:
        return f'{self.numero}, {self.nombre}'
    


 
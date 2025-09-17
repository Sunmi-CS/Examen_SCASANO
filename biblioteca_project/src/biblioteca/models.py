from django.db import models


class Libro(models.Model):
   
    titulo = models.CharField(max_length=200, verbose_name="Título")
    publicacion = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=200, verbose_name="Genero")
   
    def __str__(self):
        return self.titulo
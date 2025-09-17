from django.db import models

class Libro(models.Model):
    
    titulo = models.CharField(max_length=200, verbose_name="Título")
    ano_publicacion = models.TextField(blank=True, verbose_name="año_publicacion")
    genero = models.CharField(max_length=200, verbose_name="Genero")
    
    def __str__(self):
        return self.titulo

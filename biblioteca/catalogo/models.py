from django.db import models

# Create your models here.
from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=200, help_text="Ingrese un género de libro (ej: Ciencia Ficción)")

    def __str__(self):
        return self.nombre

# TODO: manager

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    resumen = models.TextField(max_length=1000, help_text="Ingrese un breve resumen del libro")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN</a>')
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

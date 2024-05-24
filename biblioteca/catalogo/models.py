from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=200, help_text="Ingrese un género de libro (ej: Ciencia Ficción)")

    def __str__(self):
        return self.nombre

class LibroManager(models.Manager):
    def validate_titulo(self, titulo):
        if not titulo.isalpha():
            raise ValidationError("El título solo debe contener letras.")

    def validate_autor(self, autor):
        if len(autor) < 2:
            raise ValidationError("El autor debe tener al menos 2 caracteres.")

    def validate_resumen(self, resumen):
        if len(resumen) < 10:
            raise ValidationError("El resumen debe tener al menos 10 caracteres.")

    def validate_isbn(self, isbn):
        if not isbn.isdigit() or len(isbn) not in [10, 13]:
            raise ValidationError("El ISBN debe tener 10 o 13 dígitos numéricos.")

    def create_libro(self, titulo, autor, resumen, isbn, genero):
        self.validate_titulo(titulo)
        self.validate_autor(autor)
        self.validate_resumen(resumen)
        self.validate_isbn(isbn)
        libro = self.create(titulo=titulo, autor=autor, resumen=resumen, isbn=isbn, genero=genero)
        return libro

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    resumen = models.TextField(max_length=1000, help_text="Ingrese un breve resumen del libro")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN</a>')
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)

    objects = LibroManager()

    def __str__(self):
        return self.titulo

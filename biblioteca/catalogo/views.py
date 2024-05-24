from django.views import View
from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ValidationError
from catalogo.models import Libro, Genero


class CatalogoView(View):
    def get(self, request):
        libros = Libro.objects.all().order_by('-id') 
        return render(request, 'catalogo.html', {'libros': libros})


class LibroFormView(View):
    def get(self, request):
        generos = Genero.objects.all()
        return render(request, 'libro_form.html', {'generos': generos})

    def post(self, request):
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        resumen = request.POST.get('resumen')
        isbn = request.POST.get('isbn')
        genero_id = request.POST.get('genero')
        genero = Genero.objects.get(id=genero_id)

        try:
            Libro.objects.create_libro(titulo, autor, resumen, isbn, genero)
            return redirect(reverse("catalogo"))
        except ValidationError as e:
            generos = Genero.objects.all()
            return render(request, 'libro_form.html', {
                'errors': e.messages,
                'titulo': titulo,
                'autor': autor,
                'resumen': resumen,
                'isbn': isbn,
                'genero_id': genero_id,
                'generos': generos
            })

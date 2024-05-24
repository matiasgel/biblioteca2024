from django.views.generic import View
from django.shortcuts import render, redirect
from catalogo.models import Libro, Genero
from .forms import LibroForm
from django.core.exceptions import ValidationError


class CatalogoView(View):
    def get(self, request):
        libros = Libro.objects.all().order_by('-id')
        return render(request, 'index.html', {'libros': libros})


class LibroFormView(View):
    def get(self, request):
        form = LibroForm()
        generos = Genero.objects.all()
        return render(request, 'libro_form.html', {'form': form, 'generos': generos})

    def post(self, request):
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo')
        else:
            generos = Genero.objects.all()
            return render(request, 'libro_form.html', {'form': form, 'generos': generos})
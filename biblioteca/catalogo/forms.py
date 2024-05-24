from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'resumen', 'isbn', 'genero']

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if len(titulo) < 2:
            raise forms.ValidationError("El título debe tener al menos 2 caracteres.")
        return titulo

    def clean_autor(self):
        autor = self.cleaned_data.get('autor')
        if len(autor) < 2:
            raise forms.ValidationError("El autor debe tener al menos 2 caracteres.")
        return autor

    def clean_resumen(self):
        resumen = self.cleaned_data.get('resumen')
        if len(resumen) < 10:
            raise forms.ValidationError("El resumen debe tener al menos 10 caracteres.")
        return resumen

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if not isbn.isdigit() or len(isbn) not in [10, 13]:
            raise forms.ValidationError("El ISBN debe tener 10 o 13 dígitos numéricos.")
        return isbn

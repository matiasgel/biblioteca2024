from django.views.generic import ListView
from catalogo.models import Libro


class CatalogoView(ListView):
    template_name = "index.html"
    model = Libro
    queryset = Libro.objects.all()
    context_object_name = 'libros'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

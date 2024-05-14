import os
import django
import requests
from django.utils.text import slugify

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')
django.setup()

from catalogo.models import Genero, Libro

# Lista de géneros a crear
nombres_generos = [
    "Python", "Machine Learning", "Data Science", "Artificial Intelligence",
    "Deep Learning", "Computer Vision", "Natural Language Processing",
    "Big Data", "Algorithms", "Statistics"
]

# Crear géneros
generos = []
for nombre in nombres_generos:
    genero, created = Genero.objects.get_or_create(nombre=nombre)
    generos.append(genero)

# Función para obtener libros de Google Books
def obtener_libros(query, max_results=40):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        print(f"Error al obtener libros para la consulta '{query}': {response.status_code}")
        return []

# Función para cargar libros en la base de datos
def cargar_libros(genero, query):
    libros = obtener_libros(query)
    for libro in libros:
        info = libro['volumeInfo']
        titulo = info.get('title', 'Título desconocido')
        autores = ", ".join(info.get('authors', ['Autor desconocido']))
        isbn_list = [identifier['identifier'] for identifier in info.get('industryIdentifiers', []) if identifier['type'] == 'ISBN_13']
        isbn = isbn_list[0] if isbn_list else 'N/A'
        resumen = info.get('description', f"Libro sobre {query}")

        libro_obj = Libro.objects.create(
            titulo=titulo,
            autor=autores,
            resumen=resumen,
            isbn=isbn,
            genero=genero
        )

        print(f"Libro '{titulo}' creado.")

# Cargar al menos 1000 libros distribuidos en los 10 géneros
libros_por_genero = 100
for genero in generos:
    cargar_libros(genero, genero.nombre)

print("Carga de libros completada.")

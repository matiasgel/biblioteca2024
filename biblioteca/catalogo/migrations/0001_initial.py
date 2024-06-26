# Generated by Django 4.1 on 2024-05-14 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genero",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        help_text="Ingrese un género de libro (ej: Ciencia Ficción)",
                        max_length=200,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Libro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=200)),
                ("autor", models.CharField(max_length=200)),
                (
                    "resumen",
                    models.TextField(
                        help_text="Ingrese un breve resumen del libro", max_length=1000
                    ),
                ),
                (
                    "isbn",
                    models.CharField(
                        help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN</a>',
                        max_length=13,
                        verbose_name="ISBN",
                    ),
                ),
                (
                    "genero",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalogo.genero",
                    ),
                ),
            ],
        ),
    ]

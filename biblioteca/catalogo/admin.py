from django.contrib import admin
from django import forms
from django.contrib.auth.models import Permission
from catalogo.models import Libro, Genero


admin.site.register(Permission)

def marcar_como_publicado(modeladmin, request, queryset):
    queryset.update(publicado=True)
marcar_como_publicado.short_description = "Marcar libros seleccionados como publicados"

class GeneroAdmin(admin.TabularInline):
    model = Genero
    extra = 1 


class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'resumen', 'isbn', 'genero', 'publicado')
    list_filter = ('titulo', 'autor')
    search_fields = ('titulo', 'autor')
    actions = [marcar_como_publicado]

    fieldsets = (
        (None, {
            'fields': ('titulo', 'autor', 'genero')
        }),
        ('Otros campos', {
            'classes': ('collapse',),
            'fields': ('resumen', 'isbn'),
        }),
    )

class LibroInline(admin.StackedInline):
    model = Libro
    extra = 2  # Mostrar dos formularios adicionales para nuevos objetos

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    inlines = [LibroInline]

admin.site.register(Libro, LibroAdmin)
admin.site.register(Genero, GeneroAdmin)
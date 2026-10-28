from django.contrib import admin

from .models import Categoria, Livro


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ("nome",)


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "categoria", "preco", "disponivel")
    list_filter = ("categoria", "disponivel")
    search_fields = ("titulo", "autor", "isbn")

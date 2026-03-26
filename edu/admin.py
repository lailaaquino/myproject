from django.contrib import admin

# Register your models here.
from .models import Autor, Livro, Editora
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'ISBN', 'titulo', 'publicacao', 'preco', 'estoque', 'editora_id')
    search_fields = ('titulo',)
@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
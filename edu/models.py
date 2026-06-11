from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100, verbose_name=_("Nome"))

class Livro (models.Model):
    ISBN = models.CharField(max_length=13, verbose_name=_("ISBN"))
    titulo = models.CharField(max_length=20, verbose_name=_("Título"))
    publicacao = models.DateField(verbose_name=_("Data de Publicação"))
    preco = models.FloatField(verbose_name=_("Preço"))
    estoque = models.IntegerField(verbose_name=_("Quantidade em Estoque"))
    editora_id = models.ForeignKey('Editora', on_delete=models.CASCADE, verbose_name=_("Editora"))
    autores = models.ManyToManyField(Autor, verbose_name=_("Autores"))
    
class Editora(models.Model):
    nome = models.CharField(max_length=10, verbose_name=_("Nome da Editora"))
    
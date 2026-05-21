from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100)

class Livro (models.Model):
    ISBN = models.CharField(max_length=13)
    titulo = models.CharField(max_length=20)
    publicacao = models.DateField()
    preco = models.FloatField()
    estoque = models.IntegerField()
    editora_id = models.ForeignKey('Editora', on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)
    
class Editora(models.Model):
    nome = models.CharField(max_length=10)
    
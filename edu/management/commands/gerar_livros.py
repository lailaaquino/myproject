from django.core.management.base import BaseCommand
from edu.models import Livro, Editora
from faker import Faker
import random


import random

class Command(BaseCommand):
    help = 'Comando para gerar 100 registros de livros' 

    def handle(self, *args, **options): 
        fake = Faker()
        lista_editoras = list(Editora.objects.values_list('id', flat=True))
        if not lista_editoras:
            self.stdout.write(self.style.ERROR('Nenhuma editora cadastrada. Cadastre editoras antes de gerar livros.'))
            return

        for i in range(100): 
            Livro.objects.create(
                titulo=fake.sentence(nb_words=3)[:20], 
                ISBN=fake.isbn13(),                    
                publicacao=fake.date_this_century(),   
                preco=random.uniform(20.0, 150.0),     
                estoque=random.randint(1, 50),        
                editora_id=Editora.objects.get(id=random.choice(lista_editoras))
            )

        self.stdout.write(self.style.SUCCESS('Livros criados com sucesso!'))
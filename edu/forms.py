from django import forms
from .models import Livro
from .models import Editora
from .models import Autor

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['ISBN', 'titulo', 'publicacao', 'preco', 'estoque', 'editora_id', 'autores']
        widgets = {
            'ISBN': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'publicacao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'editora_id': forms.Select(attrs={'class': 'form-select'}),
            'autores': forms.SelectMultiple(attrs={'class': 'form-select'})
        }
        
    
class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'})
        }
    
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'})
        }

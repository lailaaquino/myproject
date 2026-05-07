from django import forms
from .models import Livro
from .models import Editora
from .models import Autor
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'email@exemplo.com', 'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

class SignInForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'input-text'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'input-text'})
    )

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

def home(request):
    return render(request, 'edu/home.html')
from django.shortcuts import redirect, render
from .models import Livro
from .forms import LivroForm, SignUpForm, SignInForm
from .models import Editora
from .forms import EditoraForm
from .models import Autor
from .forms import AutorForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.http import HttpResponseNotAllowed
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.auth.decorators import permission_required


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('edu:home')
    else:
        form = SignUpForm()
    return render(request, 'edu/registro_usuario.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next', '') or request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            return redirect('edu:home')
    else:
        form = SignInForm()
    return render(request, 'edu/login_usuario.html', {'form': form})

def logout_view(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    logout(request)
    return redirect('signin')

# Create your views here.

@login_required

@permission_required('edu.add_livro')
def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid(): # se está de acordo com definição em models 
            form.save()
            return redirect('edu:list_livros')
    else:
        form = LivroForm()
    return render(request, 'edu/cadastro_livro.html', {'form': form})

def editora_create(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_editoras')
    else:
        form = EditoraForm()
    return render(request, 'edu/cadastro_editora.html', {'form': form})

def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_autores')
    else:
        form = AutorForm()
    return render(request, 'edu/cadastro_autor.html', {'form': form})

#agr para atualizar dados 
@permission_required('edu.change_livro')
@login_required
def edit_livros(request, id):
    from .models import Livro
    livro = Livro.objects.get(id=id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('edu:list_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'edu/cadastro_livro.html', {'form': form})

def edit_editoras(request, id):
    from .models import Editora
    editora = Editora.objects.get(id=id)
    if request.method == 'POST':
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
            return redirect('list_editoras')
    else:
        form = EditoraForm(instance=editora)
    return render(request, 'edu/cadastro_editora.html', {'form': form})

def edit_autores(request, id):
    from .models import Autor
    autor = Autor.objects.get(id=id)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('list_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'edu/cadastro_autor.html', {'form': form})

def list_livros(request):
    from .models import Livro
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    livros = Livro.objects.all().order_by('titulo')
    page = request.GET.get('page', 1)
    paginator = Paginator(livros, 5)  
    try:
        livros = paginator.page(page)
    except PageNotAnInteger:
        livros = paginator.page(1)
    except EmptyPage:
        livros = paginator.page(paginator.num_pages)
        
    return render(request, 'edu/livro_list.html', {'livros': livros})

def list_editoras(request):
    editoras = Editora.objects.all()
    return render(request, 'edu/editora_list.html', {'editoras': editoras})

def list_autores(request):
    autores = Autor.objects.all()
    return render(request, 'edu/autor_list.html', {'autores': autores})

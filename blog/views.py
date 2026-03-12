from datetime import date

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def welcome(request):
    dicionario = [
        {"nome": "maça", "preço": "4"},
        {"nome": "banana", "preço": "3"},
        {"nome": "laranja", "preço": "2"},
        {"nome": "morango", "preço": "4"},
    ]
    numero = 9999999
    
    context = {
    "nome": "Edemberg",
    "data": date.today(),
    "is_logged_in": True,
    "is_role" == "admin": False,
    "is_role" == "user": True,
    "dicionario": dicionario,
    "numero": numero
    }    
    return render(request, "blog/index.html", context)


def eco(request, msg):
    return HttpResponse(f"Você digitou: {msg}")

def info(request):
    info= {
        "disciplina": "RAD",
        "framework": "Django",
        "semestre": "2025.2"
    }
    return JsonResponse(info)


def home(request):
    return render(request, "blog/home.html")

def contato(request, numero):
    return HttpResponse(f"Entre em contato conosco pelo pelo telefone {numero}")




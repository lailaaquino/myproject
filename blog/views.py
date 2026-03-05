from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def welcome(request):
    return HttpResponse("Bem vindo ao meu blog!")

def eco(request, msg):
    return HttpResponse(f"Você digitou: {msg}")

def info(request):
    info= {
        "disciplina": "RAD",
        "framework": "Django",
        "semestre": "2025.2"
    }
    return JsonResponse(info)


from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def lista_produtos(request):
    produtos = [
        {"id": 1, "nome": "Arroz", "quantidade": 50},
        {"id": 2, "nome": "Feijão", "quantidade": 30},
        {"id": 3, "nome": "Macarrão", "quantidade": 20},
    ]
    return JsonResponse(produtos, safe=False)

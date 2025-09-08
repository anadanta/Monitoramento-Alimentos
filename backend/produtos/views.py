from django.shortcuts import render, redirect
from produtos.forms import ProdutoForm

# Create your views here.
from django.http import JsonResponse

def lista_produtos(request):
    produtos = [
        {"id": 1, "nome": "Arroz", "quantidade": 50},
        {"id": 2, "nome": "Feijão", "quantidade": 30},
        {"id": 3, "nome": "Macarrão", "quantidade": 20},
    ]
    return JsonResponse(produtos, safe=False)

def formulario_produtos(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    
    context = {
        'title': 'Formulário Produtos',
        'form': form
    }

    return render(request, 'produtos/formulario_produtos.html',context)

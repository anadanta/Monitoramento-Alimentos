from django.shortcuts import render, redirect
from produtos.forms import ProdutoForm
from core.models import Produto

# Create your views here.
from django.http import JsonResponse

def lista_produtos(request):

    # Implementar lógica para obter o usuário
    # usuario = 1
    # produtos = Produto.objects.filter(usuario=usuario)

    produtos = Produto.objects.all()

    context = {
        'title': 'Produtos',
        'produtos': produtos,
        'title': 'Listagem de Produtos',
    }

    return render(request, 'produtos/listagem_produtos.html', context)

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

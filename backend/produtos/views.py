from django.shortcuts import render, redirect
from produtos.forms import ProdutoForm
from core.models import Produto
from usuarios.models import Usuarios

def lista_produtos(request):
    if 'usuario_id' not in request.session:
        return redirect('login')

    # Implementar lógica para obter o usuário
    usuario = Usuarios.objects.get(id=request.session['usuario_id'])
    produtos = Produto.objects.filter(usuario=usuario)

    context = {
        'title': 'Produtos',
        'produtos': produtos,
        'title': 'Listagem de Produtos',
    }

    return render(request, 'produtos/listagem_produtos.html', context)

def formulario_produtos(request):
    if 'usuario_id' not in request.session:
        return redirect('login')
    
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            usuario_id = request.session.get('usuario_id')
            if usuario_id:
                produto.usuario_id = usuario_id
                form.save()
                return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    
    context = {
        'title': 'Formulário Produtos',
        'form': form
    }

    return render(request, 'produtos/formulario_produtos.html',context)

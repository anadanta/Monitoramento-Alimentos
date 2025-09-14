from django.shortcuts import render, redirect
from produtos.forms import ProdutoForm
from core.models import Produto
from usuarios.models import Usuarios
import datetime
from django.contrib import messages

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
    
    form = ProdutoForm(request.POST)

    if request.method == "POST":
        data_validade = request.POST.get('data_validade')
        codigo = request.POST.get('codigo')
        usuario_id = request.session.get('usuario_id')

        try:
            data_validade = datetime.datetime.strptime(data_validade, "%d/%m/%Y")
            if (datetime.datetime.now() >= data_validade):
                messages.error(request, "Seu produto está vencido ou venceu hoje. Digite uma data de validade válida")
                return render(request, 'produtos/formulario_produtos.html', {
                    'title': 'Formulário Produtos',
                    'form': form
                })
        except ValueError:
            messages.error(request, "Formato de data inválido. Use DD/MM/AAAA")
            return render(request, 'produtos/formulario_produtos.html', {
                'title': 'Formulário Produtos',
                'form': form
            })
        
        if Produto.objects.filter(codigo=codigo, usuario_id=usuario_id).exists():
            messages.error(request, "Código ja cadastrado...")
            return render(request, 'produtos/formulario_produtos.html', {
                'title': 'Formulário Produtos',
                'form': form
            })

        if form.is_valid():
            produto = form.save(commit=False)
            usuario_id = request.session.get('usuario_id')
            produto.usuario_id = usuario_id
            produto.data_validade = data_validade
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    
    context = {
        'title': 'Formulário Produtos',
        'form': form
    }

    return render(request, 'produtos/formulario_produtos.html',context)

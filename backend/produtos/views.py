from django.shortcuts import render, redirect, get_object_or_404
from produtos.forms import ProdutoForm
from core.models import Produto, StatusProduto, Categoria
from usuarios.models import Usuarios
import datetime
from django.contrib import messages

def lista_produtos(request):
    if 'usuario_id' not in request.session:
        return redirect('login')

    usuario = Usuarios.objects.get(id=request.session['usuario_id'])
    produtos = Produto.objects.filter(usuario=usuario)
    categorias = Categoria.objects.all()

    # -- Filtro que pesquisa por nome do produto --
    query = request.GET.get('q')
    if query:
        produtos = produtos.filter(nome__icontains=query)

    # -- Ordenação por data de validade --
    sort_by = request.GET.get('sort')
    if sort_by == 'data_asc':
        produtos = produtos.order_by("data_validade")
    elif sort_by == 'data_desc':
        produtos = produtos.order_by("-data_validade")

    # -- Filtro por status --
    status = request.GET.get('status')
    if status and status in dict(StatusProduto.choices).keys():
        produtos = produtos.filter(status=status)

    # -- Filtro por categoria --
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        produtos = produtos.filter(categoria_id=categoria_id)

    # -- Filtro pelo intervalo de data de validade do produto --
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    if data_inicio and data_fim:
        produtos = produtos.filter(data_validade__range=[data_inicio, data_fim])
    elif data_inicio:
        produtos = produtos.filter(data_validade__gte=data_inicio)
    elif data_fim:
        produtos = produtos.filter(data_validade__lte=data_fim)

    # -- Ordenação por data de quantidade disponível (Estoque) --
    sort_by_quantidade = request.GET.get('sort_validade')
    if sort_by_quantidade == 'quantidade_asc':
        produtos = produtos.order_by("quantidade_disponivel")
    elif sort_by_quantidade == 'quantidade_desc':
        produtos = produtos.order_by("-quantidade_disponivel")

    form = ProdutoForm()    

    context = {
        'title': 'Produtos',
        'produtos': produtos,
        'title': 'Listagem de Produtos',
        'form': form,
        "status_choices": StatusProduto.choices,
        'categorias': categorias
    }

    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')

        if produto_id:
            produto = get_object_or_404(Produto, id=produto_id)
            form = ProdutoForm(request.POST, instance=produto)

            data_validade = request.POST.get('data_validade')
            codigo = request.POST.get('codigo')
            usuario_id = request.session.get('usuario_id')

            try:
                data_validade = datetime.datetime.strptime(data_validade, "%d/%m/%Y")
                if (datetime.datetime.now() >= data_validade):
                    messages.error(request, "Seu produto está vencido ou venceu hoje. Digite uma data de validade válida")
                    return render(request, 'produtos/listagem_produtos.html', context)
            except ValueError:
                messages.error(request, "Formato de data inválido. Use DD/MM/AAAA")
                return render(request, 'produtos/listagem_produtos.html', context)

            if Produto.objects.filter(usuario_id=usuario_id, codigo=codigo).exclude(pk=produto.id).exists():
                messages.error(request, "Código já cadastrado...")
                return render(request, 'produtos/listagem_produtos.html', context)

            if form.is_valid():
                form.save()
                messages.success(request, "Produto editado com sucesso.")
                return redirect('lista_produtos')
        else:
            form = ProdutoForm(request.POST)

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
        
        if Produto.objects.filter(usuario_id=usuario_id, codigo=codigo).exists():
            messages.error(request, "Código já cadastrado...")
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
            messages.success(request, "Produto criado com sucesso.")
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()

    context = {
        'title': 'Formulário Produtos',
        'form': form
    }

    return render(request, 'produtos/formulario_produtos.html',context)

def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == "GET":
        messages.success(request, "Produto deletado com sucesso.")
        produto.delete()

    return redirect('lista_produtos')
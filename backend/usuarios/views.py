from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from usuarios.models import Usuarios
from usuarios.forms import UsuarioForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            usuario = Usuarios.objects.get(email=email)
            if check_password(senha, usuario.senha):
                request.session['usuario_id'] = usuario.id
                return redirect('lista_produtos')
            else:
                messages.error(request, "A senha não confere...")
        except Usuarios.DoesNotExist:
            messages.error(request, "Usuário não encontrado...")

    context = {
        'title': 'Login'
    }

    return render(request, 'usuarios/login.html', context)

def cadastro(request):

    form = UsuarioForm(request.POST)

    if request.method == "POST":
        senha_confirmacao = request.POST.get('senha_confirmacao')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        
        if senha != senha_confirmacao:
            messages.error(request, "As senhas nao conferem...")
            return render(request, 'usuarios/cadastro.html', {
                'title': 'Cadastro',
                'form': form
            })
        
        if Usuarios.objects.filter(email=email).exists():
            messages.error(request, "Email ja cadastrado...")
            return render(request, 'usuarios/cadastro.html', {
                'title': 'Cadastro',
                'form': form
            })
        
        if form.is_valid():
            usario = form.save(commit=False) # Instancia um usuário, mas não salva
            usario.senha = make_password(senha) # Criptografa a senha
            form.save() # Salva o usuário
            messages.success(request, "Usuário cadastrado com sucesso...")
            return redirect('login')

    context = {
        'title': 'Cadastro',
        'form': form
    }

    return render(request, 'usuarios/cadastro.html', context)

def sair(request):
    logout(request)
    
    return HttpResponseRedirect('/') # Redireciona para a home

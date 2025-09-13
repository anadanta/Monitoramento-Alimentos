from django import forms
from usuarios.models import Usuarios

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nome_estabelecimento', 'email', 'senha', 'segmento']
        widgets = {
            'nome_estabelecimento': forms.TextInput(attrs={
                'class': 'w-full mt-1 px-4 py-2 border rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none',
                'placeholder': 'Digite o nome do seu estabelecimento',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full mt-1 px-4 py-2 border rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none',
                'placeholder': 'Digite seu email',
                'required': 'required'
            }),
            'senha': forms.PasswordInput(attrs={
                'class': 'w-full mt-1 px-4 py-2 border rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none',
                'id': 'senha',
                'placeholder': 'Digite sua senha',
                'required': 'required'
            }),
            'segmento': forms.Select(attrs={
                'class': 'w-full mt-1 px-4 py-2 border rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none',
                'required': 'required'
            }),
        }
from django import forms
from core.models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'data_validade','unidade_medida', 'quantidade_disponivel', 'codigo']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full mt-1 px-4 py-2 border rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none',
                'placeholder': 'Digite o nome do produto',
                'required': 'required'
            }),
            'categoria': forms.Select(attrs={
                'class': 'w-full mt-1 px-4 py-2 border rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none',
                'required': 'required'
            }),
            'data_validade': forms.TextInput(attrs={
                'class': 'w-full mt-1 px-4 py-2 border rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none',
                'placeholder': 'dd/mm/aaaa',
                'required': 'required',
                'id': 'data_validade'
            }),
            'unidade_medida': forms.Select(attrs={
                'class': 'w-full mt-1 px-4 py-2 border rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none',
                'required': 'required'
            }),
            'quantidade_disponivel': forms.TextInput(attrs={
                'class': 'w-full mt-1 px-4 py-2 border rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none',
                'placeholder': 'Digite a quantidade de produto disponível',
                'required': 'required',
                'id': 'quantidade_disponivel'
            }),
            'codigo': forms.TextInput(attrs={
                'class': 'w-full mt-1 px-4 py-2 border rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none',
                'placeholder': 'Digite o código do produto',
                'id': 'codigo'
            }),
        }

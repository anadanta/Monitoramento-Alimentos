from django import forms
from core.models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'data_validade', 'quantidade_disponivel']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'
            }),
            'categoria': forms.Select(attrs={
                'class': 'w-full p-2 border rounded-lg bg-white focus:ring-2 focus:ring-blue-500 focus:outline-none'
            }),
            'data_validade': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'
            }),
            'quantidade_disponivel': forms.NumberInput(attrs={
                'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'
            }),
        }

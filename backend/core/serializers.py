from rest_framework import serializers
from .models import Categoria, Produto

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer para o modelo Categoria.
    Usa hyperlinks para representar as relações.
    """
    class Meta:
        model = Categoria
        # 'url' é o link para o detalhe da categoria, 'nome' é o nome
        fields = ['url', 'id', 'nome']
        extra_kwargs = {
            'url': {'view_name': 'categoria-detail'},
        }


class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer para o modelo Produto.
    Usa hyperlinks para representar as relações.
    """
    # Representa a categoria como um link para a API de categorias
    categoria = serializers.HyperlinkedRelatedField(
        view_name='categoria-detail',
        queryset=Categoria.objects.all()
    )

    # Campo para exibir o nome da categoria (apenas leitura)
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True, required=False)

    class Meta:
        model = Produto
        # Trocamos 'id' por 'url' para ter o link clicável
        fields = [
            'url',
            'id',
            'nome',
            'categoria',
            'categoria_nome',
            'data_validade',
            'quantidade_disponivel'
        ]
        # Informa ao DRF qual URL usar para o detalhe do produto
        extra_kwargs = {
            'url': {'view_name': 'produto-detail'},
        }


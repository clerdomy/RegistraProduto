from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    """
    Serializador para converter objetos Produto em representações JSON e vice-versa.

    Attributes:
        model (Produto): O modelo associado ao serializador.
        fields (list): Lista de campos a serem incluídos na representação JSON.
    """

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'valor', 'disponivel', 'descricao']

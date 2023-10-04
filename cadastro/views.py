from rest_framework import viewsets
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manipulação de operações CRUD (Create, Read, Update, Delete) em produtos.

    Attributes:
        queryset (QuerySet): Um conjunto de objetos Produto.
        serializer_class (ProdutoSerializer): O serializador usado para converter objetos Produto em JSON e vice-versa.
    """

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer




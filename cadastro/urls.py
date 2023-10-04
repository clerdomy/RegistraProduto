"""
Módulo de definição de URLs para a API REST relacionada a cadastro de produtos.

Este módulo utiliza o Django REST Framework para criar rotas (URLs) para operações CRUD
relacionadas a produtos, usando a classe ProdutoViewSet.

Attributes:
    router (DefaultRouter): Um roteador padrão do Django REST Framework para criar automaticamente as rotas da API.
    urlpatterns (list): Lista de padrões de URL criados pelo roteador para a API REST de produtos.

"""
from rest_framework import routers
from .views import ProdutoViewSet

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = router.urls



from rest_framework import routers
from .views import ProdutoViewSet

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = router.urls


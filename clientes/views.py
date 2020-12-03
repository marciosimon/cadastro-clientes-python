from rest_framework import viewsets
from clientes.models import Cliente, Produto
from clientes.serializer import ClienteSerializer, ProdutoSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
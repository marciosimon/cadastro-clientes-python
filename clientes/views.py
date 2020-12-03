from rest_framework import viewsets
from clientes.models import Cliente
from clientes.serializer import ClienteSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
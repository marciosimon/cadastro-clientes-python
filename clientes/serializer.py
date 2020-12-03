from rest_framework import serializers
from clientes.models import Cliente, Produto

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ['id','nome','email','produtos']


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = ['id','price','image', 'brand', 'title', 'reviewScore']
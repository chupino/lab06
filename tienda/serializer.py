from rest_framework import serializers
from .models import Producto,Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre','pub_date')
class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    class Meta:
        model = Producto
        fields = ('id', 'categoria', 'precio', 'nombre', 'stock', 'pub_date')
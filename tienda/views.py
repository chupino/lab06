from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.http import HttpResponse
from .serializer import ProductoSerializer, CategoriaSerializer

# Create your views here.
class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
class ProductoView(APIView):
    
    def get(self,request):
        dataSeries = Producto.objects.all()
        prodSeries = ProductoSerializer(dataSeries,many=True)
        return Response(prodSeries.data)
    
class ProductoDetailView(APIView):
    
    def get(self,request,producto_id):
        dataSerie = Producto.objects.get(pk=producto_id)
        prodSerie = ProductoSerializer(dataSerie)
        return Response(prodSerie.data)
    
    def put(self,request,producto_id):
        dataSerie = Producto.objects.get(pk=producto_id)
        prodSerie = ProductoSerializer(dataSerie,data=request.data)
        prodSerie.is_valid(raise_exception=True)
        prodSerie.save()
        return Response(prodSerie.data)
    
    def delete(self,request,producto_id):
        dataSerie = Producto.objects.get(pk=producto_id)
        prodSerie = ProductoSerializer(dataSerie)
        dataSerie.delete()
        return Response(prodSerie.data)

class ProductosxCategoriaView(APIView):
    def get(self,request,categoria_id):
        categoria = get_object_or_404(Categoria, pk=categoria_id)
        products = Producto.objects.filter(categoria=categoria).order_by('nombre')
        products_data = [ProductoSerializer(product).data for product in products]
        return Response(products_data)
class CategoriaView(APIView):
    
    def get(self,request):
        dataSeries = Categoria.objects.all()
        catSeries = CategoriaSerializer(dataSeries,many=True)
        return Response(catSeries.data)
    
def index(request):
    api_url_producto = 'http://127.0.0.1:8000/tienda/producto'
    api_url_categoria = 'http://127.0.0.1:8000/tienda/categoria'
    responseProducto = requests.get(api_url_producto)
    responseCategoria = requests.get(api_url_categoria)
    product_list = responseProducto.json()
    categorias = responseCategoria.json()
    context = {'product_list':product_list, 'category_list': categorias}
    return render(request,'index.html',context)

def producto(request, producto_id):
    api_url_categoria = 'http://127.0.0.1:8000/tienda/categoria'
    api_url_producto = f'http://127.0.0.1:8000/tienda/producto/{producto_id}'
    responseProducto = requests.get(api_url_producto)
    responseCategoria = requests.get(api_url_categoria)
    categorias = responseCategoria.json()
    producto = responseProducto.json()
    return render(request,'producto.html', {'producto': producto,'category_list': categorias})

def categoria(request, categoria_id):
    api_url_categoria = 'http://127.0.0.1:8000/tienda/categoria/{categoria_id}'
    responseCategoria = requests.get(api_url_categoria)
    product_list = responseCategoria.json()
    return render(request,'categoria.html', {'product_list': product_list})


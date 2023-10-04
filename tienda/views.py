from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categorias = Categoria.objects.order_by('nombre')
    context = {'product_list':product_list, 'category_list': categorias}
    return render(request,'index.html',context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk = producto_id)
    categorias = Categoria.objects.order_by('nombre')[:6]
    return render(request,'producto.html', {'producto': producto,'category_list': categorias})

def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    product_list = Producto.objects.filter(categoria=categoria).order_by('nombre')
    return render(request,'categoria.html', {'product_list': product_list})


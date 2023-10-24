from django.urls import path

from . import views

app_name = "tienda"

urlpatterns = [
    path('', views.index, name='index'),
    path('producto',views.ProductoView.as_view(),name='productos'),
    path('producto/<int:producto_id>',views.ProductoDetailView.as_view()),
    path('categoria',views.CategoriaView.as_view()),
    path('productos/<int:producto_id>/',views.producto,name='producto'),
    path('categoria/<int:categoria_id>/',views.ProductosxCategoriaView.as_view(),name='categoria'),
    path('categorias/<int:categoria_id>/',views.categoria,name='categorias')
]

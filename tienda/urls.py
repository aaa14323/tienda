from django.urls import path
from . import views
app_name = 'tienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/', views.producto_index, name='producto'),
    path('cliente/', views.cliente_index, name='cliente'),
    path('compra/', views.compra, name='compra'),
    path('compraProducto/', views.compra_producto, name="compra-producto"),
    path('add/', views.cliente_add, name='cliente-add'),
    path('addp/', views.producto_add, name='producto-add'),
    path('imagenes/', views.imagenes, name='creditos-imagenes'),
    path('delete/<int:idc>', views.delete_cliente, name='deletec'),
    path('deletep/<int:idp>', views.delete_producto, name='deletep'),
    path('updatec/<int:idcl>', views.update_cliente, name='updatec'),
    path('updatep/<int:idpr>', views.update_producto, name='updatep'),
]
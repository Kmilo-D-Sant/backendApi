from django.urls import path
from api.views import *
from rest_framework.authtoken import views
from .helpers import CustomAuthToken
from .views import GestionarProducto

app_name = 'api'

urlpatterns = [
    path('gestionar-producto', GestionarProducto.as_view(), name="gestionar-producto"),
    path('gestionar-usuario', GestionarUsuario.as_view(), name="gestionar-usuario"),
    path('gestionar-factura', GestionarFactura.as_view(), name="gestionar-factura"),
    path('factura-detalles', facturaDetalles, name="factura-detalles"),
    path('gestionar-pedido', GestionarPedido.as_view(), name="gestionar-pedido"),
    path('gestionar-direccion', GestionarDireccion.as_view(), name="gestionar-direccion"),
    #path('filtrar', filtro2, name="filtrar"),
    path('obtener-categoria', obtenerCategoria, name="obtener-categoria"),
    path('api-token/', CustomAuthToken.as_view()),
    
    path('producto-categoria', productosPorCategoria, name="producto-categoria"),
    path('producto-proveedor', productosPorProveedor, name="producto-proveedor"),
    path('producto-nombre', productosPorNombre, name="producto-nombre"),
    path('producto-detalles', productoDetalles, name="producto-detalles"),
    
    ]
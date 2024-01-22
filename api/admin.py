from django.contrib import admin

from django.contrib import admin
from django.contrib.auth import get_user_model

from api.helpers import crearSerializador
from .models import *
# from django.apps import apps

Usuario = get_user_model()

#admin.site.register(Usuario)
#admin.site.register(Nom_Catergoria)
#admin.site.register(Producto)

#admin.site.register(Pedido)
#admin.site.register(Direccion)
#admin.site.register(Factura)
@admin.register(Usuario)
class Usuario(admin.ModelAdmin):
    list_display  = ["username","first_name", "telefono", "es_proveedor", "is_active"]
    list_filter = ("es_proveedor", "is_active")

@admin.register(Direccion)
class Direccion(admin.ModelAdmin):
    list_display  = ["direccion", "referencia", "usuario"]

@admin.register(Producto)
class Producto(admin.ModelAdmin):
    list_display  = ["nombre", "categoriaNombre", "precio", "usuario", "activo"]
    list_filter = ("categoria","usuario", "activo" )
    search_fields = ("nombre__startswith", )
    def categoriaNombre(self, obj):
        return obj.categoria.valor
    
@admin.register(Factura)
class Factura(admin.ModelAdmin):
    list_display  = ["total", "aprobada", "destinatario", "fecha", "impuesto", "impuestos_pagados"]
    list_filter = ("destinatario", "impuestos_pagados", "aprobada" )
    
  
    
@admin.register(Pedido)
class Pedido(admin.ModelAdmin):
    list_display  = ["producto","productoPrecio", "cantidad", "total" ,"factura"]
    
    def productoPrecio(self, obj):
        return obj.producto.precio
    def total(self, obj):
        return obj.producto.precio * obj.cantidad
 
    
@admin.register(Nom_Catergoria)
class Nom_Catergoria(admin.ModelAdmin):
    list_display  = ["valor"]

# def crearDiccionarioAtributos():
#     app_models = apps.get_app_config('api').get_models()

#     diccionarioAtributos = {}
#     for model in app_models:
#         listaCampos = []
#         campos = model.objects.model._meta.get_fields(include_hidden=True)
#         for campo in campos:
#             campo = str(campo)
#             try:
#                 campoAux = campo[campo.index(model.__name__+"."):]
#                 campoAux = campoAux[campoAux.index(".")+1:]

#             except:
#                 campoAux = campo[campo.index(".")+1: -1]
#             listaCampos.append(campoAux)
#         diccionarioAtributos[model] = listaCampos
#     return diccionarioAtributos

# DICCIONARIO_ATRIBUTOS = crearDiccionarioAtributos()

# admin.site.register(Vendedor)

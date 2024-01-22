from django.db import models
from .helpers import error, respuesta
from datetime import datetime
from rest_framework import status
from django.contrib.auth.models import AbstractUser, User
import base64
import io
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile



class Usuario(AbstractUser):
    telefono = models.CharField(max_length=10)
    es_proveedor = models.BooleanField("Es proveedor", default= False, null =False, blank = False)
    imagen = models.ImageField(blank= True, null= True, default="",upload_to="imagenes/")
    imagenB64 = models.TextField(blank= True, null= True)
    

    def __nuevo__(username, password, first_name, email, telefono, es_proveedor, is_staff, imagen, imagenB64):
        self = Usuario()
        if imagen != None:
            imagen_io = io.BytesIO()
            imagen.save(imagen_io, format='PNG')
            self.imagen = InMemoryUploadedFile(imagen_io, field_name=None, name= username + ".png", content_type='imagen/png', size=imagen_io.tell, charset=None)
            
        self.username = username
        self.set_password(password)
        self.first_name = first_name
        self.email = email
        self.telefono = telefono
        self.es_proveedor = es_proveedor
        self.is_staff = is_staff
        self.imagenB64 = imagenB64
        self.save()
        return self      
    
    def __actualizar__(self, username, password, first_name, email, telefono, es_proveedor, is_staff, imagen, imagenB64):
        if imagen != None:
            imagen_io = io.BytesIO()
            imagen.save(imagen_io, format='PNG')
            self.imagen = InMemoryUploadedFile(imagen_io, field_name=None, name= username + ".png", content_type='imagen/png', size=imagen_io.tell, charset=None)
        self.username = username
        self.set_password(password)
        self.first_name = first_name
        self.imagenB64 = imagenB64
        self.email = email
        self.telefono = telefono
        self.es_proveedor = es_proveedor
        self.is_staff = is_staff
        self.save()
        return self     
     
    def __inhabilitar__(self):
        self.is_active = False
        self.save()
        return self 
    
    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

class Nom_Catergoria(models.Model):
    valor = models.CharField("Valor", max_length=50, blank=False, null=False)
    def __str__(self):
       return self.valor

class Direccion(models.Model):
    nombre = models.CharField("Nombre", max_length=50, blank=False, null=False)
    direccion = models.CharField("Dirección", max_length=250, blank=False, null=False)
    referencia = models.CharField("Referencia", max_length=250, blank=False, null=False)
    usuario = models.ForeignKey(Usuario, on_delete = models.SET_NULL, null = True)
    
    def __nuevo__(nombre, direccion, referencia, usuario):
        self = Direccion()
        self.nombre = nombre
        self.direccion = direccion
        self.referencia = referencia
        self.usuario = usuario
        self.save()
        return self
    
    def __actualizar__(self, nombre, direccion, referencia):
        self.nombre = nombre
        self.precio = direccion
        self.descripcion = referencia
        self.save()
        return self
    
    def __inhabilitar__(self):
        self.delete()
        return self
    
    def __str__(self):
       return self.nombre
class Producto(models.Model):
    nombre = models.CharField("Name", max_length=50, blank=False, null=False)
    precio = models.FloatField("Precio", blank=False, null=False)
    descripcion = models.CharField("Descripcion", max_length=100, blank=True, null=True)
    imagen = models.ImageField(blank= True, null= True, default="",upload_to="imagenes/")
    imagenB64 = models.TextField(blank= True, null= True)
    categoria = models.ForeignKey(Nom_Catergoria, on_delete = models.SET_NULL, null = True)
    activo = models.BooleanField("Activo", default= True, null =False, blank = False)
    usuario = models.ForeignKey(Usuario, on_delete = models.SET_NULL,related_name = '+', null = True)
    
    def __str__(self):
       return self.nombre +"_"+ self.usuario.username
    
    def __nuevo__(nombre, precio, descripcion, imagen, categoria, usuario, imagenB64):
            productoAux = Producto()
            if imagen != None:
                imagen_io = io.BytesIO()
                imagen.save(imagen_io, format='PNG')
                productoAux.imagen = InMemoryUploadedFile(imagen_io, field_name=None, name= usuario.username + "_" + nombre + ".png", content_type='imagen/jpeg', size=imagen_io.tell, charset=None)
            productoAux.nombre = nombre
            productoAux.precio = precio
            productoAux.descripcion = descripcion
            productoAux.categoria = categoria
            productoAux.usuario = usuario
            productoAux.imagenB64 = imagenB64
            productoAux.save()
            return productoAux
        
    def __actualizar__(self, nombre, precio, descripcion, imagen, categoria, imagenB64):
        if imagen != None:
            imagen_io = io.BytesIO()
            imagen.save(imagen_io, format='PNG')
            self.imagen = InMemoryUploadedFile(imagen_io, field_name=None, name= self.usuario.username + "_" + nombre + ".png", content_type='imagen/jpeg', size=imagen_io.tell, charset=None)
            
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.categoria = categoria
        self.imagenB64 = imagenB64
        self.save()
        return self
    
    def __inhabilitar__(self):
        self.activo = False
        self.save()
        return self   
        
class Factura(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.SET_NULL,related_name = '+', null = True)
    destinatario = models.ForeignKey(Usuario, on_delete = models.SET_NULL, related_name = '+', null = True)
    direccion = models.ForeignKey(Direccion, on_delete = models.CASCADE, null = True)
    numero = models.BigIntegerField("Número")
    fecha = models.DateTimeField(default= datetime.now())
    mensajeria = models.FloatField("Costo por mensajeria")
    total = models.FloatField("Total a pagar")
    aprobada = models.BooleanField("Se aprobo", default = False)
    impuestos_pagados = models.BooleanField("Impuestos pagados", default = False)
    contra_oferta = models.TextField("Contra oferta", null =True, blank = True)
    impuesto = models.FloatField()
    def __str__(self):
       return str(self.pk)

    def __nuevo__(numero, mensajeria, total, aprobada, contra_oferta,impuesto,usuario,destinatario,direccion):
            facturaAux = Factura()
            facturaAux.numero = numero
            facturaAux.mensajeria = mensajeria
            facturaAux.total = total
            facturaAux.aprobada = aprobada
            facturaAux.contra_oferta = contra_oferta
            facturaAux.impuesto = impuesto
            facturaAux.usuario = usuario
            facturaAux.destinatario = destinatario
            facturaAux.direccion = direccion
            facturaAux.save()
            return facturaAux
        
    def __actualizar__(self, mensajeria, total, aprobada, contra_oferta,impuesto,direccion):
        self.mensajeria = mensajeria
        self.total = total
        self.aprobada = aprobada
        self.contra_oferta = contra_oferta
        self.impuesto = impuesto
        self.direccion = direccion
        self.save()
        return self
    
class Pedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete = models.SET_NULL, null = True)
    factura = models.ForeignKey(Factura, on_delete = models.SET_NULL, null = True)
    cantidad = models.IntegerField()
    
    def __nuevo__(producto, factura, cantidad):
        self = Pedido()
        self.producto = producto
        self.factura = factura
        self.cantidad = cantidad
        self.save()
        return self
    
    def __actualizar__(self, cantidad):
        self.cantidad = cantidad
        self.save()
        return self
    
    def __inhabilitar__(self):
        self.delete()
        return self
    
    def calcularCosto(self):
        return self.producto.precio * self.cantidad



#Producto.__nuevo__ ("frijoles", 300, "Granos", "XXXXXXXXXXXXXXXXXXXXX")   
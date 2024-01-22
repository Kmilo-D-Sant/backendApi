from django.db import transaction
from django.db.models import Q
from .models import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .helpers import Base64Aimagen, obtenerUsuario, respuesta, error, crearSerializador
from .const import *

@method_decorator(csrf_exempt, name='dispatch')
class GestionarProducto(View):
    
    def post(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            if not usuario.es_proveedor or not usuario.is_active:
                return error(MENSAJE_USUARIO_NO_AUTORIZADO, status.HTTP_403_FORBIDDEN)
            dataRequest = JSONParser().parse(request)
            imagen = Base64Aimagen(dataRequest['imagen'])
            if imagen == None:
                return error("El producto necesita una imagen", status.HTTP_403_FORBIDDEN)
            serializador = crearSerializador(Producto, 0)
            nuevoProducto =  serializador(Producto.__nuevo__(dataRequest['nombre'],dataRequest['precio'],dataRequest['descripcion'],imagen,Nom_Catergoria.objects.get(id = dataRequest['categoria']), usuario, dataRequest['imagenB64']), many = False).data
            return respuesta(nuevoProducto)
        except BaseException as err:
            return error(str(err))
        
    def get(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None or not usuario.is_active:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            serializador = crearSerializador(Producto, 0)
            if request.body:
                datosRequest = json.loads(request.body.decode('utf-8'))
                productos = serializador(Producto.objects.filter(id = datosRequest.get('id'), usuario = usuario), many = True).data 
            else: 
                productos = serializador(Producto.objects.filter(usuario = usuario), many = True).data
            return respuesta(productos)
        except BaseException as err:
            return error(str(err))
        
    def put(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None or not usuario.is_active:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            dataRequest = JSONParser().parse(request)
            imagen = Base64Aimagen(dataRequest['imagen'])
            if imagen == None:
                return error("El producto necesita una imagen", status.HTTP_403_FORBIDDEN)
            producto = Producto.objects.get(id=dataRequest['id'] )
            if usuario != producto.usuario:
                return error(MENSAJE_USUARIO_NO_AUTORIZADO, status.HTTP_403_FORBIDDEN)
            serializador = crearSerializador(Producto, 0)
            productoActualizado =  serializador(Producto.__actualizar__(producto,dataRequest['nombre'],dataRequest['precio'],dataRequest['descripcion'],imagen,Nom_Catergoria.objects.get(id = dataRequest['categoria']), dataRequest['imagenB64']), many = False).data
            return respuesta(productoActualizado)
        except BaseException as err:
            return error(str(err))
        
    def delete(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None or not usuario.is_active:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            dataRequest = JSONParser().parse(request)
            producto = Producto.objects.get(id=dataRequest['id'] )
            if usuario != producto.usuario:
                return error(MENSAJE_USUARIO_NO_AUTORIZADO, status.HTTP_403_FORBIDDEN)
            serializador = crearSerializador(Producto, 0)
            productoInhabilitado =  serializador(Producto.__inhabilitar__(producto), many = False).data
            return respuesta(productoInhabilitado)
        except BaseException as err:
            return error(str(err))
        

@method_decorator(csrf_exempt, name='dispatch')
class GestionarUsuario(View):
    
    def post(self, request):
        try:
            dataRequest = JSONParser().parse(request)
            imagen = Base64Aimagen(dataRequest['imagen'])
            serializador = crearSerializador(Usuario, 0)
            nuevoUsuario =  serializador(Usuario.__nuevo__(dataRequest['username'],dataRequest['password'],dataRequest['first_name'],dataRequest['email'],dataRequest['telefono'],dataRequest['es_proveedor'],dataRequest['is_staff'], imagen, dataRequest['imagenB64']), many = False).data
            return respuesta(nuevoUsuario)
        except BaseException as err:
            return error(str(err))
        
    def get(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None or not usuario.is_active:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            serializador = crearSerializador(Usuario, 0)
            return respuesta(serializador(Usuario.objects.filter(id = usuario.id), many = True).data)
            # usuario = obtenerUsuario(request)
            # if usuario == None:
            #     return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            # serializador = crearSerializador(Usuario, 0)
            # if request.body:
            #     datosRequest = json.loads(request.body.decode('utf-8'))
            #     usuarios = serializador(Usuario.objects.filter(id = datosRequest.get('id')), many = True).data 
            # else: 
            #     usuarios = serializador(Usuario.objects.all(), many = True).data
            #return respuesta(usuarios)
        except BaseException as err:
            return error(str(err))
        
    def put(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None or not usuario.is_active:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            dataRequest = JSONParser().parse(request)
            imagen = Base64Aimagen(dataRequest['imagen'])
            serializador = crearSerializador(Usuario, 0)
            usuarioActualizado =  serializador(Usuario.__actualizar__(usuario,dataRequest['username'],dataRequest['password'],dataRequest['first_name'],dataRequest['email'],dataRequest['telefono'],dataRequest['es_proveedor'],dataRequest['is_staff'], imagen, dataRequest['imagenB64']), many = False).data
            return respuesta(usuarioActualizado)
        except BaseException as err:
            return error(str(err))
        
    def delete(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None or not usuario.is_active:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            serializador = crearSerializador(Usuario, 0)
            usuarioInhabilitado =  serializador(Usuario.__inhabilitar__(usuario), many = False).data
            return respuesta(usuarioInhabilitado)
        except BaseException as err:
            return error(str(err))


@method_decorator(csrf_exempt, name='dispatch')
class GestionarDireccion(View):
    
    def post(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None or not usuario.is_active:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            dataRequest = JSONParser().parse(request)
            serializador = crearSerializador(Direccion, 0)
            nuevaDireccion =  serializador(Direccion.__nuevo__(dataRequest['nombre'],dataRequest['direccion'],dataRequest['referencia'],usuario), many = False).data
            return respuesta(nuevaDireccion)
        except BaseException as err:
            return error(str(err))
        
    def get(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None or not usuario.is_active:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            serializador = crearSerializador(Direccion, 0)
            if request.body:
                datosRequest = json.loads(request.body.decode('utf-8'))
                direccion = serializador(Direccion.objects.filter(id = datosRequest.get('id'), usuario = usuario), many = True).data 
            else: 
                direccion = serializador(Direccion.objects.filter(usuario = usuario), many = True).data
            return respuesta(direccion)
        except BaseException as err:
            return error(str(err))
        
    def put(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            direccion = Direccion.objects.get(id=dataRequest['id'] )
            if usuario != direccion.usuario or not usuario.is_active:
                return error(MENSAJE_USUARIO_NO_AUTORIZADO, status.HTTP_403_FORBIDDEN)
            dataRequest = JSONParser().parse(request)
            serializador = crearSerializador(Direccion, 0)
            usuarioActualizado =  serializador(Direccion.__actualizar__(direccion ,dataRequest['nombre'],dataRequest['direccion'],dataRequest['referencia']), many = False).data
            return respuesta(usuarioActualizado)
        except BaseException as err:
            return error(str(err))
        
    def delete(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            direccion = Direccion.objects.get(id=dataRequest['id'] )
            if usuario != direccion.usuario or not usuario.is_active:
                return error(MENSAJE_USUARIO_NO_AUTORIZADO, status.HTTP_403_FORBIDDEN)
            dataRequest = JSONParser().parse(request)
            serializador = crearSerializador(Direccion, 0)
            direccionInhabilitada =  serializador(Direccion.__inhabilitar__(direccion), many = False).data
            return respuesta(direccionInhabilitada)
        except BaseException as err:
            return error(str(err))

 
@method_decorator(csrf_exempt, name='dispatch')
class GestionarFactura(View):
    
    def post(self, request):
        try:
            with transaction.atomic():
                usuario = obtenerUsuario(request)
                if usuario == None or not usuario.is_active:
                    return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
                dataRequest = JSONParser().parse(request)
                serializador = crearSerializador(Factura, 0)
                nuevaFactura = Factura.__nuevo__(dataRequest['numero'],dataRequest['mensajeria'],dataRequest['total'],dataRequest['aprobada'],dataRequest['contra_oferta'],dataRequest['impuesto'],usuario,Usuario.objects.get(id = dataRequest['destinatario']),Direccion.objects.get(id = dataRequest['direccion']))
                nuevaFacturaData =  serializador(nuevaFactura, many = False).data
                pedidosArray = []
                serializadorPedido = crearSerializador(Pedido, 0)
                for pedido in dataRequest['pedidos']:
                    pedidoaux = Pedido.__nuevo__(Producto.objects.get(id =pedido["producto"]),nuevaFactura,pedido["cantidad"])
                    pedidosArray.append(serializadorPedido(pedidoaux, many = False).data )
                nuevaFacturaData["pedidos"] = pedidosArray
                return respuesta(nuevaFacturaData)
        except BaseException as err:
            return error(str(err))
        
    def get(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None or not usuario.is_active:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            serializador = crearSerializador(Factura, 0)
            if request.body:
                datosRequest = json.loads(request.body.decode('utf-8'))
                factura = serializador(Factura.objects.filter(Q(id = datosRequest.get('id')), Q(usuario = usuario) | Q(destinatario = usuario) ), many = True).data 
            else: 
                factura = serializador(Factura.objects.filter(Q(usuario = usuario) | Q(destinatario = usuario) ), many = True).data
            return respuesta(factura)
        except BaseException as err:
            return error(str(err))
        
    def put(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None or not usuario.is_active:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            dataRequest = JSONParser().parse(request)
            serializador = crearSerializador(Factura, 0)
            facturaActualizada =  serializador(Factura.__actualizar__(Factura.objects.get(Q(id=dataRequest['id']), Q(usuario = usuario) | Q(destinatario = usuario)  ),dataRequest['mensajeria'],dataRequest['total'],dataRequest['aprobada'],dataRequest['contra_oferta'],dataRequest['impuesto'],Direccion.objects.get(id = dataRequest['direccion'])), many = False).data
            return respuesta(facturaActualizada)
        except BaseException as err:
            return error(str(err))
 
 #por chequear cambios de autorizacion por usuario


@method_decorator(csrf_exempt, name='dispatch')
class GestionarPedido(View):
    
    def post(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            dataRequest = JSONParser().parse(request)
            serializador = crearSerializador(Pedido, 0)
            nuevaPedido =  serializador(Pedido.__nuevo__(Producto.objects.get(id = dataRequest['producto']), Factura.objects.get(id= dataRequest['factura']),dataRequest['cantidad']), many = False).data
            return respuesta(nuevaPedido)
        except BaseException as err:
            return error(str(err))
        
    def get(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            serializador = crearSerializador(Pedido, 0)
            if request.body:
                datosRequest = json.loads(request.body.decode('utf-8'))
                pedido = serializador(Pedido.objects.filter(id = datosRequest.get('id')), many = True).data 
            else: 
                pedido = serializador(Pedido.objects.all(), many = True).data
            return respuesta(pedido)
        except BaseException as err:
            return error(str(err))
        
    def put(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            dataRequest = JSONParser().parse(request)
            serializador = crearSerializador(Pedido, 0)
            pedidoActualizado =  serializador(Pedido.__actualizar__(Pedido.objects.get(id= dataRequest['id']), dataRequest['cantidad']), many = False).data
            return respuesta(pedidoActualizado)
        except BaseException as err:
            return error(str(err))
        
    def delete(self, request):
        try:
            usuario = obtenerUsuario(request)
            if usuario == None:
                return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
            dataRequest = JSONParser().parse(request)
            serializador = crearSerializador(Pedido, 0)
            pedidoInhabilitado =  serializador(Pedido.__inhabilitar__(Pedido.objects.get(id=dataRequest['id'] )), many = False).data
            return respuesta(pedidoInhabilitado)
        except BaseException as err:
            return error(str(err))
          
   
def obtenerCategoria(request):
    try:
        serializador = crearSerializador(Nom_Catergoria, 0)
        categorias = serializador(Nom_Catergoria.objects.all(), many = True).data
        return respuesta(categorias)
    except BaseException as err:
        return error(str(err))
    
@csrf_exempt    
def facturaDetalles(request):
    try:
        usuario = obtenerUsuario(request)
        if usuario == None or not usuario.is_active:
            return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
        dataRequest = JSONParser().parse(request)
        serializador = crearSerializador(Pedido, 0)
        pedidos = serializador(Pedido.objects.filter(factura = Factura.objects.get(Q(id= dataRequest['factura']), Q(usuario = usuario) | Q(destinatario = usuario) )), many = True).data
        return respuesta(pedidos)
    except BaseException as err:
        return error(str(err))   


def productoDetalles(request):
    try:
        serializador = crearSerializador(Producto, 0)
        datosRequest = json.loads(request.body.decode('utf-8'))
        productos = serializador(Producto.objects.filter(id = datosRequest.get('id'), activo =True), many = True).data 
        return respuesta(productos)
    except BaseException as err:
        return error(str(err))


def productosPorCategoria(request):
    try:
        serializador = crearSerializador(Producto, 0)
        datosRequest = json.loads(request.body.decode('utf-8'))
        productos = serializador(Producto.objects.filter(categoria = Nom_Catergoria.objects.get(id = datosRequest.get('categoria')), activo =True), many = True).data 
        return respuesta(productos)
    except BaseException as err:
        return error(str(err))


def productosPorProveedor(request):
    try:
        serializador = crearSerializador(Producto, 0)
        datosRequest = json.loads(request.body.decode('utf-8'))
        productos = serializador(Producto.objects.filter(usuario = Usuario.objects.get(id = datosRequest.get('proveedor')), activo =True), many = True).data 
        return respuesta(productos)
    except BaseException as err:
        return error(str(err))
    
    
def productosPorNombre(request):
    try:
        serializador = crearSerializador(Producto, 0)
        datosRequest = json.loads(request.body.decode('utf-8'))
        productos = serializador(Producto.objects.filter(nombre__icontains = datosRequest.get('nombre'), activo =True), many = True).data 
        return respuesta(productos)
    except BaseException as err:
        return error(str(err))
    

        
    
# def crearDiccionarioAtributos():
#     app_models = [Usuario, Factura, Pedido, Direccion, Producto]

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


# def si(expresionVF, verdadero, falso):
#     if expresionVF:
#         return verdadero
#     return falso

# def obtenerDatosObjetoSerializado(modelo, objeto=None, objetos=None, profundidad=0):
#     return obtenerObjetoSerializado(modelo, objeto=objeto, objetos=objetos, profundidad=profundidad).data

# def obtenerObjetoSerializado(modelo, objeto=None, objetos=None, profundidad=0):
#     many = False
#     if objetos != None:
#         objeto = objetos
#         many = True
#     serializador = crearSerializador(modelo, profundidad)
#     return serializador(instance=objeto, many=many)

# DICCIONARIO_ATRIBUTOS = crearDiccionarioAtributos()

# @csrf_exempt
# def filtro(request):
#     try:
#         diccionarioModelo = [Usuario, Factura, Pedido, Direccion, Producto]
#         datos = JSONParser().parse(request)
#         modeloD = datos['modelo']
#         filtros = datos['filtros']
#         # Validación de modelo
#         modeloL = [m for m in diccionarioModelo if str.lower(m.__name__) == str.lower(modeloD)]
#         if len(modeloL) < 1:
#             return error(f"Modelo ({modeloD}) no reconocido", status.HTTP_404_NOT_FOUND)
#         modelo = modeloL[0]
#         # Validación de filtros
#         filtrosL = [f for f in filtros if f["atributo"] not in [a for a in DICCIONARIO_ATRIBUTOS[modelo]]]
#         if len(filtrosL) > 0:
#             filtrosN = [f["atributo"] for f in filtrosL]
#             plural = si(len(filtrosN) > 1, "s", "")
#             return error(f"Filtro{plural} ({str(filtrosN)}) no reconocido{plural} para el modelo ({modeloD})", status.HTTP_404_NOT_FOUND)
#         objetos = obtenerDatosObjetoSerializado(
#         modelo, objetos=modelo.objects.all())
#         lista = []
#         for objeto in objetos:
#             for filtro in filtros:
#                 if str(objeto[filtro["atributo"]]) == str(filtro["valor"]):
#                     lista.append(objeto)
#         return respuesta(lista)
#     except BaseException as err:
#         return respuesta(str(err))
    
# @csrf_exempt
# def filtroUnico(request):
#     try:
#         x = "activo"
#         z = False
#         serializador = crearSerializador(Producto, 0)
#         categorias = serializador(Producto.objects.filter(Q((x,z))), many = True).data
#         diccionarioModelo = [Usuario, Factura, Pedido, Direccion, Producto]
#         datos = JSONParser().parse(request)
#         modeloD = datos['modelo']
#         filtros = datos['filtros']
#         # Validación de modelo
#         modeloL = [m for m in diccionarioModelo if str.lower(m.__name__) == str.lower(modeloD)]
#         if len(modeloL) < 1:
#             return error(f"Modelo ({modeloD}) no reconocido", status.HTTP_404_NOT_FOUND)
#         modelo = modeloL[0]
#         # Validación de filtros
#         filtrosL = [f for f in filtros if f["atributo"] not in [a for a in DICCIONARIO_ATRIBUTOS[modelo]]]
#         if len(filtrosL) > 0:
#             filtrosN = [f["atributo"] for f in filtrosL]
#             plural = si(len(filtrosN) > 1, "s", "")
#             return error(f"Filtro{plural} ({str(filtrosN)}) no reconocido{plural} para el modelo ({modeloD})", status.HTTP_404_NOT_FOUND)
#         objetos = obtenerDatosObjetoSerializado(
#         modelo, objetos=modelo.objects.all())
#         lista = []
#         for objeto in objetos:
#             for filtro in filtros:
#                 if str(objeto[filtro["atributo"]]) == str(filtro["valor"]):
#                     lista.append(objeto)
#         return respuesta(lista)
#     except BaseException as err:
#         return respuesta(str(err))
    
    
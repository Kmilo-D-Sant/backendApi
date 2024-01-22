# from asyncio.windows_events import NULL
# from ctypes import Array
# from datetime import date, datetime
# import os
# from typing import List
# from django.apps import apps
# from email.headerregistry import Group
# from inspect import Parameter
from django.http.response import JsonResponse
#from rest_framework.parsers import JSONParser
from rest_framework import serializers, status
#from django.contrib.auth.models import User, Permission, Group
from rest_framework.authtoken.models import Token
# from .admin import  DICCIONARIO_ATRIBUTOS
from .models import *
#from django.contrib.admin.models import LogEntry
#import time
#from django.core import mail
#from django.conf import settings
#from django.db.models.signals import post_save
#from django.dispatch import receiver
#from django.conf import settings
from django.contrib.auth import get_user_model
import io
import base64
from PIL import Image
 


CHECK_ERROR = "error"
CHECK_DATOS = "datos"
CHECK_NO_EXISTE = "DoesNotExist"
CHECK_PARSE_ERROR = "ParseError"
CHECK_KEY_ERROR = "KeyError"
CHECK_TYPE_ERROR = "TypeError"
CHECK_VALIDATION_ERROR = "ValidationError"

MENSAJE_NO_EXISTE_R = "No existe el elemento solicitado"
MENSAJE_NO_EXISTE_M = "No existe el modelo solicitado"
MENSAJE_NO_CUMPLE_REQUISITOS_ESTABLECIDOS = "Los datos no cumplen con los requisitos establecidos"
MENSAJE_USUARIO_NO_AUTENTICADO = "Usuario no autenticado"
MENSAJE_USUARIO_NO_AUTORIZADO = "Usuario no autorizado"
MENSAJE_PARAMETRO_NO_VALIDO = "Parámetro no válido"
MENSAJE_AUTENTICACION_NO_VALIDA = "Usuario o contraseña incorrecta"
MENSAJE_OK = "Acción completada correctamente"
MENSAJE_ARCHIVO_NO_VALIDO = "Archivo no válido"
        

# def mes(id):
#     try:
#         meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
#                  7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
#         return meses[int(id)]
#     except:
#         return ""


# def dia(id):
#     try:
#         dias = {
#             1: "Domingo",
#             2: "Lunes",
#             3: "Martes",
#             4: "Miércoles",
#             5: "Jueves",
#             6: "Viernes",
#             7: "Sábado",
#         }
#         return dias[int(id % 7)]
#     except:
#         return ""


# def compara(a: str, b: str):
#     return str.lower(a) == str.lower(b)


# def completarConCeros(texto):
#     return f"{texto:6}".replace(" ", "0")


# def generaNombreArchivoRespaldo():
#     return f"Respaldo_{fechaHoraFormato(time.localtime())}.bkp"


# def archivoRespaldo(archivo):
#     try:
#         aux = archivo.replace("Respaldo_", "").replace(".bkp", "")
#         tiempo = formatoFechaHora(aux)
#         return {
#             "archivo": archivo,
#             "fecha": fecha(tiempo),
#             "fecha_larga": fechaHoraLarga(tiempo),
#             "hora": hora(tiempo),
#             "dia": tiempo.tm_mday,
#             "dia_semana": dia(tiempo.tm_wday),
#             "mes": tiempo.tm_mon,
#             "mes_nombre": mes(tiempo.tm_mon),
#             "año": tiempo.tm_year
#         }
#     except:
#         return {}


# def formatoFechaHora(tiempo: str):
#     return time.strptime(tiempo, '%Y-%m-%d_%H-%M-%S')


# def fechaHoraFormato(tiempo: time.struct_time):
#     return time.strftime('%Y-%m-%d_%H-%M-%S', tiempo)


# def fechaDMY(fecha: date):
#     return fecha.strftime("%d/%m/%Y")


# def fechaYMD(fecha: date):
#     return fecha.strftime("%Y-%m-%d")


# def fecha(tiempo: time.struct_time):
#     return time.strftime('%d/%m/%Y', tiempo)


# def hora(tiempo: time.struct_time):
#     return time.strftime('%I:%M:%S %p', tiempo)


# def hora24(tiempo: time.struct_time):
#     return time.strftime('%H:%M:%S', tiempo)


# def fechaHora(tiempo: time.struct_time):
#     return time.strftime('%d/%m/%Y %I:%M:%S %p', tiempo)


# def fechaHora24H(tiempo: time.struct_time):
#     return time.strftime('%d/%m/%Y %H:%M:%S', tiempo)


# def fechaLarga(tiempo: time.struct_time):
#     return f"{dia(tiempo.tm_wday)}, {tiempo.tm_mday} de {mes(tiempo.tm_mon)} de {tiempo.tm_year}"


# def fechaHoraLarga(tiempo: time.struct_time):
#     return f"{dia(tiempo.tm_wday)}, {tiempo.tm_mday} de {mes(tiempo.tm_mon)} de {tiempo.tm_year}. {time.strftime('%I:%M:%S %p',tiempo)}"


# def fechaHoraLarga24H(tiempo: time.struct_time):
#     return f"{dia(tiempo.tm_wday)}, {tiempo.tm_mday} de {mes(tiempo.tm_mon)} de {tiempo.tm_year}. {time.strftime('%H:%M:%S',tiempo)}"


# def isEmpty(objeto):
#     return objeto == None or objeto == "" or (type(objeto) in [Array, List, Str] and len(objeto) < 1),


# def ifEmptyGet(objeto, valor):
#     if isEmpty(objeto):
#         return valor
#     return objeto


# def ifDo(expresion, siTrue, siFalse):
#     if expresion:
#         siTrue
#     return siFalse


# def rellenar(texto, longitud=20, caracter="_"):
#     # print("<rellenar>")
#     # print(" ifEmptyGet '",ifEmptyGet(str(texto), ""),"'",replace(str(texto)," ",""))
#     # s = ifEmptyGet(str(texto), "")
#     if isEmpty(texto):
#         return "".ljust(longitud,caracter)
#     s = str(texto)
#     l = round(longitud-len(s)/2)
#     print(" parametros", texto, len(s), longitud, l)
#     return s.ljust(l, caracter).rjust(l, caracter)


# def unir(list, separador=" "):
#     return str.join(separador, list)


# def si(expresionVF, verdadero, falso):
#     if expresionVF:
#         return verdadero
#     return falso


# def estaVacio(valor, reemplazo=""):
#     if valor == None:
#         return reemplazo
#     return valor


# def enviarCorreo(asunto, mensaje, destinatario):
#     return enviarCorreoMutiple(asunto, mensaje, [destinatario])


# def enviarCorreoMutiple(asunto, mensaje, listaDestinatario, usuarioId):
#     print("<enviarCorreo inicio>")
#     print("asunto", asunto, "mensaje", mensaje,
#           "listaDestinatario", len(listaDestinatario))
#     listaDestinatario = ["pepe@as.com", "asdd@s.com"]
#     try:
#         conexion = mail.get_connection()
#         email = mail.EmailMessage(
#             subject=asunto,
#             body=mensaje,
#             from_email=settings.EMAIL_HOST_USER,
#             to=listaDestinatario,
#             connection=conexion
#         )
#         conexion.open()
#         email.send(False)
#         conexion.close()

#         correo_enviado = {
#             "Remitente": email.from_email,
#             "Destinatario": email.to,
#             "Asunto": email.subject,
#             "Mensaje": email.body,
#         }
#         return respuesta({"correo enviado": correo_enviado})
#     except BaseException as error:
#         crearTraza( NULL, 'Error al enviar el correo ' + error, usuarioId)
#         return manipularError(error)
#     finally:
#         print("<enviarCorreo fin>")


# def generarConsecutivo():
#     return int(datetime.datetime.now().timestamp()/1000).__trunc__()


# # def crearNotificacion(modelo, objetoId, correoRol, usuario, descripcion):
# #     print("<crearNotificacion inicio>")
# #     usuariosAux = User.objects.all()
# #     objeto = obtenerObjeto(modelo, objetoId)
# #     if descripcion == None:
# #         descripcion = f"Nuevo elemento creado. {modelo.__name__}: {objeto.__str__()}"
# #     listaCorreos = []

# #     if correoRol == "Comercial":
# #         for usuario in usuariosAux:
# #             rol = obtenerRolUsuario(usuario)
# #             if rol == "Director" or rol == "Jefe dpto comercial":
# #                 if usuario.email != None:
# #                     listaCorreos.append(usuario.email)

# #     if correoRol == "Metrologia":
# #         for usuario in usuariosAux:
# #             rol = obtenerRolUsuario(usuario)
# #             if rol == "Director" or rol == "Jefe dpto metrología":
# #                 if usuario.email != None:
# #                     listaCorreos.append(usuario.email)

# #     if correoRol == "Normalizacion":
# #         for usuario in usuariosAux:
# #             rol = obtenerRolUsuario(usuario)
# #             if rol == "Director" or rol == "Jefe dpto normalización":
# #                 if usuario.email != None:
# #                     listaCorreos.append(usuario.email)

# #     if correoRol == "Comercial-Normalizacion":
# #         for usuario in usuariosAux:
# #             rol = obtenerRolUsuario(usuario)
# #             if rol == "Director" or rol == "Jefe dpto normalización" or rol == "Jefe dpto comercial":
# #                 if usuario.email != None:
# #                     listaCorreos.append(usuario.email)

# #     if correoRol == "Metrologia-Normalizacion":
# #         for usuario in usuariosAux:
# #             rol = obtenerRolUsuario(usuario)
# #             if rol == "Director" or rol == "Jefe dpto metrología" or rol == "Jefe dpto normalización":
# #                 if usuario.email != None:
# #                     listaCorreos.append(usuario.email)

# #     try:
# #         objeto = Notificacion.objects.get(descripcion=descripcion)
# #         if objeto != None:
# #             crearTraza(objeto.id, descripcion, usuario.id, modelo)
# #     except:
# #         if type(modelo) != str:
# #             modelo = modelo.__name__
# #         notificacion: Notificacion = {
# #             "modelo": modelo,
# #             "objetoId": objetoId,
# #             "descripcion": descripcion
# #         }
# #         serializer = serializarObjeto(Notificacion, notificacion)
# #         if serializer.is_valid(raise_exception=True):
# #             serializer.save()
# #         if correoRol != None:
# #             enviarCorreoMutiple(modelo, descripcion, listaCorreos, usuario.id)
# #         crearTraza(objetoId, descripcion, usuario.id, modelo)
# #     finally:
# #         print("<crearNotificacion fin>")


# def strToInt(cadena: str):
#     try:
#         if cadena == None or cadena == "":
#             return 0
#         i = int(cadena)
#         return i
#     except:
#         return -1


def error(mensaje: str, estado=status.HTTP_400_BAD_REQUEST):
    return JsonResponse({"error": mensaje}, status=estado)


# def errorMetodoNoPermitido(metodo):
#     return error(f"Método no permitido ({metodo})", status.HTTP_405_METHOD_NOT_ALLOWED)


def respuesta(datos, estado=status.HTTP_200_OK):
    return JsonResponse({"datos": datos}, status=estado)


def manipularError(err):
    strTypeError = str(type(err))
    strError = str(err)
    msg = f"{strTypeError} {strError}"
    print("<manipularError>", msg)
    try:
        if strTypeError.__contains__(CHECK_NO_EXISTE):
            return error(MENSAJE_NO_EXISTE_R, status.HTTP_404_NOT_FOUND)
        elif strTypeError.__contains__(CHECK_PARSE_ERROR):
            return error(MENSAJE_NO_CUMPLE_REQUISITOS_ESTABLECIDOS, status.HTTP_406_NOT_ACCEPTABLE)
        elif strTypeError.__contains__(CHECK_KEY_ERROR):
            return error(f'{MENSAJE_PARAMETRO_NO_VALIDO} ({strError})', status.HTTP_406_NOT_ACCEPTABLE)
        elif strTypeError.__contains__(CHECK_TYPE_ERROR):
            if strError.find(': ', 0) != -1:
                p = strError.index(': ')
                if p >= 0:
                    strError = strError[p+2:]
            return error(f'{MENSAJE_PARAMETRO_NO_VALIDO} ({strError})', status.HTTP_406_NOT_ACCEPTABLE)
        elif strTypeError.__contains__(CHECK_VALIDATION_ERROR):
            return error(f'{MENSAJE_PARAMETRO_NO_VALIDO} ({strError})', status.HTTP_406_NOT_ACCEPTABLE)
        return error(msg)
    except BaseException as otroError:
        return error(f"{str(type(otroError))} {str(otroError)}")


# def obtenerRol(request):
#     print("<Obtener Rol inicio>")
#     usuario = obtenerUsuario(request)
#     serializer = obtenerDatosObjetoSerializado(User, usuario)
#     grupos = serializer["groups"]
#     if grupos == []:
#         if serializer["is_superuser"]:
#             return "admin"
#     rol = Group.objects.get(id=grupos[0])
#     print("<Obtener Rol fin>")
#     return rol


# def obtenerRolUsuario(usuario):
#     print("<Obtener Rol inicio>")
#     serializer = obtenerDatosObjetoSerializado(User, usuario)
#     grupos = serializer["groups"]
#     if grupos == []:
#         if serializer["is_superuser"]:
#             return "admin"
#     rol = str(Group.objects.get(id=grupos[0]))
#     print("<Obtener Rol fin>")
#     return rol


# # def tienePermiso(request, modelo, usuario, idAux):
# #     print("<Tiene Permiso inicio>")
# #     operacion = ""
# #     if request.method == 'GET':
# #         operacion = "view"
# #     elif request.method == 'PUT':
# #         operacion = "change"
# #     elif request.method == 'POST':
# #         operacion = "add"
# #     elif request.method == 'DELETE':
# #         operacion = "delete"
# #     if modelo == 'logentry':
# #         permiso = f'admin.{operacion}_{modelo}'
# #     elif modelo == 'user' or modelo == 'permission' or modelo == 'group':
# #         permiso = f'auth.{operacion}_{modelo}'
# #     else:
# #         permiso = f'Api.{operacion}_{modelo}'
# #     tienePermiso = usuario.has_perm(permiso)
# #     if tienePermiso:
# #         if request.method == 'PUT' or request.method == 'DELETE':
# #             if not permisoRolEstado(request, modelo, idAux):
# #                 tienePermiso = False
# #     print("<Tiene Permiso inicio>")
# #     return tienePermiso


# def traductor(cadena: str):
#     if not cadena.find("view_", 0) == -1:
#         aux = cadena.replace('view_', 'ver_')
#     if not cadena.find("add_", 0) == -1:
#         aux = cadena.replace('add_', 'adicionar_')
#     if not cadena.find("delete_", 0) == -1:
#         aux = cadena.replace('delete_', 'eliminar_')
#     if not cadena.find("change_", 0) == -1:
#         aux = cadena.replace('change_', 'editar_')
#     return aux


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)    

from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        
def Base64Aimagen(data):
    try:
        data = base64.b64decode(data.encode('UTF-8'))
        buf = io.BytesIO(data)
        img = Image.open(buf)
        return img
    except:
        return None

# def imagenAbase64(image_file, format='png'):
    
#     if not os.path.isfile(image_file):
#         return None
    
#     encoded_string = ''
#     with open(image_file, 'rb') as img_f:
#         encoded_string = base64.b64encode(img_f.read())
#     return 'data:image/%s;base64,%s' % (format, encoded_string)


def extraerToken(request):
    try:
        tokenKey = str(request.META["HTTP_AUTHORIZATION"])
        if not tokenKey.find('Bearer ', 0) == -1:
            p = tokenKey.index('Bearer ')
            tokenKey = tokenKey[p+7:]
        if not tokenKey.find('Token ', 0) == -1:
            p = tokenKey.index('Token ')
            tokenKey = tokenKey[p+6:]
        return tokenKey
    except:
        return None


def obtenerObjetoSerializado(modelo, objeto=None, objetos=None, profundidad=0):
    many = False
    if objetos != None:
        objeto = objetos
        many = True
    serializador = crearSerializador(modelo, profundidad)
    return serializador(instance=objeto, many=many)


# def serializarObjeto(modelo, objeto, profundidad=0):
#     serializador = crearSerializador(modelo, profundidad)
#     return serializador(data=objeto)


# def obtenerDatosObjetoSerializado(modelo, objeto=None, objetos=None, profundidad=0):
#     return obtenerObjetoSerializado(modelo, objeto=objeto, objetos=objetos, profundidad=profundidad).data


def obtenerUsuario(request):
    tokenKey = extraerToken(request)
    try:
        token = Token.objects.get(key=tokenKey)
    except:
        return None
    return obtenerObjeto(get_user_model(), token.user_id)


# def obtenerModeloPorNombre(nombreModelo):
#     # print("<obtenerModeloPorNombre fin>")
#     try:
#         nombre = nombreModelo.lower()
#         app_models = apps.get_app_config('Api').get_models()
#         for model in app_models:
#             if nombre == model.__name__.lower():
#                 return model
#         # for model in [User, Group, LogEntry, Permission, ]:
#         #     if nombre == model.__name__.lower():
#                 return model
#         return None
#     except BaseException as err:
#         manipularError(err)
#     # finally:
#         # print("<obtenerModeloPorNombre fin>")


def obtenerObjeto(modelo, objetoId):
    try:
        return modelo.objects.get(id=objetoId)
    except BaseException as err:
        manipularError(err)
        return None


# def obtenerObjetoPorCampo(modelo, campo, valor):
#     try:
#         objetos = modelo.objects.all()
#         for objeto in objetos:
#             data = obtenerDatosObjetoSerializado(modelo, objeto)
#             if data[f"{campo}"] == valor:
#                 return objeto
#     except:
#         return None


# def traducirEstado(estadoNumerico):
#     if estadoNumerico == -1:
#         estadoString = "Vencido"
#     if estadoNumerico == 0:
#         estadoString = "Creado"
#     if estadoNumerico == 1:
#         estadoString = "Revisado"
#     if estadoNumerico == 2:
#         estadoString = "Aprobado"
#     if estadoNumerico == 3:
#         estadoString = "Culminado"
#     return estadoString

# # def cumpleRequisitosSeguridad(request, modelo, idAux):
# #     print("<cumpleResquisitosSeguridad>")
# #     usuario = obtenerUsuario(request)
# #     if usuario == None:
# #         return error(MENSAJE_USUARIO_NO_AUTENTICADO, status.HTTP_403_FORBIDDEN)
# #     if not usuario.is_superuser:
# #         if (type(modelo) != str):
# #             model = modelo.__name__
# #         else:
# #             model = modelo
# #         if not tienePermiso(request, model.lower(), usuario, idAux):
# #             return error(MENSAJE_USUARIO_NO_AUTORIZADO, status.HTTP_401_UNAUTHORIZED)
# #     return respuesta(f"El usuario {usuario.username} tiene permiso al modelo {modelo}")


def crearSerializador(modelo, profundidad=0):
    class serializador(serializers.ModelSerializer):
        class Meta:
            model = modelo
            fields = '__all__'
            depth = profundidad

    return serializador


# def cumpleAtributosRequeridos(serializer, datos):
#     if datos["tipoCliente"] == "Persona natural":
#         diccRequeridos = {
#             'apellido1': datos["apellido1"],
#             'apellido2': datos["apellido2"],
#             'ci': datos["ci"],
#             'telefono': datos["telefono"],
#             'Sector_Economico': datos["Sector_Economico"]
#         }
#     else:
#         diccRequeridos = {
#             'direccion': datos["direccion"],
#             'codigoReuup': datos["codigoReuup"],
#             'Organismo': datos["Organismo"]
#         }
#     for key in diccRequeridos:
#         if diccRequeridos[key] == None or diccRequeridos[key].strip() == "":
#             return error(f"El campo {key} no puede estar vacio", status.HTTP_406_NOT_ACCEPTABLE)

#     return respuesta('Los datos cumplen con los requisitos')


# def obtenerModeloPorUrl(request):
#     urlAux = request.META["PATH_INFO"][1:]
#     try:
#         url = urlAux[: urlAux.index("/")]
#     except:
#         url = urlAux
#     return DICCIONARIO_MODELOS[url]


# def procesarUrl(request, idAux):
#     try:
#         modelo = obtenerModeloPorUrl(request)
#         return gestionarElementos(request, modelo, idAux)
#     except BaseException as err:
#         return manipularError(err)


# def filtrarUsuario(usuario):
#     for item in ["password", "user_permissions"]:
#         usuario.pop(item)
#     if len(usuario['groups']) > 0:
#         for grupo in usuario['groups']:
#             filtrarGrupo(grupo)


# def filtrarGrupo(grupo):
#     grupo.pop('permissions')


# # def filtrarElementos(request):
# #     try:
# #         datos = JSONParser().parse(request)
# #         modelo = datos['modelo']
# #         filtros = datos['filtros']

# #         for key in DICCIONARIO_ATRIBUTOS:
# #             if str(key.__name__) == modelo:
# #                 modelo = key

# #         lista = []
# #         objetos = modelo.objects.all()
        
# #         serializador = crearSerializador(modelo, 1)
# #         serializer = serializador(objetos, many=True)
# #         for objeto in serializer.data:
# #             count = 0
# #             for filtro in filtros:
# #                 print(filtros)
# #                 print("pepe objeto  " + str(objeto[filtro["atributo"]]) )
# #                 print("pepe filtro" + str(filtro["valor"]))
# #                 if (str(objeto[filtro["atributo"]]) == str(filtro["valor"])):
# #                     count += 1
# #             if count == len(filtros):
# #                 lista.append(objeto)
# #         serializer = serializador(lista, many=True)
# #         return respuesta(serializer.data)
# #     except BaseException as err:
# #         return manipularError(err)


# def filtrarElementos(request):
#     try:
#         diccionarioModelo = [Usuario, Factura, Pedido, Direccion, Producto]
#         datos = JSONParser().parse(request)
#         print(str(diccionarioModelo))
#         modeloD = datos['modelo']
#         filtros = datos['filtros']
#         # Validación de modelo
#         modeloL = [m for m in diccionarioModelo if compara(
#             m.__name__, modeloD)]
#         if len(modeloL) < 1:
#             return error(f"Modelo ({modeloD}) no reconocido", status.HTTP_404_NOT_FOUND)
#         modelo = modeloL[0]
#         # Validación de filtros
#         filtrosL = [f for f in filtros if f["atributo"]
#                     not in [a for a in diccionarioModelo[modelo]]]
#         if len(filtrosL) > 0:
#             filtrosN = [f["atributo"] for f in filtrosL]
#             plural = si(len(filtrosN) > 1, "s", "")
#             return error(f"Filtro{plural} ({str(filtrosN)}) no reconocido{plural} para el modelo ({modeloD})", status.HTTP_404_NOT_FOUND)
#         objetos = obtenerDatosObjetoSerializado(
#             modelo, objetos=modelo.objects.all())
#         lista = []
#         for objeto in objetos:
#             for filtro in filtros:
#                 if str(objeto[filtro["atributo"]]) == str(filtro["valor"]):
#                     lista.append(objeto)
#         return respuesta(lista)
#     except BaseException as err:
#         return manipularError(err)


# def gestionarElementos(request: Parameter, modelo: object, idAux: str):
#     print("<gestionarElementos>")
#     try:
#         # Desactivada la seguridad hasta que terminemos de desarrollar
#         # resp = cumpleRequisitosSeguridad(request, modelo, idAux)
#         # if resp.status_code != status.HTTP_200_OK:
#         #     return resp

#         id = strToInt(idAux)
#         if id < 0:
#             return error(MENSAJE_PARAMETRO_NO_VALIDO, status.HTTP_406_NOT_ACCEPTABLE)

#         if request.method == 'GET':
#             print(modelo)
#             if modelo == Group:
#                 profundidad = 0
#             else:
#                 profundidad = 1
#             serializador = crearSerializador(modelo, profundidad)
#             if id == 0:
#                 if modelo == User:
#                     objetos = modelo.objects.filter(is_active=True)
#                 # elif modelo == LogEntry or modelo == Group:
#                 #     objetos = modelo.objects.all()
#                 # else:
#                     objetos = modelo.objects.filter(deshabilitado=False)
#                 datos = serializador(objetos, many=True).data
#                 if modelo == Permission:
#                     for permiso in datos:
#                         permiso["codename"] = traductor(permiso["codename"])
#                     return respuesta(datos)
#                 elif modelo == User:
#                     for dict in datos:
#                         filtrarUsuario(dict)
#                 elif modelo == Group:
#                     for dict in datos:
#                         filtrarGrupo(dict)
#                 return respuesta(datos)
#             else:
#                 objeto = modelo.objects.get(id=id)
#                 datos = serializador(objeto).data
#                 if modelo == User:
#                     filtrarUsuario(datos)
#                 elif modelo == Group:
#                     filtrarGrupo(datos)
#                 return respuesta(datos)

#         serializador = crearSerializador(modelo)

#         if request.method == 'PUT':
#             objeto = modelo.objects.get(id=id)
#             datos = JSONParser().parse(request)
#             userChangeWithoutPass = False
#             if modelo == User and datos.get("password") == None:
#                 datos["password"] = objeto.password
#                 userChangeWithoutPass = True
#             serializer = serializador(objeto, data=datos)
#             if serializer.is_valid(raise_exception=True):
#                 # if modelo == Curso or modelo == Capacitacion or modelo == Cliente or modelo == OrdenTrabajo or modelo == Verificacion:
#                 #     objeto = serializer.save()
#                 #     crearReferencias(datos, objeto.id, modelo)
#                 #     data = serializer.data
#                 #     # data[ModalidadCurso.__name__]=listModalidades
#                 #     return respuesta(data, status.HTTP_201_CREATED)
#                 # if modelo == Cliente:
#                 #     resp = cumpleAtributosRequeridos(serializer,datos)
#                 #     if resp.status_code != status.HTTP_200_OK:
#                 #         return resp
#                 objeto = serializer.save()
#                 if modelo == User and not userChangeWithoutPass:
#                     objeto = serializer.save()
#                     objeto.set_password(objeto.password)
#                     objeto.save()
#                 return respuesta(serializer.data, status.HTTP_202_ACCEPTED)

#         if request.method == 'POST':
#             datos = JSONParser().parse(request)
#             for atributo in datos.items():
#                 if atributo[0] == "fecha" and atributo[1] == None:
#                     fecha = fechaYMD(datetime.datetime.now())
#                     datos["fecha"] = fecha
#             serializer = serializador(data=datos)
#             usuario = obtenerUsuario(request)
#             if serializer.is_valid(raise_exception=True):
#                 # if modelo == Curso or modelo == Cliente or modelo == Capacitacion or modelo == OrdenTrabajo or modelo == Verificacion:
#                 #     objeto = serializer.save()
#                 #     crearReferencias(datos, objeto.id, modelo)
#                 #     data = serializer.data
#                 #     print(data)
#                 #     if modelo == Contrato or modelo == VentaNorma or modelo == Verificacion or modelo == OrdenTrabajo or modelo == LevNorma or modelo == Capacitacion or modelo == Curso or modelo == Diagnostico:
#                 #         if modelo == Contrato or modelo == VentaNorma:
#                 #             correoRol = "Comercial"
#                 #         elif modelo == Verificacion or modelo == OrdenTrabajo:
#                 #             correoRol = "Metrologia"
#                 #         elif modelo == LevNorma:
#                 #             correoRol = "Normalizacion"
#                 #         elif modelo == Capacitacion or modelo == Curso:
#                 #             correoRol = "Comercial-Normalizacion"
#                 #         else:
#                 #             correoRol = "Metrologia-Normalizacion"
#                 #         crearNotificacion(modelo, objeto.id,
#                 #                           correoRol, usuario, None)
#                 #     return respuesta(data, status.HTTP_201_CREATED)
#                 # objeto = serializer.save()
#                 # if modelo == Contrato or modelo == VentaNorma or modelo == Verificacion or modelo == OrdenTrabajo or modelo == LevNorma or modelo == Capacitacion or modelo == Curso or modelo == Diagnostico:
#                 #     if modelo == Contrato or modelo == VentaNorma:
#                 #         correoRol = "Comercial"
#                 #     elif modelo == Verificacion or modelo == OrdenTrabajo:
#                 #         correoRol = "Metrologia"
#                 #     elif modelo == LevNorma:
#                 #         correoRol = "Normalizacion"
#                 #     elif modelo == Capacitacion or modelo == Curso:
#                 #         correoRol = "Comercial-Normalizacion"
#                 #     else:
#                 #         correoRol = "Metrologia-Normalizacion"
#                 #     crearNotificacion(modelo, objeto.id,
#                 #                       correoRol, usuario, None)

#                 if modelo == User:
#                     objeto.set_password(objeto.password)
#                     objeto.save()
#                 return respuesta(serializer.data, status.HTTP_201_CREATED)

#         if request.method == 'DELETE':
#             objeto = modelo.objects.get(id=id)
#             if (modelo == User):
#                 objeto.is_active = False
#             else:
#                 objeto.deshabilitado = True
#             objeto.save()
#             serializer = serializador(objeto)
#             # objeto.delete()
#             return respuesta(serializer.data, status.HTTP_202_ACCEPTED)

#         return error(MENSAJE_NO_CUMPLE_REQUISITOS_ESTABLECIDOS, status.HTTP_406_NOT_ACCEPTABLE)

#     except BaseException as err:
#         return manipularError(err)


# # def crearReferencias(datos, idContenedor, modelo):
# #     print("<Crear referencias>, modelo: ", modelo)
# #     if modelo == Curso:
# #         modeloReferencia = ModalidadCurso
# #         objetos = modeloReferencia.objects.all()
# #         for objeto in objetos:
# #             if objeto.Curso.id == idContenedor:
# #                 objeto.delete()
# #     elif modelo == Capacitacion:
# #         modeloReferencia = ListaEstudiantes
# #         objetos = modeloReferencia.objects.all()
# #         for objeto in objetos:
# #             if objeto.Capacitacion.id == idContenedor:
# #                 objeto.delete()
# #     elif modelo == Cliente:
# #         modeloReferencia = ListaPersonal
# #         objetos = modeloReferencia.objects.all()
# #         for objeto in objetos:
# #             if objeto.Cliente.id == idContenedor:
# #                 objeto.delete()
# #     # elif modelo == Verificacion:
# #     #     modeloReferencia = ListaInstrumentos
# #     #     objetos = modeloReferencia.objects.all()
# #     #     for objeto in objetos:
# #     #         if objeto.Verificacion.id == idContenedor:
# #     #             objeto.delete()
# #     else:
# #         modeloReferencia = InstrumentoOrdenTrabajo
# #         objetos = modeloReferencia.objects.all()
# #         for objeto in objetos:
# #             if objeto.OrdenTrabajo.id == idContenedor:
# #                 objeto.delete()

# #     if datos[modeloReferencia.__name__] == None:
# #         listaIdElementos = []
# #     else:
# #         listaIdElementos = datos[modeloReferencia.__name__]
# #     listModalidades = []

# #     serializador = crearSerializador(modeloReferencia)
# #     for idElemento in listaIdElementos:
# #         if modelo == Curso:
# #             objeto = {
# #                 Curso.__name__: idContenedor,
# #                 Modalidad.__name__: idElemento,
# #             }
# #         elif modelo == Capacitacion:
# #             objeto = {
# #                 Capacitacion.__name__: idContenedor,
# #                 Estudiante.__name__: idElemento,
# #             }
# #         elif modelo == Verificacion:
# #             objeto = {
# #                 Verificacion.__name__: idContenedor,
# #                 Instrumento.__name__: idElemento,
# #             }
# #         elif modelo == Cliente:
# #             print("asd")
# #             objeto = {
# #                 Cliente.__name__: idContenedor,
# #                 PersonalEntidad.__name__: idElemento,
# #             }
# #             print(objeto)
# #         elif modelo == OrdenTrabajo:
# #             objeto = {
# #                 OrdenTrabajo.__name__: idContenedor,
# #                 Instrumento.__name__: idElemento,
# #             }
# #         serializer = serializador(data=objeto)
# #         if serializer.is_valid(raise_exception=True):
# #             serializer.save()
# #             listModalidades.append(idElemento)
# #     return listModalidades


# # def eliminarReferencias(objeto, modelo):
# #     print("<Eliminar referencias>, modelo: ", modelo)
# #     if modelo == Curso:
# #         modeloReferencia = ModalidadCurso
# #     elif modelo == Capacitacion:
# #         modeloReferencia = ListaEstudiantes
# #     elif modelo == Cliente:
# #         modeloReferencia = ListaPersonal
# #     # elif modelo == Verificacion:
# #     #     modeloReferencia = ListaInstrumentos
# #     elif modelo == OrdenTrabajo:
# #         modeloReferencia = InstrumentoOrdenTrabajo
# #     objetos = modeloReferencia.objects.all()
# #     for objeto in objetos:
# #         if objeto[modelo.__name__].id == objeto.id:
# #             objeto.delete()


# # def obtenerNorma(request):
# #     print("<obtenerNorma>")
# #     try:
# #         # Desactivada la seguridad hasta que terminemos de desarrollar
# #         resp = cumpleRequisitosSeguridad(request, Norma, None)
# #         if resp.status_code != status.HTTP_200_OK:
# #             return resp
# #         if request.method == 'GET':
# #             serializador = crearSerializador(Norma, 1)
# #             objetos = Norma.objects.exclude(tipoNorma=2)
# #             datos = serializador(objetos, many=True).data
# #             return respuesta(datos)
# #         else:
# #             return errorMetodoNoPermitido(request.method)
# #     except BaseException as err:
# #         return manipularError(err)


# # def obtenerPorRango(request):
# #     print("<obtenerPorRango>")
# #     try:
# #         if request.method == 'POST':
# #             datos = JSONParser().parse(request)
# #             modeloAux = datos["modelo"]

# #             resp = cumpleRequisitosSeguridad(request, modeloAux, None)
# #             if resp.status_code != status.HTTP_200_OK:
# #                 return resp

# #             rangoInicio = datos["rangoInicio"]
# #             rangoFin = datos["rangoFin"]

# #             modelo = obtenerModeloPorNombre(modeloAux)
# #             if rangoInicio != None and rangoFin != None:
# #                 objetos = modelo.objects.all()[rangoInicio:rangoFin]
# #             elif rangoInicio == None and rangoFin == None:
# #                 objetos = modelo.objects.all()
# #             elif rangoInicio == None:
# #                 objetos = modelo.objects.all()[:rangoFin]
# #             else:
# #                 objetos = modelo.objects.all()[rangoInicio:]

# #             serializador = crearSerializador(modelo)
# #             datos = serializador(objetos, many=True).data

# #             if objetos.count() == 0:
# #                 datos = []
# #             else:
# #                 datos = serializador(objetos, many=True).data
# #             return respuesta(datos)
# #         else:
# #             return errorMetodoNoPermitido(request.method)
# #     except BaseException as err:
# #         return manipularError(err)


# # def obtenerConsecutivo(request):
# #     print("<obtenerConsecutivo>")
# #     try:
# #         if request.method == 'POST':
# #             datos = JSONParser().parse(request)
# #             modeloAux = datos["modelo"]

# #             resp = cumpleRequisitosSeguridad(request, modeloAux, None)
# #             if resp.status_code != status.HTTP_200_OK:
# #                 return resp

# #             modelo = obtenerModeloPorNombre(modeloAux)

# #             objetos = modelo.objects.aggregate()

# #             serializador = crearSerializador(modelo)
# #             datos = serializador(objetos, many=True).data

# #             if objetos.count() == 0:
# #                 datos = []
# #             else:
# #                 datos = serializador(objetos, many=True).data
# #             return respuesta(datos)
# #         else:
# #             return errorMetodoNoPermitido(request.method)
# #     except BaseException as err:
# #         return manipularError(err)


# def crearTraza(objetoId, descripcion, usuarioId, mensaje="[{\"added\": {}}]", modelo=None):
#     print("<Crear traza inicio>")
#     try:
#         if len(descripcion) > 200:
#             descripcion = descripcion.ljust(200)
#         contenido = modelo
#         # traza: LogEntry = {
#         #     "action_time": time.ctime(),
#         #     "object_id": objetoId,
#         #     "object_repr": descripcion,
#         #     "action_flag": 1,
#         #     "change_message": mensaje,
#         #     "user": usuarioId,
#         #     "content_type": contenido,
#         # }
#         # serializer = serializarObjeto(LogEntry, traza)
#         #if serializer.is_valid(raise_exception=True):
#             #serializer.save()
#         print("<Crear traza fin>")
#         return respuesta("quitar")#respuesta(serializer.data)
#     except BaseException as error:
#         return manipularError(error)

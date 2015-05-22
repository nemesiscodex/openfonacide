# -*- coding: utf-8 -*-

import hashlib, os
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.urlresolvers import reverse
from django.core.mail import EmailMessage
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext, Context
from django.template.loader import get_template
from django.views.generic import View, TemplateView
from django.http import HttpResponse, Http404, JsonResponse
from django.http import QueryDict
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from rest_framework import pagination
from rest_framework.response import Response
from rest_framework import permissions

from django.contrib.auth.models import User

from openfonacide.utils import dictfetch, escapelike
from openfonacide.serializers import *
from openfonacide import jsonh as JSONH


"""
ViewSets for API
"""


class PaginadorEstandard(pagination.LimitOffsetPagination):
    default_limit = 100


class OpenFonacideViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = PaginadorEstandard


class EstablecimientoViewSet(OpenFonacideViewSet):
    serializer_class = EstablecimientoSerializer
    queryset = Establecimiento.objects.all()


class DummyPrioridad(object):
    espacio = None
    mobiliario = None
    sanitario = None
    servicio = None


class PrioridadAPIViewDetail(viewsets.views.APIView):
    """
    Vista para listar las prioridades, y servicios de un establecimiento
    en especifico, dado un codigo de establecimiento
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, codigo_establecimiento):
        prioridad = DummyPrioridad()
        not_found = 0
        try:
            prioridad.espacio = Espacio.objects.get(codigo_establecimiento=codigo_establecimiento)
        except Espacio.DoesNotExist:
            not_found += 1
        try:
            prioridad.mobiliario = Mobiliario.objects.get(codigo_establecimiento=codigo_establecimiento)
        except Mobiliario.DoesNotExist:
            not_found += 1
        try:
            prioridad.sanitario = Sanitario.objects.get(codigo_establecimiento=codigo_establecimiento)
        except Sanitario.DoesNotExist:
            not_found += 1
        try:
            prioridad.servicio = ServicioBasico.objects.get(codigo_establecimiento=codigo_establecimiento)
        except ServicioBasico.DoesNotExist:
            not_found += 1

        if not_found == 4:
            return Http404

        return prioridad

    def get(self, request, codigo_establecimiento, format=None):
        prioridad = self.get_object(codigo_establecimiento)
        serializer = PrioridadSerializer(prioridad)
        if format == "jsonh":
            return Response(JSONH.pack(serializer.data))
        return Response(serializer.data)


class PrioridadAPIView(viewsets.views.APIView):
    """
    Vista para listar todas las prioridades, espacios (aulas, otros)
    mobiliarios, sanitarios. Y ademas los serivicios basicos
    """
    permission_classes = (permissions.IsAuthenticated,)
    # queryset = DummyPrioridad()

    def get_queryset(self):
        queryset = DummyPrioridad()
        queryset.espacio = Espacio.objects.all()
        queryset.mobiliario = Mobiliario.objects.all()
        queryset.sanitario = Sanitario.objects.all()
        queryset.servicio = ServicioBasico.objects.all()
        return queryset

    def get(self, request, format=None):
        """
        Retorna la lista de todas las prioridades y servicios
        """
        prioridad_serializada = PrioridadSerializer(self.get_queryset())

        if format == "json":
            return JsonResponse(prioridad_serializada.data, safe=False)

        if format == "jsonh":
            return JsonResponse(JSONH.pack(prioridad_serializada.data), safe=False)

        return Response(prioridad_serializada.data)


class InstitucionViewSet(OpenFonacideViewSet):
    serializer_class = InstitucionSerializer
    queryset = Institucion.objects.all()


class PartialGroupView(TemplateView):
    """
    Utilizada para los templates de AngularJS
    """

    def get_context_data(self, **kwargs):
        context = super(PartialGroupView, self).get_context_data(**kwargs)
        # update the context
        return context


class Index(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('index-nuevo.html', context_instance=RequestContext(request))

class Recuperar(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('index-nuevo.html', context_instance=RequestContext(request))
    def post(self, request, *args, **kwargs):
        method = request.POST.get('_method')
        _query = request.GET.copy()
        print request.REQUEST.__str__();
        print _query;
        _query.pop("error", None)
        _query.pop("message", None)
        _query.pop("success", None)
        if method == 'PUT':
            password = request.POST.get('password')
            password_confirm = request.POST.get('password_confirm')
            email = request.GET.get('email')
            token = request.GET.get('token')
            print email
            if password == password_confirm:
                try:
                    user = User.objects.get(email=email)
                    token_gen = PasswordResetTokenGenerator()
                    if token_gen.check_token(user, token):
                        user.set_password(password)
                        user.save()
                        _query['success'] = 'password_changed'
                        _query['message'] = 'Tu password ha sido cambiado!'
                        # redirect ?success=password_changed
                    else:
                        _query['error'] = 'invalid_token'
                        _query['message'] = 'Esta url ha caducado o es inválida!'
                        # redirect ?error=invalid_token
                except ObjectDoesNotExist:
                    # redirect ?error=user_does_not_exist
                    _query['error'] = 'user_does_not_exist'
                    _query['message'] = 'El usuario no existe!'
            else:
                # redirect ?error=password_missmatch
                _query['error'] = 'password_missmatch'
                _query['message'] = 'Las contraseñas no coinciden!'
                pass
        else:
            email = request.POST.get('email')

            user = User.objects.get(email=email)
            if user:
                token_gen = PasswordResetTokenGenerator()
                token = token_gen.make_token(user)
                print user.username
                ctx = {
                    "name": user.username,
                    "url": request.build_absolute_uri(reverse('recuperar_pass')) + '?token=' + token + '&email=' + email
                }
                mensaje = get_template('registration/mail.recuperar.html').render(Context(ctx))
                to = [ email ]
                mail = EmailMessage('Recuperar Contraseña',
                                    mensaje,
                                    to=to,
                                    from_email='openfonacide@ceamso.com.py')
                mail.content_type = 'html'
                mail.send()

            _query['success'] = 'email_sent'
            _query['message'] = 'Se ha enviado un correo con las instrucciones!'
            #redirect ?success=email_sent
        return redirect(reverse('recuperar_pass') + '?' + _query.urlencode())


# Deprecated
# class ListaInstitucionesController(View):
# def get(self, request, *args, **kwargs):
# cantidad = request.GET.get('rows')
# pagina = request.GET.get('page')
# lista = Institucion.objects.all()
# if cantidad is not None:
# paginator = Paginator(lista, cantidad)
#         else:
#             paginator = Paginator(lista, 10)
#         total = len(lista)
#         if pagina is None:
#             pagina = 1
#         try:
#             instituciones = paginator.page(pagina)
#         except PageNotAnInteger:
#             instituciones = paginator.page(1)
#         except EmptyPage:
#             instituciones = paginator.page(paginator.num_pages)
#         lista_instituciones = ListaInstitucionesSerializer(instituciones, many=True)
#         # result = lista_instituciones.data
#         result = {'total': str(paginator.num_pages), 'page': pagina, 'records': str(total),
#                   'rows': lista_instituciones.data}
#         return JsonResponse(result, safe=False)


class EstablecimientoController(View):
    def get(self, request, *args, **kwargs):
        _md5 = request.GET.get('md5')
        if _md5:
            cursor = connection.cursor()
            cursor.execute('select md5(CAST((array_agg(es.* order by es.id)) AS text)) from openfonacide_establecimiento es')
            result = cursor.fetchone()[0]
            return JsonResponse({ "hash":result}, safe=False)
        codigo_establecimiento = kwargs.get('codigo_establecimiento')
        short = request.GET.get('short')
        query = request.GET.get('q')
        anio = request.GET.get('anio')
        if not anio:
            anio = '2014'
        if short is not None:
            if codigo_establecimiento:
                establecimiento = EstablecimientoSerializerShort(
                    Establecimiento.objects.get(codigo_establecimiento=codigo_establecimiento, anio=anio))
            else:
                if query is not None:
                    establecimiento = EstablecimientoSerializerShort(
                        Establecimiento.objects.filter(nombre__icontains=query, anio=anio) |
                        Establecimiento.objects.filter(direccion__icontains=query, anio=anio), many=True)
                    establecimiento = {"results": establecimiento.data}
                    return JsonResponse(establecimiento, safe=False)
                else:
                    establecimiento = EstablecimientoSerializerShort(Establecimiento.objects.filter(anio=anio),
                                                                     many=True)
                    return JsonResponse(JSONH.pack(establecimiento.data), safe=False)
        else:
            if codigo_establecimiento:
                establecimiento = EstablecimientoSerializer(
                    Establecimiento.objects.get(codigo_establecimiento=codigo_establecimiento, anio=anio))
            else:
                establecimiento = EstablecimientoSerializer(Establecimiento.objects.filter(anio=anio), many=True)
        return JsonResponse(establecimiento.data, safe=False)


class InstitucionController(View):
    def get(self, request, *args, **kwargs):
        codigo_establecimiento = kwargs.get('codigo_establecimiento')
        query = request.GET.get('q')
        periodo = request.GET.get('periodo')
        offset = request.GET.get('offset')
        cantidad = request.GET.get('cantidad')
        tipos = ['nombre', 'codigo', 'direccion', 'distrito', 'barrio']
        tipo = request.GET.get('tipo')
        if tipo not in tipos:
            tipo = None
        if not periodo:
            periodo = '2014'
        if codigo_establecimiento:
            institucion = InstitucionSerializer(
                Institucion.objects.filter(codigo_establecimiento=codigo_establecimiento, periodo=periodo), many=True)
        else:
            if query is not None:
                instituciones = {
                    "results": {},
                    "query": query,
                    "tipo": tipo,
                    "periodo": periodo,
                    "base_url": reverse('index')
                }
                base_query = 'SELECT * FROM openfonacide_institucion inst ' \
                             'JOIN openfonacide_establecimiento est on ' \
                             '(est.anio=inst.periodo AND est.codigo_establecimiento=inst.codigo_establecimiento)'
                cursor = connection.cursor()
                if tipo is None or tipo == 'codigo':
                    cursor.execute(
                        base_query +
                        " WHERE inst.codigo_institucion = '" + escapelike(query.upper()) + "' AND inst.periodo=%s order by inst.codigo_institucion",
                        [periodo]
                    )
                    institucion0 = dictfetch(cursor, cantidad, offset)
                    instituciones['results']["codigo"] = {
                        "name": "Codigo de Instituci&oacute;n",
                        "results": institucion0
                    }

                if tipo is None or tipo == 'nombre':
                    cursor.execute(
                        base_query +
                        " WHERE inst.nombre_institucion like '%%" + escapelike(query.upper()) + "%%' AND inst.periodo=%s",
                        [periodo]
                    )
                    institucion1 = dictfetch(cursor, cantidad, offset)
                    instituciones['results']["nombre"] = {
                        "name": "Nombre",
                        "results": institucion1
                    }

                if tipo is None or tipo == 'direccion':
                    cursor.execute(
                        base_query +
                        " WHERE est.direccion like '%%" + escapelike(query.upper()) + "%%' AND inst.periodo=%s",
                        [periodo]
                    )
                    institucion2 = dictfetch(cursor, cantidad, offset)
                    instituciones['results']["direccion"] = {
                        "name": "Direccion",
                        "results": institucion2
                    }

                if tipo is None or tipo == 'distrito':
                    cursor.execute(
                        base_query +
                        " WHERE inst.nombre_distrito like '%%" + escapelike(query.upper()) + "%%' AND inst.periodo=%s",
                        [periodo]
                    )
                    institucion3 = dictfetch(cursor, cantidad, offset)
                    instituciones['results']["distrito"] = {
                        "name": "Distrito",
                        "results": institucion3
                    }

                if tipo is None or tipo == 'barrio':
                    cursor.execute(
                        base_query +
                        " WHERE inst.nombre_barrio_localidad like '%%" + escapelike(
                            query.upper()) + "%%' AND inst.periodo=%s",
                        [periodo]
                    )
                    institucion4 = dictfetch(cursor, cantidad, offset)
                    instituciones['results']["barrio"] = {
                        "name": "Barrio/Localidad",
                        "results": institucion4
                    }
                return JsonResponse(instituciones, safe=False)
            else:
                institucion = InstitucionSerializer(Institucion.objects.all(), many=True)
        return JsonResponse(institucion.data, safe=False)


class PrioridadController(View):
    def get(self, request, *args, **kwargs):
        codigo_establecimiento = kwargs.get('codigo_establecimiento')
        result = {
            "aulas": get_Pr(codigo_establecimiento, Espacio, EspacioSerializer).data,
            "sanitarios": get_Pr(codigo_establecimiento, Sanitario,
                                 SanitarioSerializer).data,
            "mobiliarios": get_Pr(codigo_establecimiento, Mobiliario,
                                  MobiliarioSerializer).data,
            "estados": get_Pr(codigo_establecimiento, ServicioBasico,
                              ServicioBasicoSerializer).data,


        }
        return JsonResponse(result, safe=False)


# class TotalPrioridadController(View):
# def get(self, request, *args, **kwargs):
#
#         result = {
#             "establecimietos": get_fonacide().data,
#
#
#
#
#         }
#         return JSONResponse(result)


class ComentariosController(View):
    pass

    # Not yet Implemented
    # def get(self, request, *args, **kwargs):
    #     codigo_establecimiento = kwargs.get('codigo_establecimiento')
    #     comentarios = Comentarios.objects.filter(codigo_establecimiento=codigo_establecimiento).order_by('fecha')
    #     return JSONResponse(ComentariosSerializer(comentarios, many=True).data)
    #
    # def post(self, request, *args, **kwargs):
    #     codigo_establecimiento = kwargs.get('codigo_establecimiento')
    #
    #     captcha = json.loads(request.POST.get('captcha'))
    #
    #     # captcha_result = urllib2.urlopen("https://www.google.com/recaptcha/api/siteverify",
    #     #                                  data=urllib.urlencode({
    #     #                                      "secret": "secret",
    #     #                                      "response": captcha
    #     #                                  })).read()
    #
    #     # analize captcha result
    #
    #     comentario = Comentarios()
    #     comentario.codigo_establecimiento_id = codigo_establecimiento
    #     comentario.autor = request.POST.get('autor')
    #     comentario.email = request.POST.get('email')
    #     comentario.texto = request.POST.get('texto')
    #     comentario.fecha = datetime.datetime.now()
    #     comentario.save()
    #     return JSONResponse({"success": True});

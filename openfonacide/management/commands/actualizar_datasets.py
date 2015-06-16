# encoding: utf-8
import csv
import django
from django.db import transaction

import urllib2
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from openfonacide.matcher import Matcher
from openfonacide.models import Importacion, RegistroImportacion, Adjudicacion, Planificacion, Temporal, Institucion

__author__ = 'Diego Ramírez'


def registrar_ultima_importacion(importacion=None, md5_sum=None):
    registro = RegistroImportacion(ultimo=True, ultimo_md5=md5_sum, importacion=importacion, fecha=datetime.now())
    registro.save()


@transaction.atomic
def do_import(lines_list=None, tipo=None):
    header_flag = True
    header = list()
    reader = csv.reader(lines_list)
    for row in reader:
        if header_flag:
            for column in row:
                header.append(column)
            header_flag = False
        else:
            args = dict()
            for element in range(len(row)):
                # setattr(a, header[i], row[i])
                args[header[element]] = row[element]

            if tipo is None:
                return

            if tipo is "planificacion":
                # Planificación logic
                try:
                    Planificacion.objects.update_or_create(id=args['id'], anio=args['anio'], defaults=args)
                except Exception as e:
                    continue

            if tipo is "adjudicación":
                # adjudicación logic
                try:
                    Adjudicacion.objects.update_or_create(id=args['id'], defaults=args)
                except Exception as e:
                    continue


def read_url_file(url=None):
    _file = urllib2.urlopen(url)
    data = _file.read()
    _file.close()

    return data


class Command(BaseCommand):
    def handle(self, *args, **options):
        tareas = Importacion.objects.filter(activo=True)
        worked = False

        for t in tareas:
            md5 = read_url_file(t.md5_url)

            try:
                registro = t.registroimportacion_set.get(ultimo=True)
                if md5 == registro.ultimo_md5:
                    return
                do_import(read_url_file(t.url), t.tipo)
                registro.ultimo = False
                registro.save()
                registrar_ultima_importacion(importacion=t, md5_sum=md5)
            except ObjectDoesNotExist:
                do_import(read_url_file(t.url), t.tipo)
                registrar_ultima_importacion(importacion=t, md5_sum=md5)

            worked = True

        if worked:
            m = Matcher(institucion_manager=Institucion.objects, planificacion_manager=Planificacion.objects,
                        temporal_manager=Temporal.objects
                        )
            m.do_match()


if __name__ == "__main__":
    django.setup()
    c = Command()
    c.handle()

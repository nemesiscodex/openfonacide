# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('anio', models.CharField(max_length=128)),
                ('codigo_establecimiento', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('codigo_departamento', models.CharField(max_length=128)),
                ('nombre_departamento', models.CharField(max_length=128)),
                ('codigo_distrito', models.CharField(max_length=128)),
                ('nombre_distrito', models.CharField(max_length=128)),
                ('codigo_zona', models.CharField(max_length=128)),
                ('nombre_zona', models.CharField(max_length=128)),
                ('codigo_barrio_localidad', models.CharField(max_length=128)),
                ('nombre_barrio_localidad', models.CharField(max_length=128)),
                ('direccion', models.CharField(max_length=128)),
                ('coordenadas_y', models.CharField(max_length=128)),
                ('coordenadas_x', models.CharField(max_length=128)),
                ('latitud', models.CharField(max_length=128)),
                ('longitud', models.CharField(max_length=128)),
                ('anho_cod_geo', models.CharField(max_length=128)),
                ('programa', models.CharField(max_length=128)),
                ('proyecto_111', models.CharField(max_length=128)),
                ('proyecto_822', models.CharField(max_length=128)),
                ('uri', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

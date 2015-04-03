# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0021_auto_20150402_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio', models.CharField(max_length=256)),
                ('codigo_establecimiento', models.CharField(max_length=256)),
                ('codigo_departamento', models.CharField(max_length=256)),
                ('nombre_departamento', models.CharField(max_length=256)),
                ('codigo_distrito', models.CharField(max_length=256)),
                ('nombre_distrito', models.CharField(max_length=256)),
                ('codigo_zona', models.CharField(max_length=256)),
                ('nombre_zona', models.CharField(max_length=256)),
                ('codigo_barrio_localidad', models.CharField(max_length=256)),
                ('nombre_barrio_localidad', models.CharField(max_length=256)),
                ('direccion', models.CharField(max_length=256)),
                ('coordenadas_y', models.CharField(max_length=256)),
                ('coordenadas_x', models.CharField(max_length=256)),
                ('latitud', models.CharField(max_length=256)),
                ('longitud', models.CharField(max_length=256)),
                ('anho_cod_geo', models.CharField(max_length=256)),
                ('uri', models.CharField(max_length=256)),
                ('nombre', models.CharField(default=b'<Sin nombre>', max_length=256)),
                ('fonacide', models.CharField(max_length=5, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('periodo', models.CharField(max_length=256)),
                ('codigo_departamento', models.CharField(max_length=256)),
                ('nombre_departamento', models.CharField(max_length=256)),
                ('codigo_distrito', models.CharField(max_length=256)),
                ('nombre_distrito', models.CharField(max_length=256)),
                ('codigo_barrio_localidad', models.CharField(max_length=256)),
                ('nombre_barrio_localidad', models.CharField(max_length=256)),
                ('codigo_zona', models.CharField(max_length=256)),
                ('nombre_zona', models.CharField(max_length=256)),
                ('codigo_establecimiento', models.CharField(max_length=256)),
                ('codigo_institucion', models.CharField(max_length=256)),
                ('nombre_institucion', models.CharField(max_length=256)),
                ('anho_cod_geo', models.CharField(max_length=256)),
                ('uri_establecimiento', models.CharField(max_length=256, null=True)),
                ('uri_institucion', models.CharField(max_length=256, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='establecimiento',
            unique_together=set([('anio', 'codigo_establecimiento')]),
        ),
    ]

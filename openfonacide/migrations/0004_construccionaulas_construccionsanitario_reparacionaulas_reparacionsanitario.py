# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0003_institucion_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstruccionAulas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prioridad', models.IntegerField()),
                ('cod_local', models.CharField(max_length=128)),
                ('cod_institucion', models.CharField(max_length=128)),
                ('nombre_institucion', models.CharField(max_length=128)),
                ('nro_esc', models.CharField(max_length=128)),
                ('distrito', models.CharField(max_length=128)),
                ('localidad_barrio', models.CharField(max_length=128)),
                ('zona', models.CharField(max_length=128)),
                ('nombre_asentamiento', models.CharField(max_length=128)),
                ('region_supervision', models.CharField(max_length=128)),
                ('nro_beneficiados', models.CharField(max_length=128)),
                ('nivel_educativo_beneficiado', models.CharField(max_length=128)),
                ('espacio_destinado', models.CharField(max_length=128)),
                ('cantidad_espacios_nuevos', models.CharField(max_length=128)),
                ('abastecimiento_agua', models.CharField(max_length=128)),
                ('corriente_electrica', models.CharField(max_length=128)),
                ('titulo_propiedad', models.CharField(max_length=128)),
                ('cuenta_con_espacio_construccion', models.CharField(max_length=128)),
                ('justificacion', models.CharField(max_length=128)),
                ('departamento', models.CharField(max_length=128)),
                ('cod_departamento', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConstruccionSanitario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prioridad', models.IntegerField()),
                ('cod_local', models.CharField(max_length=128)),
                ('cod_institucion', models.CharField(max_length=128)),
                ('nombre_institucion', models.CharField(max_length=128)),
                ('nro_esc', models.CharField(max_length=128)),
                ('distrito', models.CharField(max_length=128)),
                ('localidad_barrio', models.CharField(max_length=128)),
                ('zona', models.CharField(max_length=128)),
                ('nombre_asentamiento', models.CharField(max_length=128)),
                ('region_supervision', models.CharField(max_length=128)),
                ('nro_beneficiados', models.CharField(max_length=128)),
                ('nivel_educativo_beneficiado', models.CharField(max_length=128)),
                ('cant_sanitarios_construccion', models.CharField(max_length=128)),
                ('abastecimiento_agua', models.CharField(max_length=128)),
                ('corriente_electrica', models.CharField(max_length=128)),
                ('titulo_propiedad', models.CharField(max_length=128)),
                ('cuenta_con_espacio', models.CharField(max_length=128)),
                ('justificacion', models.CharField(max_length=128)),
                ('departamento', models.CharField(max_length=128)),
                ('cod_departamento', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReparacionAulas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prioridad', models.IntegerField()),
                ('cod_local', models.CharField(max_length=128)),
                ('cod_institucion', models.CharField(max_length=128)),
                ('nombre_institucion', models.CharField(max_length=128)),
                ('nro_esc', models.CharField(max_length=128)),
                ('distrito', models.CharField(max_length=128)),
                ('localidad_barrio', models.CharField(max_length=128)),
                ('zona', models.CharField(max_length=128)),
                ('nombre_asentamiento', models.CharField(max_length=128)),
                ('region_supervision', models.CharField(max_length=128)),
                ('nro_beneficiados', models.CharField(max_length=128)),
                ('nivel_educativo_beneficiado', models.CharField(max_length=128)),
                ('espacio_destinado_a', models.CharField(max_length=128)),
                ('cant_espacios_necesitan_reparacion', models.CharField(max_length=128)),
                ('cant_espacios_construidos_adecuacion', models.CharField(max_length=128)),
                ('justificacion', models.CharField(max_length=128)),
                ('departamento', models.CharField(max_length=128)),
                ('cod_departamento', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReparacionSanitario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prioridad', models.IntegerField()),
                ('cod_local', models.CharField(max_length=128)),
                ('cod_institucion', models.CharField(max_length=128)),
                ('nombre_institucion', models.CharField(max_length=128)),
                ('nro_esc', models.CharField(max_length=128)),
                ('distrito', models.CharField(max_length=128)),
                ('localidad_barrio', models.CharField(max_length=128)),
                ('zona', models.CharField(max_length=128)),
                ('nombre_asentamiento', models.CharField(max_length=128)),
                ('region_supervision', models.CharField(max_length=128)),
                ('nro_beneficiados', models.CharField(max_length=128)),
                ('nivel_educativo_beneficiado', models.CharField(max_length=128)),
                ('cantidad_sanitarios_construidos_reparacion', models.CharField(max_length=128)),
                ('cantidad_sanitarios_construidos_adecuacion', models.CharField(max_length=128)),
                ('justificacion', models.CharField(max_length=128)),
                ('departamento', models.CharField(max_length=128)),
                ('cod_departamento', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

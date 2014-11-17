# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mecmapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitucionData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio', models.CharField(max_length=128)),
                ('codigo_departamento', models.CharField(max_length=128)),
                ('nombre_departamento', models.CharField(max_length=128)),
                ('codigo_distrito', models.CharField(max_length=128)),
                ('nombre_distrito', models.CharField(max_length=128)),
                ('codigo_barrio_localidad', models.CharField(max_length=128)),
                ('nombre_barrio_localidad', models.CharField(max_length=128)),
                ('codigo_zona', models.CharField(max_length=128)),
                ('nombre_zona', models.CharField(max_length=128)),
                ('codigo_institucion', models.CharField(max_length=128)),
                ('nombre_institucion', models.CharField(max_length=128)),
                ('sector_o_tipo_gestion', models.CharField(max_length=128)),
                ('codigo_region_administrativa', models.CharField(max_length=128)),
                ('nombre_region_administrativa', models.CharField(max_length=128)),
                ('nombre_supervisor', models.CharField(max_length=128)),
                ('niveles_modalidades', models.CharField(max_length=128)),
                ('codigo_tipo_organizacion', models.CharField(max_length=128)),
                ('nombre_tipo_organizacion', models.CharField(max_length=128)),
                ('participacion_comunitaria', models.CharField(max_length=128)),
                ('direccion', models.CharField(max_length=128)),
                ('nro_telefono', models.CharField(max_length=128)),
                ('tiene_internet', models.CharField(max_length=128)),
                ('paginaweb', models.CharField(max_length=128)),
                ('correo_electronico', models.CharField(max_length=128)),
                ('codigo_establecimiento', models.ForeignKey(to='mecmapi.Institucion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0037_auto_20150405_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_planificacion', models.CharField(max_length=50, null=True)),
                ('anio', models.CharField(max_length=50, null=True)),
                ('id_llamado', models.CharField(max_length=50, null=True)),
                ('nombre_licitacion', models.CharField(max_length=400, null=True)),
                ('convocante', models.CharField(max_length=200, null=True)),
                ('codigo_sicp', models.CharField(max_length=50, null=True)),
                ('categoria_id', models.CharField(max_length=50, null=True)),
                ('categoria_codigo', models.CharField(max_length=50, null=True)),
                ('categoria', models.CharField(max_length=50, null=True)),
                ('tipo_procedimiento_id', models.CharField(max_length=50, null=True)),
                ('tipo_procedimiento_codigo', models.CharField(max_length=50, null=True)),
                ('tipo_procedimiento', models.CharField(max_length=50, null=True)),
                ('fecha_estimada', models.CharField(max_length=50, null=True)),
                ('fecha_publicacion', models.CharField(max_length=50, null=True)),
                ('_moneda', models.CharField(max_length=50, null=True)),
                ('moneda', models.CharField(max_length=50, null=True)),
                ('_estado', models.CharField(max_length=50, null=True)),
                ('estado', models.CharField(max_length=50, null=True)),
                ('_objeto_licitacion', models.CharField(max_length=50, null=True)),
                ('objeto_licitacion', models.CharField(max_length=50, null=True)),
                ('etiquetas', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Planificaciones',
            },
            bases=(models.Model,),
        ),
    ]

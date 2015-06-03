# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0040_auto_20150424_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adjudicacion',
            fields=[
                ('id', models.CharField(max_length=1024, serialize=False, primary_key=True)),
                ('planificacion_id', models.CharField(max_length=1024)),
                ('convocatoria_id', models.CharField(max_length=1024)),
                ('id_llamado', models.CharField(max_length=255)),
                ('nombre_licitacion', models.CharField(max_length=1024, null=True)),
                ('convocante', models.CharField(max_length=255, null=True)),
                ('codigo_sicp', models.CharField(max_length=255, null=True)),
                ('categoria_id', models.CharField(max_length=255, null=True)),
                ('categoria_codigo', models.CharField(max_length=255, null=True)),
                ('categoria', models.CharField(max_length=255, null=True)),
                ('tipo_procedimiento_id', models.CharField(max_length=255, null=True)),
                ('tipo_procedimiento_codigo', models.CharField(max_length=255, null=True)),
                ('tipo_procedimiento', models.CharField(max_length=255, null=True)),
                ('_estado', models.CharField(max_length=255, null=True)),
                ('estado', models.CharField(max_length=255, null=True)),
                ('_sistema_adjudicacion', models.CharField(max_length=255, null=True)),
                ('sistema_adjudicacion', models.CharField(max_length=255, null=True)),
                ('monto_total_adjudicado', models.CharField(max_length=255, null=True)),
                ('monto_periodo', models.CharField(max_length=255, null=True)),
                ('_moneda', models.CharField(max_length=255, null=True)),
                ('moneda', models.CharField(max_length=255, null=True)),
                ('fecha_publicacion', models.CharField(max_length=255, null=True)),
                ('observaciones', models.CharField(max_length=255, null=True)),
                ('restricciones', models.CharField(max_length=255, null=True)),
                ('organismo_financiador_id', models.CharField(max_length=255, null=True)),
                ('organismo_financiador', models.CharField(max_length=255, null=True)),
                ('codigo_institucion', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'adjudicaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Temporal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('periodo', models.CharField(max_length=256)),
                ('nombre_departamento', models.CharField(max_length=256)),
                ('nombre_distrito', models.CharField(max_length=256)),
                ('codigo_institucion', models.CharField(max_length=256)),
                ('id_planificacion', models.CharField(max_length=200, null=True)),
                ('anio', models.CharField(max_length=50, null=True)),
                ('id_llamado', models.CharField(max_length=200, null=True)),
                ('nombre_licitacion', models.CharField(max_length=1024, null=True)),
                ('convocante', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'temporales',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='planificacion',
            options={'verbose_name_plural': 'planificaciones'},
        ),
        migrations.AlterField(
            model_name='planificacion',
            name='nombre_licitacion',
            field=models.CharField(max_length=1024, null=True),
            preserve_default=True,
        ),
    ]

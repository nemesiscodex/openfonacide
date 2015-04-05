# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0023_delete_espacios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Espacios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('periodo', models.CharField(max_length=50, null=True)),
                ('codigo_departamento', models.CharField(max_length=256, null=True)),
                ('nombre_departamento', models.CharField(max_length=256, null=True)),
                ('codigo_distrito', models.CharField(max_length=256, null=True)),
                ('nombre_distrito', models.CharField(max_length=200, null=True)),
                ('numero_prioridad', models.IntegerField(null=True)),
                ('codigo_establecimiento', models.CharField(max_length=256, null=True)),
                ('codigo_institucion', models.CharField(max_length=256, null=True)),
                ('nombre_institucion', models.CharField(max_length=200)),
                ('codigo_zona', models.CharField(max_length=256, null=True)),
                ('nombre_zona', models.CharField(max_length=256, null=True)),
                ('nivel_educativo_beneficiado', models.CharField(max_length=256, null=True)),
                ('cuenta_espacio_para_construccion', models.CharField(max_length=256, null=True)),
                ('nombre_espacio', models.CharField(max_length=200, null=True)),
                ('tipo_requerimiento_infraestructura', models.CharField(max_length=200, null=True)),
                ('cantidad_requerida', models.CharField(max_length=256, null=True)),
                ('numero_beneficiados', models.CharField(max_length=256, null=True)),
                ('justificacion', models.CharField(max_length=2048, null=True)),
                ('uri_establecimiento', models.CharField(max_length=256, null=True)),
                ('uri_institucion', models.CharField(max_length=256, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

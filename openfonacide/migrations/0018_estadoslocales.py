# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0017_auto_20141213_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadosLocales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('periodo', models.CharField(max_length=50, null=True)),
                ('codigo_departamento', models.CharField(max_length=256, null=True)),
                ('nombre_departamento', models.CharField(max_length=256, null=True)),
                ('codigo_distrito', models.CharField(max_length=256, null=True)),
                ('nombre_distrito', models.CharField(max_length=200, null=True)),
                ('codigo_establecimiento', models.CharField(max_length=200, null=True)),
                ('codigo_barrio_localidad', models.CharField(max_length=200, null=True)),
                ('nombre_barrio_localidad', models.CharField(max_length=200, null=True)),
                ('codigo_zona', models.CharField(max_length=256, null=True)),
                ('nombre_zona', models.CharField(max_length=256, null=True)),
                ('nombre_asentamiento_colonia', models.CharField(max_length=256, null=True)),
                ('suministro_energia_electrica', models.CharField(max_length=256, null=True)),
                ('abastecimiento_agua', models.CharField(max_length=256, null=True)),
                ('servicio_sanitario_actual', models.CharField(max_length=256, null=True)),
                ('titulo_de_propiedad', models.CharField(max_length=256, null=True)),
                ('cuenta_plano', models.CharField(max_length=256, null=True)),
                ('prevencion_incendio', models.CharField(max_length=256, null=True)),
                ('uri_establecimiento', models.CharField(max_length=256, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

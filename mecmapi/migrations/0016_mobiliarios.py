# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mecmapi', '0015_auto_20141213_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobiliarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('periodo', models.CharField(max_length=50, null=True)),
                ('cod_departamento', models.CharField(max_length=256, null=True)),
                ('nombre_departamento', models.CharField(max_length=256, null=True)),
                ('cod_distrito', models.CharField(max_length=256, null=True)),
                ('nombre_distrito', models.CharField(max_length=200, null=True)),
                ('prioridad', models.IntegerField(null=True)),
                ('cod_establecimiento', models.CharField(max_length=256, null=True)),
                ('cod_institucion', models.CharField(max_length=256, null=True)),
                ('nombre_institucion', models.CharField(max_length=200, null=True)),
                ('codigo_zona', models.CharField(max_length=256, null=True)),
                ('nombre_zona', models.CharField(max_length=256, null=True)),
                ('nivel_educativo_beneficiado', models.CharField(max_length=256, null=True)),
                ('nombre_mobiliario', models.CharField(max_length=256, null=True)),
                ('cantidad_requerida', models.CharField(max_length=256, null=True)),
                ('numero_beneficiados', models.CharField(max_length=256, null=True)),
                ('justificacion', models.CharField(max_length=900, null=True)),
                ('uri_establecimiento', models.CharField(max_length=256, null=True)),
                ('uri_institucion', models.CharField(max_length=256, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

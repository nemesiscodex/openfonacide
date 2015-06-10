# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0054_reportes'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificacionesCambioDeEstado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Notificacion de Cambio de estado',
                'verbose_name_plural': 'Notificaciones de Cambio de estado',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NotificacionesReportes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Notificacion de Reporte',
                'verbose_name_plural': 'Notificaciones de Reporte',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NotificacionesVerificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Notificacion de Verificaci\xf3n',
                'verbose_name_plural': 'Notificaciones de Verificaci\xf3n',
            },
            bases=(models.Model,),
        ),
    ]

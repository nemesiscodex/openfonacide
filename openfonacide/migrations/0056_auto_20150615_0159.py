# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0055_notificacionescambiodeestado_notificacionesreportes_notificacionesverificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Importacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=1024)),
                ('md5_url', models.CharField(max_length=1024)),
                ('activo', models.BooleanField(default=False)),
                ('tipo', models.CharField(max_length=254, choices=[('adjudicacion', 'adjudicacion'), ('planificacion', 'planificacion')])),
            ],
            options={
                'verbose_name': 'Importaci\xf3n',
                'verbose_name_plural': 'importaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegistroImportacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ultimo', models.BooleanField(default=False)),
                ('ultimo_md5', models.CharField(max_length=1024, null=True)),
                ('fecha', models.DateTimeField()),
                ('importacion', models.ForeignKey(to='openfonacide.Importacion')),
            ],
            options={
                'verbose_name': 'Registro de importaci\xf3n',
                'verbose_name_plural': 'Registros de importaci\xf3n',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='planificacion',
            name='id',
            field=models.CharField(max_length=1024, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='planificacion',
            unique_together=set([('id_llamado', 'anio')]),
        ),
    ]

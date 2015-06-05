# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0053_auto_20150531_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_prioridad', models.IntegerField()),
                ('tipo', models.CharField(max_length=128)),
                ('codigo_establecimiento', models.CharField(max_length=256)),
                ('codigo_institucion', models.CharField(max_length=256)),
                ('nombre_institucion', models.CharField(max_length=256)),
                ('periodo', models.CharField(max_length=16)),
                ('fecha', models.DateTimeField()),
                ('cedula', models.CharField(max_length=16)),
                ('nombre', models.CharField(max_length=256)),
                ('apellido', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('telefono', models.CharField(max_length=256)),
                ('motivo', models.IntegerField()),
                ('observacion', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

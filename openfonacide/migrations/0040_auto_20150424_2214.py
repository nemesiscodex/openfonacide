# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0039_auto_20150424_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planificacion',
            name='_estado',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='planificacion',
            name='_objeto_licitacion',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='planificacion',
            name='estado',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='planificacion',
            name='id_llamado',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='planificacion',
            name='objeto_licitacion',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='planificacion',
            name='tipo_procedimiento',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]

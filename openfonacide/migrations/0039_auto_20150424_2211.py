# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0038_planificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planificacion',
            name='categoria',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='planificacion',
            name='categoria_codigo',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='planificacion',
            name='id_planificacion',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]

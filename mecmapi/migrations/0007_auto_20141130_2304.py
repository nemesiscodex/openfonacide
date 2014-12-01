# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mecmapi', '0006_auto_20141130_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construccionaulas',
            name='distrito',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='construccionaulas',
            name='espacio_destinado',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='construccionaulas',
            name='justificacion',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='construccionsanitario',
            name='distrito',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='construccionsanitario',
            name='justificacion',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='construccionsanitario',
            name='nombre_institucion',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reparacionaulas',
            name='distrito',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reparacionaulas',
            name='justificacion',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reparacionaulas',
            name='nombre_institucion',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reparacionsanitario',
            name='distrito',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reparacionsanitario',
            name='justificacion',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reparacionsanitario',
            name='nombre_institucion',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]

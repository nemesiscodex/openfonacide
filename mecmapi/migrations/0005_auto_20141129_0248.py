# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mecmapi', '0004_construccionaulas_construccionsanitario_reparacionaulas_reparacionsanitario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construccionaulas',
            name='justificacion',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='construccionaulas',
            name='nombre_institucion',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='construccionsanitario',
            name='justificacion',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='construccionsanitario',
            name='nombre_institucion',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reparacionaulas',
            name='justificacion',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reparacionaulas',
            name='nombre_institucion',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reparacionsanitario',
            name='justificacion',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reparacionsanitario',
            name='nombre_institucion',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]

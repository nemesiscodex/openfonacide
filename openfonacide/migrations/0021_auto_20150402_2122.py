# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0020_institucion_fonacide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adjudicacion',
            name='codigo_establecimiento',
        ),
        migrations.DeleteModel(
            name='Adjudicacion',
        ),
        migrations.RemoveField(
            model_name='comentarios',
            name='codigo_establecimiento',
        ),
        migrations.DeleteModel(
            name='Comentarios',
        ),
        migrations.DeleteModel(
            name='ConstruccionAulas',
        ),
        migrations.DeleteModel(
            name='ConstruccionSanitario',
        ),
        migrations.RemoveField(
            model_name='instituciondata',
            name='codigo_establecimiento',
        ),
        migrations.DeleteModel(
            name='Institucion',
        ),
        migrations.DeleteModel(
            name='InstitucionData',
        ),
        migrations.DeleteModel(
            name='ReparacionAulas',
        ),
        migrations.DeleteModel(
            name='ReparacionSanitario',
        ),
    ]

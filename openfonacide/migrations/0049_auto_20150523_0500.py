# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0048_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucion',
            name='adjudicaciones',
            field=models.ManyToManyField(to='openfonacide.Adjudicacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='institucion',
            name='planificaciones',
            field=models.ManyToManyField(to='openfonacide.Planificacion'),
            preserve_default=True,
        ),
    ]

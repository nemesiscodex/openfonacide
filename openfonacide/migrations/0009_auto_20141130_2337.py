# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0008_auto_20141130_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construccionaulas',
            name='prioridad',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='construccionsanitario',
            name='prioridad',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reparacionaulas',
            name='prioridad',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reparacionsanitario',
            name='prioridad',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]

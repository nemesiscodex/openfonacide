# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0041_auto_20150507_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacio',
            name='numero_prioridad',
            field=models.IntegerField(null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mobiliario',
            name='numero_prioridad',
            field=models.IntegerField(null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sanitario',
            name='numero_prioridad',
            field=models.IntegerField(null=True, db_index=True),
            preserve_default=True,
        ),
    ]

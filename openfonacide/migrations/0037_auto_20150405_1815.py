# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0036_auto_20150405_0226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='espacio',
            old_name='cuenta_con_espacio_para_construccion',
            new_name='cuenta_espacio_para_construccion',
        ),
        migrations.RenameField(
            model_name='establecimiento',
            old_name='anho_codigo_geo',
            new_name='anho_cod_geo',
        ),
        migrations.RenameField(
            model_name='institucion',
            old_name='anho_codigo_geo',
            new_name='anho_cod_geo',
        ),
        migrations.RenameField(
            model_name='sanitario',
            old_name='cuenta_con_espacio_para_construccion',
            new_name='cuenta_espacio_para_construccion',
        ),
    ]

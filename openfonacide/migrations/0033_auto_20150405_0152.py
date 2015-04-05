# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0032_auto_20150404_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='establecimiento',
            old_name='anho_cod_geo',
            new_name='anho_codigo_geo',
        ),
        migrations.RenameField(
            model_name='institucion',
            old_name='anho_cod_geo',
            new_name='anho_codigo_geo',
        ),
    ]

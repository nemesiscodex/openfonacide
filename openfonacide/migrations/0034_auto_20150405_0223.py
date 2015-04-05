# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0033_auto_20150405_0152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='espacio',
            old_name='cuenta_espacio_para_construccion',
            new_name='cuenta_con_espacio_para_construccion',
        ),
    ]

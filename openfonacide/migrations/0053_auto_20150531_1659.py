# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0052_auto_20150531_0225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historialestado',
            options={'permissions': (('verificar_estado', 'Puede Verificar el estado de obras'), ('cambiar_estado', 'Puede Cambiar el estado de obras'))},
        ),
    ]

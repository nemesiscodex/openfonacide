# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0030_estadoslocales'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Espacios',
            new_name='Espacio',
        ),
        migrations.RenameModel(
            old_name='EstadosLocales',
            new_name='EstadoLocal',
        ),
        migrations.RenameModel(
            old_name='Mobiliarios',
            new_name='Mobiliario',
        ),
        migrations.RenameModel(
            old_name='Sanitarios',
            new_name='Sanitario',
        ),
        migrations.AlterModelOptions(
            name='estadolocal',
            options={'verbose_name_plural': 'estadoslocales'},
        ),
    ]

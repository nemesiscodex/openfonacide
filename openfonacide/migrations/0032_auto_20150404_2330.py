# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0031_auto_20150404_2224'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EstadoLocal',
            new_name='ServicioBasico',
        ),
        migrations.AlterModelOptions(
            name='institucion',
            options={'verbose_name_plural': 'instituciones'},
        ),
        migrations.AlterModelOptions(
            name='serviciobasico',
            options={'verbose_name_plural': 'serviciosbasicos'},
        ),
    ]

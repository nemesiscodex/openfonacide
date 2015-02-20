# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0018_estadoslocales'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estadoslocales',
            old_name='codigo_departamento',
            new_name='cod_departamento',
        ),
        migrations.RenameField(
            model_name='estadoslocales',
            old_name='codigo_distrito',
            new_name='cod_distrito',
        ),
        migrations.RenameField(
            model_name='estadoslocales',
            old_name='codigo_establecimiento',
            new_name='cod_establecimiento',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0046_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planificacion',
            name='codigo_institucion',
        ),
    ]

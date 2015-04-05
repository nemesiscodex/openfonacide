# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0028_mobiliarios'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EstadosLocales',
        ),
    ]

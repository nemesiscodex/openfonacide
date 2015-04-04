# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0026_sanitarios'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mobiliarios',
        ),
    ]

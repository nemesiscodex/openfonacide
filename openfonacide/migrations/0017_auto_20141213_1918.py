# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0016_mobiliarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobiliarios',
            name='justificacion',
            field=models.CharField(max_length=1200, null=True),
            preserve_default=True,
        ),
    ]

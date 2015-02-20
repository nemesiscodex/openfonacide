# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0014_auto_20141213_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacios',
            name='justificacion',
            field=models.CharField(max_length=900, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sanitarios',
            name='justificacion',
            field=models.CharField(max_length=900, null=True),
            preserve_default=True,
        ),
    ]

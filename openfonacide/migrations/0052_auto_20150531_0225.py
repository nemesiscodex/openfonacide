# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0051_historialestado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacio',
            name='documento',
            field=models.CharField(max_length=256, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mobiliario',
            name='documento',
            field=models.CharField(max_length=256, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sanitario',
            name='documento',
            field=models.CharField(max_length=256, null=True),
            preserve_default=True,
        ),
    ]

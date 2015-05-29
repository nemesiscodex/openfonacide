# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0042_auto_20150513_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjudicacion',
            name='observaciones',
            field=models.CharField(max_length=1024, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='adjudicacion',
            name='restricciones',
            field=models.CharField(max_length=512, null=True),
            preserve_default=True,
        ),
    ]

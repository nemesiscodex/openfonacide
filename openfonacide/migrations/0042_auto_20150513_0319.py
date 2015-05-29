# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0041_auto_20150513_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjudicacion',
            name='convocante',
            field=models.CharField(max_length=1024, null=True),
            preserve_default=True,
        ),
    ]

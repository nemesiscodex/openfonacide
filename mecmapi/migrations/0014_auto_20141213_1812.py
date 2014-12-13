# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mecmapi', '0013_espacios_sanitarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacios',
            name='justificacion',
            field=models.CharField(max_length=700, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sanitarios',
            name='justificacion',
            field=models.CharField(max_length=700, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sanitarios',
            name='nombre_institucion',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]

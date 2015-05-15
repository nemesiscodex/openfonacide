# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0043_auto_20150513_0321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planificacion',
            name='id_planificacion',
        ),
        migrations.AddField(
            model_name='planificacion',
            name='codigo_institucion',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='planificacion',
            name='id',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]

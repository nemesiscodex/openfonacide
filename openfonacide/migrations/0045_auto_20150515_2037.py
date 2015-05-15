# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0044_auto_20150513_0340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='establecimiento',
            options={'verbose_name_plural': 'establecimientos'},
        ),
        migrations.RemoveField(
            model_name='adjudicacion',
            name='codigo_institucion',
        ),
        migrations.AddField(
            model_name='temporal',
            name='nombre_institucion',
            field=models.CharField(max_length=256, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='adjudicacion',
            name='nombre_licitacion',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mecmapi', '0019_auto_20141213_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucion',
            name='fonacide',
            field=models.CharField(max_length=5, null=True),
            preserve_default=True,
        ),
    ]

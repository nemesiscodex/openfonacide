# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0035_auto_20150405_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobiliario',
            name='uri_establecimiento',
            field=models.CharField(max_length=256, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mobiliario',
            name='uri_institucion',
            field=models.CharField(max_length=256, null=True),
            preserve_default=True,
        ),
    ]

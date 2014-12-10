# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mecmapi', '0010_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='email',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]

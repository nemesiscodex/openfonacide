# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mecmapi', '0002_instituciondata'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucion',
            name='nombre',
            field=models.CharField(default=b'<Sin nombre>', max_length=256),
            preserve_default=True,
        ),
    ]

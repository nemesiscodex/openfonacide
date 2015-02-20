# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0009_auto_20141130_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.CharField(max_length=1024)),
                ('autor', models.CharField(max_length=256)),
                ('fecha', models.DateField()),
                ('codigo_establecimiento', models.ForeignKey(to='openfonacide.Institucion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mecmapi', '0009_auto_20141130_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adjudicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_adjudicacion', models.CharField(max_length=256)),
                ('llamado', models.CharField(max_length=256)),
                ('monto', models.IntegerField()),
                ('entidad', models.CharField(max_length=256)),
                ('estado', models.CharField(max_length=256)),
                ('anio', models.IntegerField()),
                ('codigo_establecimiento', models.ForeignKey(to='mecmapi.Institucion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='nombre',
            field=models.CharField(max_length=256, default='<Sin nombre>'),
            preserve_default=True,
        ),
    ]

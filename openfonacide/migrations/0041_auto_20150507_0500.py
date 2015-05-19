# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0040_auto_20150424_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacio',
            name='codigo_departamento',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='espacio',
            name='codigo_distrito',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='espacio',
            name='codigo_establecimiento',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='espacio',
            name='codigo_institucion',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='espacio',
            name='codigo_zona',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='establecimiento',
            name='codigo_barrio_localidad',
            field=models.CharField(max_length=256, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='establecimiento',
            name='codigo_departamento',
            field=models.CharField(max_length=256, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='establecimiento',
            name='codigo_distrito',
            field=models.CharField(max_length=256, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='establecimiento',
            name='codigo_establecimiento',
            field=models.CharField(max_length=256, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='establecimiento',
            name='codigo_zona',
            field=models.CharField(max_length=256, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='institucion',
            name='codigo_barrio_localidad',
            field=models.CharField(max_length=256, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='institucion',
            name='codigo_departamento',
            field=models.CharField(max_length=256, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='institucion',
            name='codigo_distrito',
            field=models.CharField(max_length=256, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='institucion',
            name='codigo_establecimiento',
            field=models.CharField(max_length=256, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='institucion',
            name='codigo_institucion',
            field=models.CharField(max_length=256, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='institucion',
            name='codigo_zona',
            field=models.CharField(max_length=256, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mobiliario',
            name='codigo_departamento',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mobiliario',
            name='codigo_distrito',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mobiliario',
            name='codigo_establecimiento',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mobiliario',
            name='codigo_institucion',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mobiliario',
            name='codigo_zona',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sanitario',
            name='codigo_departamento',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sanitario',
            name='codigo_distrito',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sanitario',
            name='codigo_establecimiento',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sanitario',
            name='codigo_institucion',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sanitario',
            name='codigo_zona',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='serviciobasico',
            name='codigo_barrio_localidad',
            field=models.CharField(max_length=200, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='serviciobasico',
            name='codigo_departamento',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='serviciobasico',
            name='codigo_distrito',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='serviciobasico',
            name='codigo_establecimiento',
            field=models.CharField(max_length=200, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='serviciobasico',
            name='codigo_zona',
            field=models.CharField(max_length=256, null=True, db_index=True),
            preserve_default=True,
        ),
    ]

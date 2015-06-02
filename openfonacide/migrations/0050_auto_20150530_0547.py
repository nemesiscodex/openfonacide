# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import openfonacide.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openfonacide', '0049_auto_20150523_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='espacio',
            name='cambiado_por',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='espacio',
            name='documento',
            field=models.FileField(null=True, upload_to=openfonacide.models.get_upload_file_name),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='espacio',
            name='estado_de_obra',
            field=models.CharField(default=b'Priorizado', max_length=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='espacio',
            name='fecha_modificacion',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='espacio',
            name='fecha_verificacion',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='espacio',
            name='verificado_por',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mobiliario',
            name='cambiado_por',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mobiliario',
            name='documento',
            field=models.FileField(null=True, upload_to=openfonacide.models.get_upload_file_name),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mobiliario',
            name='estado_de_obra',
            field=models.CharField(default=b'Priorizado', max_length=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mobiliario',
            name='fecha_modificacion',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mobiliario',
            name='fecha_verificacion',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mobiliario',
            name='verificado_por',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sanitario',
            name='cambiado_por',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sanitario',
            name='documento',
            field=models.FileField(null=True, upload_to=openfonacide.models.get_upload_file_name),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sanitario',
            name='estado_de_obra',
            field=models.CharField(default=b'Priorizado', max_length=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sanitario',
            name='fecha_modificacion',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sanitario',
            name='fecha_verificacion',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sanitario',
            name='verificado_por',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]

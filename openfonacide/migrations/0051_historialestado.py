# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import openfonacide.models


class Migration(migrations.Migration):

    dependencies = [
        ('openfonacide', '0050_auto_20150530_0547'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialEstado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prioridad', models.IntegerField(db_index=True)),
                ('clase', models.CharField(max_length=50, db_index=True)),
                ('fecha', models.DateTimeField()),
                ('estado_de_obra', models.CharField(max_length=32)),
                ('fecha_modificacion', models.DateTimeField(null=True, db_index=True)),
                ('cambiado_por_id', models.IntegerField(null=True)),
                ('cambiado_por_email', models.CharField(max_length=256, null=True)),
                ('fecha_verificacion', models.DateTimeField(null=True)),
                ('verificado_por_id', models.IntegerField(null=True)),
                ('verificado_por_email', models.CharField(max_length=256, null=True)),
                ('documento', models.FileField(null=True, upload_to=openfonacide.models.get_upload_file_name)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

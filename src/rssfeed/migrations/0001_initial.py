# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('publishdate', models.DateTimeField()),
                ('guid', models.TextField(unique=True)),
                ('url', models.TextField()),
                ('srcurl', models.TextField()),
            ],
        ),
    ]

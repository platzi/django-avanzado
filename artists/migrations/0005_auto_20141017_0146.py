# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0004_auto_20141014_0215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='track',
            name='file',
            field=models.FileField(null=True, upload_to=b'tracks', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='slug',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='slug',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]

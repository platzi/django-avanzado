# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_remove_track_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='slug',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
    ]

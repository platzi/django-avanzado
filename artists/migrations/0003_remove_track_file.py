# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_track_listen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='file',
        ),
    ]

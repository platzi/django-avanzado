# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('cover', models.ImageField(upload_to=b'albums')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=30, blank=True)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('biography', models.TextField(blank=True)),
                ('picture', models.ImageField(upload_to=b'artists')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(null=True, upload_to=b'tracks', blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('album', models.ForeignKey(to='artists.Album')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(to='artists.Artist'),
            preserve_default=True,
        ),
    ]

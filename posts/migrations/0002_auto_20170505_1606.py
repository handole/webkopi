# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 16:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp', '-updated']},
        ),
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='harga',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=posts.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 5, 5, 16, 6, 5, 909955, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2017, 5, 5, 16, 6, 25, 734527, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=160),
        ),
    ]

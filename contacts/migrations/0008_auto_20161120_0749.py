# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161117174642 on 2016-11-20 07:49
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20161120_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cal_file',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='jobs/processes'), upload_to=django.core.files.storage.FileSystemStorage(location='jobs/processes')),
        ),
    ]

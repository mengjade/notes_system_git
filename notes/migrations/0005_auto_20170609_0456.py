# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20170609_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='comment',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='pic_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]

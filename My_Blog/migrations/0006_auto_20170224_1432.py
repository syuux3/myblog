# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Blog', '0005_auto_20170224_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(verbose_name='发表日期'),
        ),
    ]

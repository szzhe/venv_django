# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-17 14:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='choice',
            table='choice',
        ),
        migrations.AlterModelTable(
            name='question',
            table='question',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-22 09:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_front', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storedbasket',
            options={'verbose_name': 'stored basket', 'verbose_name_plural': 'stored baskets'},
        ),
    ]

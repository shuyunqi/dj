# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 01:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_total_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('created',), 'verbose_name': '\u56fe\u7247', 'verbose_name_plural': '\u56fe\u7247'},
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20181128_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='is_pub',
            field=models.BooleanField(default=False, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='art',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='catalog_pic/', verbose_name='Photo'),
        ),
    ]

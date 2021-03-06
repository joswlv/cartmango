# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-03 16:37
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mall',
            name='thumbnail',
            field=django_resized.forms.ResizedImageField(blank=True, null=True, upload_to='mall/%Y/%m/%d', verbose_name='썸네일'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=django_resized.forms.ResizedImageField(blank=True, null=True, upload_to='product/%Y/%m/%d', verbose_name='썸네일'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-03 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]

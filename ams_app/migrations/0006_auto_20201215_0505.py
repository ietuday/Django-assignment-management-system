# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-12-15 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams_app', '0005_auto_20171119_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='matric_number',
            field=models.CharField(max_length=100),
        ),
    ]
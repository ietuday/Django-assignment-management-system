# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams_app', '0003_auto_20171116_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='upload',
            field=models.FileField(default='No file uploaded', null=True, upload_to='assignments/'),
        ),
    ]

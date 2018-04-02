# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-02 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdm_data', '0007_auto_20180329_0848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='graphdata',
            old_name='cpu_use',
            new_name='downstream',
        ),
        migrations.AddField(
            model_name='graphdata',
            name='upstream',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
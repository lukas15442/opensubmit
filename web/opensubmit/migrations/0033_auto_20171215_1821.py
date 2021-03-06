# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-15 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensubmit', '0032_auto_20171215_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmachine',
            name='address',
        ),
        migrations.AlterField(
            model_name='testmachine',
            name='config',
            field=models.TextField(help_text='Host configuration in JSON format.', null=True),
        ),
        migrations.AlterField(
            model_name='testmachine',
            name='host',
            field=models.CharField(help_text='UUID of this machine.', max_length=50, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20160207_0950'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactions',
            options={},
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='transaction_timestamp',
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transactions_code',
            field=models.CharField(choices=[('CB', 'Check balance'), ('GM', 'Trye gets money'), ('SS', 'Success operation')], max_length=2),
        ),
    ]

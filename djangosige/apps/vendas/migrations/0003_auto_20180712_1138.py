# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 03:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_auto_20170820_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='local_orig',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='venda_local_estoque', to='estoque.LocalEstoque'),
        ),
    ]

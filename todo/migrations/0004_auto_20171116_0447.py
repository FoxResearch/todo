# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_nota_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombreusuario',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

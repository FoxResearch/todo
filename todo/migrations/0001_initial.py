# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 07:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=200)),
                ('creado', models.DateField(auto_now_add=True)),
                ('publico', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreusuario', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('creado', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='nota',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Usuario'),
        ),
    ]

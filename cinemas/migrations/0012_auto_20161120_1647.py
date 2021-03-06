# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-20 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0011_auto_20161120_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinema_name', models.CharField(max_length=200)),
                ('cinema_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_type',
            field=models.CharField(default='c', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='cinema',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cinemas.Cinema'),
            preserve_default=False,
        ),
    ]

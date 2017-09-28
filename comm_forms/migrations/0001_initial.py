# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 00:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0003_auto_20170911_0618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comm_Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Post', verbose_name='Book')),
            ],
        ),
    ]
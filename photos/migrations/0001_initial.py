# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название альбома')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Ссылка для альбома')),
                ('img', models.ImageField(help_text='Размер изображения 200px на 200px', upload_to='images', verbose_name='Изображение альбома')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название фотографии')),
                ('img', models.ImageField(help_text='lololo', upload_to='images', verbose_name='Фото')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Album', verbose_name='Альбом')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['title'],
            },
        ),
    ]

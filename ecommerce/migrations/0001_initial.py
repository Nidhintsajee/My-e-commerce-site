# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('product_image', models.ImageField(upload_to=b'picture/')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('thumbnail', models.ImageField(upload_to=b'thumbnails/')),
                ('caption', models.CharField(blank=True, max_length=250)),
            ],
        ),
    ]

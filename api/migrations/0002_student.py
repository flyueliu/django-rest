# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-10 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(1, '\u7537'), (2, '\u5973')])),
            ],
        ),
    ]
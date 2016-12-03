# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=100)),
                ('action_date', models.DateTimeField()),
                ('action_object', models.CharField(max_length=100)),
                ('action', models.CharField(max_length=100)),
            ],
        ),
    ]

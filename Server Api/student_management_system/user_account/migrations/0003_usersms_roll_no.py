# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-27 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0002_auto_20160927_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersms',
            name='roll_no',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

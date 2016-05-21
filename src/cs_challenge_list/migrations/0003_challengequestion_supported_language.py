# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cs_core', '0001_initial'),
        ('cs_challenge_list', '0002_auto_20160510_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengequestion',
            name='supported_language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cs_core.ProgrammingLanguage'),
        ),
    ]

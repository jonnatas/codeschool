# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 01:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cs_questions', '0002_question_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='codingioresponse',
            old_name='question_fallback',
            new_name='question',
        ),
    ]

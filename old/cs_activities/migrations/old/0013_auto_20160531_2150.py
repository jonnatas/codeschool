# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 00:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cs_activities', '0012_auto_20160531_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='grading_method_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cs_activities.GradingMethod'),
        ),
        migrations.AlterUniqueTogether(
            name='gradingmethod',
            unique_together=set([('name', 'owner')]),
        ),
    ]

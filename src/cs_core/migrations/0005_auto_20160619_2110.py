# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 00:10
from __future__ import unicode_literals

import cs_core.models.activity.response_context
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('cs_core', '0004_auto_20160619_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='responsecontext',
            old_name='data',
            new_name='constraints',
        ),
        migrations.RemoveField(
            model_name='codecarouselactivity',
            name='grading_method',
        ),
        migrations.RemoveField(
            model_name='contentactivity',
            name='grading_method',
        ),
        migrations.AddField(
            model_name='responsecontext',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True, verbose_name='deadline'),
        ),
        migrations.AddField(
            model_name='responsecontext',
            name='delay_penalty',
            field=models.DecimalField(decimal_places=2, default=25, help_text='Sets the percentage of the total grade that will be lost due to delayed responses.', max_digits=6, verbose_name='delay penalty'),
        ),
        migrations.AddField(
            model_name='responsecontext',
            name='delayed_feedback',
            field=models.BooleanField(default=False, help_text='If set, students will be only be able to see the feedback after the activity deadline.', verbose_name='delayed feedback'),
        ),
        migrations.AddField(
            model_name='responsecontext',
            name='format',
            field=models.ForeignKey(blank=True, help_text='Defines the required file format or programming language for student responses, when applicable.', null=True, on_delete=django.db.models.deletion.CASCADE, to='cs_core.FileFormat'),
        ),
        migrations.AddField(
            model_name='responsecontext',
            name='grading_method',
            field=models.ForeignKey(blank=True, default=cs_core.models.activity.response_context.grading_method_best, help_text='Choose the strategy for grading this activity.', on_delete=django.db.models.deletion.SET_DEFAULT, to='cs_core.GradingMethod'),
        ),
        migrations.AddField(
            model_name='responsecontext',
            name='hard_deadline',
            field=models.DateTimeField(blank=True, help_text='If set, responses submitted after the deadline will be accepted with a penalty.', null=True, verbose_name='hard deadline'),
        ),
        migrations.AddField(
            model_name='responsecontext',
            name='parent',
            field=modelcluster.fields.ParentalKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Page'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='responsecontext',
            name='resources',
            field=wagtail.wagtailcore.fields.StreamField((), default=[]),
        ),
        migrations.AddField(
            model_name='responsecontext',
            name='single_submission',
            field=models.BooleanField(default=False, help_text='If set, students will be allowed to send only a single response.', verbose_name='single submission'),
        ),
        migrations.AlterField(
            model_name='responsecontext',
            name='name',
            field=models.CharField(blank=True, help_text='A unique identifier.', max_length=140, verbose_name='name'),
        ),
        migrations.AlterUniqueTogether(
            name='responsecontext',
            unique_together=set([('parent', 'name')]),
        ),
    ]
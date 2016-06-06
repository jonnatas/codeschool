# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 12:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cs_questions', '0012_remove_quizresponse_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileFreeAnswerQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cs_questions.Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('cs_questions.question',),
        ),
        migrations.RenameField(
            model_name='booleanquestion',
            old_name='answer',
            new_name='answer_key',
        ),
        migrations.RenameField(
            model_name='stringmatchquestion',
            old_name='answer',
            new_name='answer_key',
        ),
    ]
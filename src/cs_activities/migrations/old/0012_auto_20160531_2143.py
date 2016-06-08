# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 00:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cs_activities', '0011_auto_20160531_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradingMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('family', models.CharField(blank=True, max_length=20)),
                ('data', models.TextField()),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='response',
            name='final_grade',
            field=models.DecimalField(blank=True, decimal_places=3, help_text="Similar to given_grade, but can account for additional factors such as delay penalties or for any other reason the teacher may want to override the student's grade.", max_digits=6, null=True, verbose_name='Final grade'),
        ),
        migrations.AlterField(
            model_name='response',
            name='given_grade',
            field=models.DecimalField(blank=True, decimal_places=3, help_text='This grade is given by the auto-grader and represents the grade for the response before accounting for any bonuses or penalties.', max_digits=6, null=True, verbose_name='Percentage of maximum grade'),
        ),
        migrations.AlterUniqueTogether(
            name='responsegroup',
            unique_together=set([('user', 'activity')]),
        ),
    ]
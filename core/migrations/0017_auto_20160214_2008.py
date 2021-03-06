# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 20:08
from __future__ import unicode_literals

import django_date_extensions.fields
from django.db import migrations, models

import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20151206_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='is_story',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='contactemail',
            name='contact_type',
            field=models.CharField(choices=[('chapter', 'Django Girls Local Organizers'), ('support', 'Django Girls HQ (Support Team)')], default='chapter', max_length=20, verbose_name='Who do you want to contact?'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=django_date_extensions.fields.ApproximateDateField(max_length=10, null=True, validators=[core.models.validate_approximatedate]),
        ),
        migrations.AlterField(
            model_name='story',
            name='image',
            field=models.ImageField(null=True, upload_to='stories/'),
        ),
    ]

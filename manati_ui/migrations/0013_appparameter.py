# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-12 16:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
from manati_ui.models import AppParameter


def create_virus_total_api_key(apps, schema_editor):
    # using my virus total account (raulbeni@gmail.com) api key by default
    AppParameter.objects.create(key=AppParameter.KEY_OPTIONS.virus_total_key_api,
                                value='efc4346703100a29d72e72c2d91d8b9c7f25bd7c59a5bb9309918b91729220d5')


class Migration(migrations.Migration):

    dependencies = [
        ('manati_ui', '0012_webloghistory_old_verdict'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='updated_at')),
                ('key', models.CharField(choices=[('virus_total_key_api', 'Virus Total Key API')], default='', max_length=20)),
                ('value', models.CharField(default='', max_length=255)),
            ],
            options={
                'db_table': 'manati_app_parameters',
            },
        ),
        migrations.RunPython(create_virus_total_api_key),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv
import os

from django.db import migrations, models


def import_grants(apps, schema_editor):
    Grant = apps.get_model('projects', 'Grant')
    filename = 'data/tbl_LU_Grants.csv'
    if os.path.exists(filename):
        with open(filename) as f:
            fieldnames = ['id', 'title', 'code', 'description', 'sort_order']
            reader = csv.DictReader(f, fieldnames=fieldnames)
            for r in reader:
                r['sort_order'] = None
                g = Grant(**r)
                g.save()


def remove_grants(apps, schema_editor):
    Grant = apps.get_model('projects', 'Grant')
    Grant.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_initial_grant'),
    ]

    operations = [
        migrations.RunPython(import_grants, remove_grants),
    ]

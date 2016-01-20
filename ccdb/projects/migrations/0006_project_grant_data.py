# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv
import os

from django.db import migrations, models


def import_project_grant(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    Grant = apps.get_model('projects', 'Grant')
    filename = 'data/tbl_HASH_Project_Grants.csv'
    if os.path.exists(filename):
        with open(filename) as f:
            fieldnames = ['project', 'grant']
            reader = csv.DictReader(f, fieldnames=fieldnames)
            for r in reader:
                p = Project.objects.get(id=r['project'])
                g = Grant.objects.get(id=r['grant'])
                p.grants.add(g)
                p.save()


def remove_project_grant(apps, schema_editor):
    Grant = apps.get_model('projects', 'Grant')
    Grant.projects.clear()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_grant_projects'),
    ]

    operations = [
        migrations.RunPython(import_project_grant, remove_project_grant),
    ]

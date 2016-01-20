# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv
import os

from django.db import migrations, models


def import_projects(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    filename = 'data/tbl_LU_Projects.csv'
    if os.path.exists(filename):
        with open(filename) as f:
            fieldnames = ['id', 'name', 'code', 'iacuc_number',
                'description', 'sort_order']
            reader = csv.DictReader(f, fieldnames=fieldnames)
            for r in reader:
                r['sort_order'] = int(float(r['sort_order']))
                p = Project(**r)
                p.save()


def remove_projects(apps, schema_editor):
    print("removing projects...")
    Project = apps.get_model("projects", "Project")
    Project.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial_project'),
    ]

    operations = [
        migrations.RunPython(import_projects, remove_projects),
    ]

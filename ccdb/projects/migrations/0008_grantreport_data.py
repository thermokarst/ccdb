# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv
import os
from datetime import datetime

from django.db import migrations, models


def import_grantreport(apps, schema_editor):
    GrantReport = apps.get_model('projects', 'GrantReport')
    Grant = apps.get_model('projects', 'Grant')
    filename = 'data/tbl_LU_Grant_Reports.csv'
    if os.path.exists(filename):
        with open(filename) as f:
            fieldnames = ['id', 'grant_id', 'title', 'report_type', 'description',
                'due_date', 'submitted_date', 'attachment', 'sort_order']
            reader = csv.DictReader(f, fieldnames=fieldnames)
            for r in reader:
                r['sort_order'] = None
                r['due_date'] = datetime.strptime(' '.join(r['due_date'].split(' AKDT ')), '%a %b %d %H:%M:%S %Y')
                r['submitted_date'] = None
                grant_id = r.pop('grant_id')
                g = Grant.objects.get(id=grant_id)
                gr = GrantReport(grant=g, **r)
                gr.save()


def remove_grantreport(apps, schema_editor):
    GrantReport = apps.get_model('projects', 'GrantReport')
    GrantReport.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_initial_grantreport'),
    ]

    operations = [
        migrations.RunPython(import_grantreport, remove_grantreport),
    ]

import os
import shutil

from django.core.management.base import BaseCommand

import requests

from ccdb.utils.data_import import setup_sqlite
from ccdb.projects.models import Project, Grant, GrantReport


class Command(BaseCommand):
    help = 'Imports prior data into the DB'

    def add_arguments(self, parser):
        parser.add_argument('manifest_url', type=str)

    def handle(self, **options):
        _fetch_data(options['manifest_url'], self.stdout.write)
        self.stdout.write('Fetched data')
        _import_data()
        self.stdout.write('Imported data')


def _fetch_data(url, write):
    data_dir = 'data/'
    r = requests.get(url)
    files = r.json()
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    for f in files['files']:
        p = ''.join([data_dir, f.split('/')[-1]])
        if not os.path.exists(p):
            write('Grabbing {}'.format(p))
            r = requests.get(f, stream=True)
            with open(p, 'wb') as out_file:
                for chunk in r:
                    out_file.write(chunk)


def _import_data():
    c = setup_sqlite()
    if c:
        # Projects
        for r in c.execute('SELECT * FROM tbl_lu_projects;'):
            p = Project(id=r[0], name=r[1], code=r[2], iacuc_number=r[3],
                description=r[4], sort_order=r[5])
            p.save()

        # Grants
        for r in c.execute('SELECT * FROM tbl_lu_grants;'):
            g = Grant(id=r[0], title=r[1], code=r[2],
                description=r[3], sort_order=r[4])
            g.save()

        # Project-Grants
        for r in c.execute('SELECT * FROM tbl_hash_project_grants;'):
            p = Project.objects.get(id=r[0])
            g = Grant.objects.get(id=r[1])
            p.grants.add(g)
            p.save()

        # Grant Reports
        q = '''
               SELECT *, report_due_date AS "due_date [dtdt]"
               FROM tbl_lu_grant_reports;
            '''
        for r in c.execute(q):
            g = Grant.objects.get(id=r[0])
            gr = GrantReport(grant=g, title=r[1], report_type=r[2],
                description=r[3], due_date=r[8], submitted_date=r[5],
                attachment=r[6], sort_order=r[7])
            gr.save()

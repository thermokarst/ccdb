import os
import shutil

from django.core.management.base import BaseCommand
from django.db import IntegrityError

import requests

from ccdb.utils.data_import import setup_sqlite
from ccdb.projects.models import Project, Grant, GrantReport
from ccdb.misc.models import MeasurementUnit, MeasurementType, Container, \
    Material, Color
from ccdb.locations.models import Region, Site, MunicipalLocation, \
    StudyLocation, StorageLocation


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
            # No PK field in Andre's file
            gr = GrantReport(grant_id=r[0], title=r[1], report_type=r[2],
                description=r[3], due_date=r[8], submitted_date=r[5],
                attachment=r[6], sort_order=r[7])
            try:
                gr.save()
            except IntegrityError:
                pass

        # Measurement Units
        for r in c.execute('SELECT * FROM tbl_lu_measurement_units;'):
            mu = MeasurementUnit(id=r[0], name=r[1], code=r[2],
                unit_class=r[3], description=r[4], sort_order=r[5])
            mu.save()

        # Measurement Types
        for r in c.execute('SELECT * FROM tbl_lu_measurement_types;'):
            mt = MeasurementType(id=r[0], name=r[1], code=r[2],
                measurement_type_class=r[3], description=r[4],
                default_measurement_unit_id=r[5], sort_order=r[6])
            mt.save()

        # Materials
        for r in c.execute('SELECT * FROM tbl_lu_materials;'):
            m = Material(id=r[0], name=r[1], code=r[2], material_class=r[3],
                description=r[4], sort_order=r[5])
            m.save()

        # Colors
        for r in c.execute('SELECT * FROM tbl_lu_colors;'):
            cl = Color(id=r[0], name=r[1], code=r[2],
                color_number=r[3], sort_order=r[4])
            cl.save()

        # Containers
        for r in c.execute('SELECT * FROM tbl_lu_containers;'):
            cl = Container(id=r[0], name=r[1], code=r[2], application=r[3],
                color_id=r[4], material_id=r[5], volume=r[6],
                measurement_unit_id=r[7], sort_order=r[8])
            cl.save()

        # Regions
        for r in c.execute('SELECT * FROM tbl_lu_regions;'):
            re = Region(id=r[0], name=r[1], code=r[2], sort_order=r[3])
            re.save()

        # Site
        for r in c.execute('SELECT * FROM tbl_lu_sites;'):
            s = Site(region_id=r[0], id=r[1], name=r[2], code=r[3],
                description=r[4], sort_order=r[5])
            s.save()

        # Municipal Locations
        for r in c.execute('SELECT * FROM tbl_lu_municipal_locations;'):
            ml = MunicipalLocation(site_id=r[0], id=r[1], name=r[2], code=r[3],
                municipal_location_type=r[4], description=r[5], sort_order=r[6])
            ml.save()

        # Study Locations
        for r in c.execute('SELECT * FROM tbl_lu_study_locations;'):
            sl = StudyLocation(site_id=r[0], id=r[1], name=r[2], code=r[3],
                study_location_type=r[4], treatment_type=r[5],
                municipal_location_id=r[6], collecting_location=r[7],
                description=r[13], sort_order=r[14])
            sl.save()

        # Storage Location
        for r in c.execute('SELECT * FROM tbl_lu_storage_locations;'):
            bldg = "".join(e[0].upper() for e in r[2].split())
            temp_c = '20'
            if r[5]:
                temp_c = r[5]
            freezer = 'No Freezer'
            if r[4]:
                freezer = r[4]
            code = " ".join([bldg, str(temp_c)+'C', str(freezer)])
            sl = StorageLocation(id=r[0], facility=r[1], building=r[2],
                room=r[3], freezer=r[4], temp_c=r[5], code=code,
                description=r[6], sort_order=r[7])
            sl.save()

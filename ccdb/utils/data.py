import sqlite3
import os
import json

from django.conf import settings

import requests
import dateutil.parser as dp


def get_data_sources():
    manifest_url = settings.MANIFEST_URL
    if not manifest_url:
        return None
    data_dir = 'data/'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        _fetch_data(data_dir, manifest_url)
    return {
        'db0': _get_db0(),
    }


def _fetch_data(data_dir, url):
    manifest = _filename(data_dir, url)
    if not os.path.exists(manifest):
        _write_url(url, manifest)
    with open(manifest) as data:
        d = json.load(data)
        for f in d['files']:
            p = _filename(data_dir, f)
            if not os.path.exists(p):
                _write_url(f, p)


def _filename(data_dir, url):
    return ''.join([data_dir, url.split('/')[-1]])


def _write_url(url, filename):
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as outfile:
        for chunk in r:
            outfile.write(chunk)


def _get_db0():
    dbfile = 'data/CC_Database_020216.sqlite'
    return setup_sqlite(dbfile)


def dtdt(s):
    """
        This lets us parse whatever crazy date/time formats that
        come our way (looking at you, MS Access)
    """
    return dp.parse(s)


sqlite3.register_converter("dtdt", dtdt)


def setup_sqlite(dbfile):
    if os.path.exists(dbfile):
        db = sqlite3.connect(dbfile, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        db.row_factory = sqlite3.Row
        return db.cursor()
    else:
        return None

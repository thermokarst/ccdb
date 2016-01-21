import sqlite3
import os

import dateutil.parser as dp


def dtdt(s):
    return dp.parse(s)


sqlite3.register_converter("dtdt", dtdt)


def setup_sqlite():
    dbfile = 'data/CC_Database_101314.sqlite'
    if os.path.exists(dbfile):
        db = sqlite3.connect(dbfile, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        db.row_factory = sqlite3.Row
        return db.cursor()
    else:
        return None

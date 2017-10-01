from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('collections_ccdb', '0003_DATA_fix_display_names'),
    ]

    operations = [
        migrations.RunSQL(
            "SELECT setval('collections_ccdb_adfgpermit_id_seq', ("
            "SELECT MAX(id)+1 FROM collections_ccdb_adfgpermit), false)",

            "SELECT setval('collections_ccdb_adfgpermit_id_seq', 1, false)"
        ),

        migrations.RunSQL(
            "SELECT setval('collections_ccdb_collection_id_seq', ("
            "SELECT MAX(id)+1 FROM collections_ccdb_collection), false)",

            "SELECT setval('collections_ccdb_collection_id_seq', 1, false)"
        ),

        migrations.RunSQL(
            "SELECT setval('collections_ccdb_collectionmethod_id_seq', ("
            "SELECT MAX(id)+1 FROM collections_ccdb_collectionmethod), false)",

            "SELECT setval('collections_ccdb_collectionmethod_id_seq', 1, "
            "false)"
        ),

        migrations.RunSQL(
            "SELECT setval('collections_ccdb_collectiontrap_id_seq', ("
            "SELECT MAX(id)+1 FROM collections_ccdb_collectiontrap), false)",

            "SELECT setval('collections_ccdb_collectiontrap_id_seq', 1, false)"
        ),

        migrations.RunSQL(
            "SELECT setval('collections_ccdb_collectiontype_id_seq', ("
            "SELECT MAX(id)+1 FROM collections_ccdb_collectiontype), false)",

            "SELECT setval('collections_ccdb_collectiontype_id_seq', 1, false)"
        ),

        migrations.RunSQL(
            "SELECT setval('collections_ccdb_datasheetattachment_id_seq', ("
            "SELECT MAX(id)+1 FROM collections_ccdb_datasheetattachment), "
            "false)",

            "SELECT setval('collections_ccdb_datasheetattachment_id_seq', 1, "
            "false)"
        ),

        migrations.RunSQL(
            "SELECT setval('collections_ccdb_flaw_id_seq', ("
            "SELECT MAX(id)+1 FROM collections_ccdb_flaw), false)",

            "SELECT setval('collections_ccdb_flaw_id_seq', 1, false)"
        ),

    ]

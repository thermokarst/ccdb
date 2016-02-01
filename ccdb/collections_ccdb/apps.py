from django.apps import AppConfig


# This is needed because 'collections' is part of the Python Std Lib
class CollectionsAppConfig(AppConfig):
    name = 'ccdb.collections_ccdb'
    verbose_name = 'Collections'

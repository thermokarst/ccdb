from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    def migrate(apps, schema_editor):
        Sex = apps.get_model('species', 'Sex')
        CollectionSpecies = apps.get_model('species', 'CollectionSpecies')

        for cs in CollectionSpecies.objects.all():
            if cs.old_sex:
                if cs.old_sex == 'both':
                    s = 'mixed'
                elif cs.old_sex not in ['male', 'female', 'mixed', 'unknown']:
                    s = 'unknown'
                else:
                    s = cs.old_sex
                cs.sex = Sex.objects.get(name=s)
                cs.save()

    def rollback(apps, schema_editor):
        CollectionSpecies = apps.get_model('species', 'CollectionSpecies')

        for cs in CollectionSpecies.objects.all():
            if cs.sex:
                cs.sex = None
            cs.old_sex = ''
            cs.save()

    dependencies = [
        ('species', '0004_sex'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectionspecies',
            old_name='sex',
            new_name='old_sex',
        ),
        migrations.RenameField(
            model_name='trapspecies',
            old_name='sex',
            new_name='old_sex',
        ),
        migrations.AddField(
            model_name='collectionspecies',
            name='sex',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE,
                related_name='collection_species', to='species.Sex'),
        ),
        migrations.AddField(
            model_name='trapspecies',
            name='sex',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE,
                related_name='trap_species', to='species.Sex'),
        ),
        migrations.RunPython(migrate, rollback),
        migrations.RemoveField(
            model_name='collectionspecies',
            name='old_sex',
        ),
        migrations.RemoveField(
            model_name='trapspecies',
            name='old_sex',
        ),
    ]

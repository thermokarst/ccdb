from django.db import migrations, models
from django.forms import modelform_factory


class Migration(migrations.Migration):
    def migrate(apps, schema_editor):
        Sex = apps.get_model('species', 'Sex')
        SexForm = modelform_factory(Sex, fields=('name', 'sort_order'))
        for i, s in enumerate(['male', 'female', 'mixed', 'unknown']):
            form = SexForm(dict(name=s, sort_order=i))
            if form.is_valid():
                form.save()
            else:
                print('sex', form.errors.as_data())

    def rollback(apps, schema_editor):
        Sex = apps.get_model('species', 'Sex')
        Sex.objects.all().delete()

    dependencies = [
        ('species', '0003_DATA_reset_sequences'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'sex',
                'ordering': ['sort_order'],
            },
        ),
        migrations.RunPython(migrate, rollback),
    ]

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=10)),
                ('iacuc_number', models.CharField(blank=True, max_length=25)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('name', 'code')]),
        ),
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('code', models.CharField(blank=True, max_length=10)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='grant',
            unique_together=set([('title', 'code')]),
        ),
        migrations.AddField(
            model_name='grant',
            name='projects',
            field=models.ManyToManyField(related_name='grants', to='projects.Project'),
        ),
        migrations.CreateModel(
            name='GrantReport',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('report_type', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('submitted_date', models.DateField(blank=True, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='projects/grants/grant_report_attachments/%Y/%m/%d')),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('grant', models.ForeignKey(to='projects.Grant')),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='grantreport',
            unique_together=set([('grant', 'title', 'due_date')]),
        ),
        migrations.AlterField(
            model_name='grantreport',
            name='grant',
            field=models.ForeignKey(related_name='reports', to='projects.Grant'),
        ),
    ]

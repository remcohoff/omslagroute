# Generated by Django 2.2.10 on 2020-02-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('documents', '0013_auto_20200227_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Naam')),
                ('order', models.IntegerField(verbose_name='Sorteer')),
                ('documents', models.ManyToManyField(blank=True, to='documents.Document', verbose_name='Documenten')),
            ],
            options={
                'verbose_name': 'Moment',
                'verbose_name_plural': 'Momenten',
                'ordering': ('-order',),
            },
        ),
    ]

# Generated by Django 2.2.10 on 2020-03-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='name_abbreviation',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Naam afkorting'),
        ),
    ]

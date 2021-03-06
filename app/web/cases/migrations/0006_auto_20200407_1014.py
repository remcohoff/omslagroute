# Generated by Django 2.2.10 on 2020-04-07 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0005_case_kinderen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='centrale_toegang_naam',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'CTBW (Centrale Toegang Begeleid Wonen)'), (2, 'CTMO (Centrale Toegang Maatschappelijke Opvang)'), (3, 'CTMOJ (Centrale Toegang Maatschappelijke Opvang Jeugd)'), (4, 'CTMOG (Centrale Toegang Maatschappelijke Opvang Gezin)'), (5, 'Jeugdhulp'), (6, 'CTBWLvB (Centrale Toegang Begeleid Wonen Licht Verstandelijke Beperking)')], null=True, verbose_name='Naam centrale toegang'),
        ),
        migrations.AlterField(
            model_name='case',
            name='centrale_toegang_trajectwijziging_ed',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'CTBW (Centrale Toegang Begeleid Wonen)'), (2, 'CTMO (Centrale Toegang Maatschappelijke Opvang)'), (3, 'CTMOJ (Centrale Toegang Maatschappelijke Opvang Jeugd)'), (4, 'CTMOG (Centrale Toegang Maatschappelijke Opvang Gezin)'), (5, 'Jeugdhulp'), (6, 'CTBWLvB (Centrale Toegang Begeleid Wonen Licht Verstandelijke Beperking)')], null=True, verbose_name='Toegang en trajectwijziging / doorstroom en jeugdzorg'),
        ),
        migrations.AlterField(
            model_name='case',
            name='jonger_dan_26',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Nee'), (2, 'Ja: standaard plaatsing jongerenwoning (5 jaar contract bij omklap)'), (3, 'Ja: plaatsing reguliere woning noodzakelijk (onbepaalde tijd bij omklap)'), (4, 'Ja: Plaatsing in een project (Licht dit toe bij de volgende vraag)')], null=True, verbose_name='Plaatsing jonger dan 26 jaar'),
        ),
    ]

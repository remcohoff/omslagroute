# Generated by Django 2.2.10 on 2020-03-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0003_auto_20200304_1315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moment',
            options={'ordering': ('order',), 'verbose_name': 'Moment', 'verbose_name_plural': 'Momenten'},
        ),
        migrations.AlterField(
            model_name='moment',
            name='order',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='Sorteer'),
        ),
    ]
# Generated by Django 2.2.10 on 2020-03-25 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_organization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='organization',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Gebruiker'),
        ),
    ]

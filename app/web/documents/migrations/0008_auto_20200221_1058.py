# Generated by Django 2.2.9 on 2020-02-21 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0007_auto_20200221_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Titel')),
                ('uploaded_file', models.FileField(upload_to='uploads', verbose_name='Bestand')),
                ('uploaded', models.DateTimeField(auto_now_add=True, verbose_name='Upload datum/tijd')),
                ('saved', models.DateTimeField(auto_now=True, verbose_name='Opgeslagen datum/tijd')),
            ],
            options={
                'verbose_name': 'Bestand',
                'verbose_name_plural': 'Bestanden',
                'ordering': ('-uploaded',),
            },
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ('type_name',), 'verbose_name': 'Bestands type', 'verbose_name_plural': 'Bestands types'},
        ),
        migrations.RemoveField(
            model_name='document',
            name='document_type',
        ),
        migrations.RemoveField(
            model_name='document',
            name='saved',
        ),
        migrations.RemoveField(
            model_name='document',
            name='title',
        ),
        migrations.RemoveField(
            model_name='document',
            name='uploaded',
        ),
        migrations.RemoveField(
            model_name='document',
            name='uploaded_file',
        ),
        migrations.AddField(
            model_name='document',
            name='icon',
            field=models.CharField(blank=True, choices=[('form', 'form'), ('checklist', 'checklist')], max_length=50, null=True, verbose_name='Icon'),
        ),
        migrations.AddField(
            model_name='document',
            name='type_name',
            field=models.CharField(default=0, max_length=100, verbose_name='Type naam'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DocumentType',
        ),
        migrations.AddField(
            model_name='documentversion',
            name='document_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_to_document_version', to='documents.Document', verbose_name='Document versie'),
        ),
    ]

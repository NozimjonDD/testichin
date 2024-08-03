# Generated by Django 3.2.7 on 2021-10-29 10:01

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import structure.models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_auto_20211023_1518'),
        ('structure', '0018_organization_staffs'),
    ]

    operations = [
        migrations.CreateModel(
            name='InnovationTerritory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, max_length=255, populate_from=structure.models.InnovationTerritory.get_populate, unique=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='staff_images/')),
                ('population', models.CharField(blank=True, max_length=255, null=True)),
                ('area', models.CharField(blank=True, max_length=255, null=True)),
                ('created_workplace', models.CharField(blank=True, max_length=255)),
                ('innovation_projects', models.CharField(blank=True, max_length=255, null=True)),
                ('technology_transfer', models.CharField(blank=True, max_length=255, null=True)),
                ('order', models.PositiveSmallIntegerField(default=1)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='innovation_districts', to='common.district')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='innovation_districts', to='common.region')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
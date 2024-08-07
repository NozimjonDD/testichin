# Generated by Django 3.2.7 on 2021-10-12 09:59

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import structure.models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_alter_interactiveservice_url'),
        ('structure', '0009_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='InnovationCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_oz', models.CharField(max_length=255, null=True)),
                ('title_qr', models.CharField(max_length=255, null=True)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, max_length=255, populate_from=structure.models.InnovationCenter.get_populate, unique=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('address_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('address_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('address_en', models.CharField(blank=True, max_length=255, null=True)),
                ('address_oz', models.CharField(blank=True, max_length=255, null=True)),
                ('address_qr', models.CharField(blank=True, max_length=255, null=True)),
                ('boss', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='innovation_center_boss', to='structure.staff')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='innovation_centers', to='common.district')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

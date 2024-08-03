# Generated by Django 3.2.7 on 2021-10-11 12:35

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import structure.models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0008_alter_management_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
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
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, max_length=255, populate_from=structure.models.Organization.get_populate, unique=True)),
                ('photo', models.ImageField(upload_to='organizations_photos/')),
                ('web', models.URLField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('address_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('address_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('address_en', models.CharField(blank=True, max_length=255, null=True)),
                ('address_oz', models.CharField(blank=True, max_length=255, null=True)),
                ('address_qr', models.CharField(blank=True, max_length=255, null=True)),
                ('activity', models.TextField()),
                ('activity_uz', models.TextField(null=True)),
                ('activity_ru', models.TextField(null=True)),
                ('activity_en', models.TextField(null=True)),
                ('activity_oz', models.TextField(null=True)),
                ('activity_qr', models.TextField(null=True)),
                ('works', models.TextField()),
                ('works_uz', models.TextField(null=True)),
                ('works_ru', models.TextField(null=True)),
                ('works_en', models.TextField(null=True)),
                ('works_oz', models.TextField(null=True)),
                ('works_qr', models.TextField(null=True)),
                ('boss', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organization_boss', to='structure.staff')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

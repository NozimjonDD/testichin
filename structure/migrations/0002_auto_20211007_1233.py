# Generated by Django 3.2.7 on 2021-10-07 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='management',
            name='management_reception_days',
        ),
        migrations.RemoveField(
            model_name='management',
            name='management_reception_days_en',
        ),
        migrations.RemoveField(
            model_name='management',
            name='management_reception_days_oz',
        ),
        migrations.RemoveField(
            model_name='management',
            name='management_reception_days_qr',
        ),
        migrations.RemoveField(
            model_name='management',
            name='management_reception_days_ru',
        ),
        migrations.RemoveField(
            model_name='management',
            name='management_reception_days_uz',
        ),
    ]

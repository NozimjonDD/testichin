# Generated by Django 3.2.7 on 2021-10-11 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0007_auto_20211009_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='management',
            options={'ordering': ['order']},
        ),
    ]

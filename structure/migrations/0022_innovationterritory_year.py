# Generated by Django 3.2.7 on 2021-10-30 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0021_auto_20211030_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='innovationterritory',
            name='year',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

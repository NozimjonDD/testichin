# Generated by Django 3.2.7 on 2021-10-19 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0017_auto_20211018_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='staffs',
            field=models.ManyToManyField(blank=True, to='structure.Staff'),
        ),
    ]
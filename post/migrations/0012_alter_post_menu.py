# Generated by Django 3.2.7 on 2021-11-10 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20211102_1356'),
        ('post', '0011_auto_20211109_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='menu',
            field=models.ManyToManyField(blank=True, related_name='posts', to='menu.Menu'),
        ),
    ]

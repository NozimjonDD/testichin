# Generated by Django 3.2.7 on 2021-11-08 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20211030_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
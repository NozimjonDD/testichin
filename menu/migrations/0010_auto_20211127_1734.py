# Generated by Django 3.2.7 on 2021-11-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_auto_20211126_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='menuattachment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='menuimage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-26 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_menu_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

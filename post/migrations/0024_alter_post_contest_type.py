# Generated by Django 3.2.7 on 2021-12-20 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_alter_post_contest_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contest_type',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Practical'), (2, 'Fundamental'), (3, 'Innovation'), (4, 'Startup'), (5, 'Cooperation'), (6, 'Practical innovation')], null=True),
        ),
    ]
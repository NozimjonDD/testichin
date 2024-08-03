# Generated by Django 3.2.7 on 2021-12-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0022_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contest_type',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Practical'), (2, 'Fundamental'), (3, 'Innovation'), (4, 'Startup'), (5, 'Cooperation'), (6, 'Practical innovation')], default=None, null=True),
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-30 15:03

import autoslug.fields
from django.db import migrations
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, max_length=150, null=True, populate_from=post.models.Tag.get_populate, unique=True),
        ),
    ]

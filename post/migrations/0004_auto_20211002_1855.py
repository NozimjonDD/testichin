# Generated by Django 3.2.7 on 2021-10-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_tag_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='contest_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='contest_tour',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

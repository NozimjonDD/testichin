# Generated by Django 3.2.7 on 2022-01-11 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0025_contestbutton'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestbutton',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contestbutton',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contestbutton',
            name='title_oz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contestbutton',
            name='title_qr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contestbutton',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contestbutton',
            name='title_uz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

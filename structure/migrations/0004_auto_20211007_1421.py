# Generated by Django 3.2.7 on 2021-10-07 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0003_management_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='management',
            name='title',
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='management',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='management',
            name='title_oz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='management',
            name='title_qr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='management',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='management',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

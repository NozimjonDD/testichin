# Generated by Django 3.2.7 on 2021-10-13 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0012_auto_20211012_1614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='management',
            options={'ordering': ['order', 'type']},
        ),
        migrations.AddField(
            model_name='staff',
            name='is_vacant',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='inner_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='staff_images/'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-30 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0022_innovationterritory_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innovationterritory',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='innovationterritory_images/'),
        ),
    ]
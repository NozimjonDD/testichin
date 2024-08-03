# Generated by Django 3.2.7 on 2021-10-30 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0021_auto_20211030_1141'),
        ('post', '0007_auto_20211018_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='innovation_territory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='structure.innovationterritory'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-12-08 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0034_auto_20211208_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='division',
            name='boss',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='structure.staff'),
        ),
        migrations.AlterField(
            model_name='division',
            name='staffs',
            field=models.ManyToManyField(blank=True, related_name='divisions', through='structure.DivisionStaffsWithOrder', to='structure.Staff'),
        ),
    ]

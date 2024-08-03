# Generated by Django 3.2.7 on 2021-12-01 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0031_alter_staff_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='DivisionStaffsWithOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(default=1)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.division')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.staff')),
            ],
        ),
        migrations.AddField(
            model_name='division',
            name='staffs',
            field=models.ManyToManyField(blank=True, related_name='division_staffs', through='structure.DivisionStaffsWithOrder', to='structure.Staff'),
        ),
    ]
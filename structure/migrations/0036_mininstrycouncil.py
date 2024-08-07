# Generated by Django 3.2.7 on 2021-12-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0035_auto_20211208_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='MininstryCouncil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('content_uz', models.TextField(null=True)),
                ('content_ru', models.TextField(null=True)),
                ('content_en', models.TextField(null=True)),
                ('content_oz', models.TextField(null=True)),
                ('content_qr', models.TextField(null=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

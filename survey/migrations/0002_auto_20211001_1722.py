# Generated by Django 3.2.7 on 2021-10-01 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='question_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='question_oz',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='question_qr',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='question_ru',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='question_uz',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='surveyvariant',
            name='text_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='surveyvariant',
            name='text_oz',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='surveyvariant',
            name='text_qr',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='surveyvariant',
            name='text_ru',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='surveyvariant',
            name='text_uz',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
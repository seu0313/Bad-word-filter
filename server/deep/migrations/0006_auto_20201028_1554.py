# Generated by Django 3.0.8 on 2020-10-28 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deep', '0005_auto_20201028_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deep',
            name='processed_file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='처리된파일'),
        ),
        migrations.AlterField(
            model_name='deep',
            name='video_file',
            field=models.FileField(null=True, upload_to='', verbose_name='파일'),
        ),
    ]
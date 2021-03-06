# Generated by Django 3.1.3 on 2022-01-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lectureinfo',
            name='lect_explan',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lectureinfo',
            name='lect_fee',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lectureinfo',
            name='lect_fee_explan',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lectureinfo',
            name='lect_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lectureinfo',
            name='lect_yoil',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lectureinfo',
            name='week_cnt',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

# Generated by Django 3.1.3 on 2022-01-02 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_nm', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lectureinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp_nm', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('lect_nm', models.CharField(max_length=255)),
                ('lect_explan', models.TextField()),
                ('lect_yoil', models.CharField(max_length=50)),
                ('lect_time', models.CharField(max_length=50)),
                ('week_cnt', models.CharField(max_length=50)),
                ('lect_fee', models.CharField(max_length=50)),
                ('lect_fee_explan', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('season_nm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='season_name', to='lecture.season')),
            ],
        ),
    ]

# Generated by Django 3.1.3 on 2022-02-17 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0018_yoil'),
    ]

    operations = [
        migrations.CreateModel(
            name='time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_nm', models.CharField(max_length=50)),
                ('num', models.IntegerField()),
            ],
        ),
    ]

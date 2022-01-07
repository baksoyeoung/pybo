# Generated by Django 3.1.3 on 2022-01-07 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0003_lectureinfo_lect_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='lectureinfo',
            name='teacher',
        ),
        migrations.AddField(
            model_name='lectureinfo',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]

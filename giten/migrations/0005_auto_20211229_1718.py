# Generated by Django 3.1.3 on 2021-12-29 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giten', '0004_gitenstudent_campis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gitenstudent',
            name='monthis',
            field=models.CharField(default='', max_length=50),
        ),
    ]

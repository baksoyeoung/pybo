# Generated by Django 3.1.3 on 2022-01-07 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0005_auto_20220107_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='num',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]

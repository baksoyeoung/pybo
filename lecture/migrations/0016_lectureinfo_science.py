# Generated by Django 3.1.3 on 2022-01-15 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0015_science'),
    ]

    operations = [
        migrations.AddField(
            model_name='lectureinfo',
            name='science',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
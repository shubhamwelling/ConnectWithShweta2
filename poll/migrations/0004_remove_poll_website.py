# Generated by Django 3.1.5 on 2021-02-01 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20210131_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='website',
        ),
    ]

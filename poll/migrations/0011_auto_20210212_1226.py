# Generated by Django 3.1.6 on 2021-02-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0010_auto_20210212_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='option_five',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='poll',
            name='option_four',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='poll',
            name='option_one',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='poll',
            name='option_three',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='poll',
            name='option_two',
            field=models.CharField(default='', max_length=60),
        ),
    ]

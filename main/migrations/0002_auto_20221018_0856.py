# Generated by Django 3.2.13 on 2022-10-18 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='check_in',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='check_out',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]

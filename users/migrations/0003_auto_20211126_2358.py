# Generated by Django 3.2.6 on 2021-11-26 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211126_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]

# Generated by Django 3.2.6 on 2021-11-26 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='location',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
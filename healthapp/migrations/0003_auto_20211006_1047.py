# Generated by Django 3.2.8 on 2021-10-06 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0002_auto_20211006_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='repeats',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='health',
            name='set',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
# Generated by Django 3.2.6 on 2021-08-19 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0006_auto_20210818_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='participants',
            field=models.ManyToManyField(blank=True, to='meetups.participant'),
        ),
    ]

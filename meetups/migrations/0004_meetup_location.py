# Generated by Django 3.2.6 on 2021-08-18 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0003_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='location',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='meetups.location'),
            preserve_default=False,
        ),
    ]

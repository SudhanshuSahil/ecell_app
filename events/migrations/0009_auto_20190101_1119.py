# Generated by Django 2.0.5 on 2019-01-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_event_venue_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='venue_name',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]

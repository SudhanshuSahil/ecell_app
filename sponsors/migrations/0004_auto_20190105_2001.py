# Generated by Django 2.0.5 on 2019-01-05 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0003_auto_20190102_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='photo',
            new_name='photo_url',
        ),
        migrations.RenameField(
            model_name='sponsor',
            old_name='link',
            new_name='website_link',
        ),
    ]

# Generated by Django 2.0.5 on 2019-01-02 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0002_auto_20190102_1801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='company',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='sponsor',
            old_name='linkedin_link',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='sponsor',
            old_name='photo_url',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='designation',
        ),
    ]

# Generated by Django 2.0.5 on 2018-06-12 23:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('str_id', models.CharField(editable=False, max_length=58, null=True)),
                ('time_of_creation', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('speaker', models.CharField(max_length=50)),
                ('speaker_image_url', models.URLField(blank=True, null=True)),
                ('speaker_website_url', models.URLField(blank=True, null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('all_day', models.BooleanField(default=False)),
                ('archived', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-time_of_creation',),
                'verbose_name_plural': 'Events',
                'verbose_name': 'Event',
            },
        ),
    ]

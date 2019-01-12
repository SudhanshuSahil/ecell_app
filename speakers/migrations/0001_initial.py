# Generated by Django 2.0.5 on 2019-01-06 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('limkedin_link', models.URLField(blank=True, default=None, null=True)),
                ('photo_url', models.URLField(blank=True, default=None, null=True)),
                ('company', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('designation', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Speaker',
                'ordering': ('-created_at',),
                'verbose_name_plural': 'Speaker',
            },
        ),
    ]

# Generated by Django 3.1.5 on 2021-02-03 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='media/ytubers/%Y/%m/')),
                ('video_url', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('hright', models.IntegerField()),
                ('crew', models.CharField(max_length=255)),
                ('camera_type', models.CharField(max_length=255)),
                ('subs_count', models.IntegerField()),
                ('category', models.CharField(max_length=255)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]

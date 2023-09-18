# Generated by Django 4.2.5 on 2023-09-18 20:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('header', models.CharField(max_length=200)),
                ('banner', models.ImageField(upload_to='media')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]

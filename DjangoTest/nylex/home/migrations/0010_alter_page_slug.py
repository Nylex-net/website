# Generated by Django 4.2.4 on 2023-09-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_page_slug_alter_page_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(),
        ),
    ]

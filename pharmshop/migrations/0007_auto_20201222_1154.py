# Generated by Django 3.0.2 on 2020-12-22 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmshop', '0006_remove_category_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='url',
            new_name='slug',
        ),
    ]

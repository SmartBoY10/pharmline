# Generated by Django 3.0.2 on 2020-12-20 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('tagline', models.CharField(max_length=100, verbose_name='Слоган')),
                ('company_year', models.CharField(max_length=100, verbose_name='История нашего бизнеса ...')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'О компании',
                'verbose_name_plural': 'О компании',
            },
        ),
        migrations.CreateModel(
            name='Consulting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('tagline', models.CharField(max_length=100, verbose_name='Слоган')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Консультация',
                'verbose_name_plural': 'Консультации',
            },
        ),
    ]

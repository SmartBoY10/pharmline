# Generated by Django 3.0.2 on 2020-12-20 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catolog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('tagline', models.CharField(max_length=100, verbose_name='Слоган')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталоги',
            },
        ),
    ]

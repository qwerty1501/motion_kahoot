# Generated by Django 3.2.9 on 2022-06-07 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='point',
            field=models.PositiveIntegerField(default=0, verbose_name='Очко'),
        ),
        migrations.AddField(
            model_name='question',
            name='point',
            field=models.PositiveIntegerField(default=1000, verbose_name='Очко'),
        ),
    ]

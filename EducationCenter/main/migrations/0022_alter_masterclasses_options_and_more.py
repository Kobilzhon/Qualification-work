# Generated by Django 4.2.1 on 2023-05-18 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_masterclasses_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='masterclasses',
            options={'verbose_name': 'Мастер класс', 'verbose_name_plural': 'Мастер классы'},
        ),
        migrations.RemoveField(
            model_name='masterclasses',
            name='date',
        ),
        migrations.RemoveField(
            model_name='masterclasses',
            name='time',
        ),
    ]

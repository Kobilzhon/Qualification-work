# Generated by Django 4.2.1 on 2023-05-19 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_courses_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MasterClasses',
            new_name='MasterClass',
        ),
        migrations.AlterModelOptions(
            name='coursecategory',
            options={'verbose_name': 'Категория курсов', 'verbose_name_plural': 'Категория курсов'},
        ),
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-16 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_zayavka_courses_courses_show_zayavka_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='zayavka',
            name='phone_num',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]

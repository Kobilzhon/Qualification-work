# Generated by Django 4.2.1 on 2023-05-18 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_zayavka_phone_num'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Пост комментирии', 'verbose_name_plural': 'Пост комментирии'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-date',), 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='zayavka',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
    ]

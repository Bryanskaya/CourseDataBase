# Generated by Django 3.1.6 on 2021-02-03 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('login', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Логин')),
                ('pswd', models.TextField(verbose_name='Пароль')),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-10 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='Почта')),
                ('fam', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('otc', models.CharField(max_length=50, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=20, unique=True, verbose_name='Контактный телефон')),
            ],
        ),
        migrations.AlterField(
            model_name='pereval',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.user', verbose_name='Пользователь'),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
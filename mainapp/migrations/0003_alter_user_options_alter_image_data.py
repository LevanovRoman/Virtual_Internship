# Generated by Django 5.0.1 on 2024-01-10 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_user_alter_pereval_user_delete_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='image',
            name='data',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Изображение'),
        ),
    ]
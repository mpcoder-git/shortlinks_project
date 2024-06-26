# Generated by Django 5.0.3 on 2024-03-26 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('shortlink', models.CharField(max_length=100, verbose_name='Коротккая ссылка')),
                ('link', models.SlugField(verbose_name='Полная ссылка')),
                ('user', models.IntegerField(verbose_name='Код пользователя')),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
            },
        ),
    ]

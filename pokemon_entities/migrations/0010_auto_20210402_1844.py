# Generated by Django 3.1.7 on 2021-04-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_pokemon_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='photo',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='title',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, verbose_name='Имя покемона на английском'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, max_length=200, verbose_name='Имя покемона на японском'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_ru',
            field=models.CharField(default='покемон', max_length=200, verbose_name='Имя покемона на русском'),
        ),
    ]
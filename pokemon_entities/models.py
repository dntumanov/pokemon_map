from django.db import models


class Pokemon(models.Model):
    """Описание покенома"""
    title_ru = models.CharField(max_length=200, verbose_name='Имя покемона на русском', default='покемон')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='Имя покемона на английском')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='Имя покемона на японском')
    image = models.ImageField(upload_to='pokemons', null=True, blank=True, verbose_name='Ваставьте картинку для покемона')
    description = models.TextField(
        verbose_name='Описание покемона', default='', null=False, blank=True)
    previous_evolution = models.ForeignKey('Pokemon', null=True, blank=True, on_delete=models.SET_NULL,
                                           related_name='next_evolution', verbose_name='Из кого эволюционировал')

    @property
    def get_image_absolute_url(self):
        """Возвращает абсолютный путь к картинке"""
        if self.image:
            image_url = self.image.url
            return image_url

    def __str__(self):
        return '{}'.format(self.title_ru)


class PokemonEntity(models.Model):
    """Описание свойст покемона"""
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Координаты покемона: широта')
    lon = models.FloatField(verbose_name='Координаты покемона: долгота')
    appeared_at = models.DateTimeField('Появился в')
    disappeared_at = models.DateTimeField('Исчез в')
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(null=True,  blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True,  blank=True, verbose_name='Показатель атаки')
    defence = models.IntegerField(null=True,  blank=True, verbose_name='Показатель защиты')
    stamina = models.IntegerField(null=True,  blank=True, verbose_name='Показатель выносливости')

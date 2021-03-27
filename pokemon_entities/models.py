from django.db import models


class Pokemon(models.Model):
    """Описание сущности покенома"""
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='pokemons', blank=True)

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()


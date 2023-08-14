from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.TextField(max_length=200)
    image = models.ImageField(upload_to='pokemon_images/', null=True)
    description = models.TextField(max_length=1000, default="Тут должно быть описание")
    title_en = models.TextField(max_length=200, default='title')
    title_jp = models.TextField(max_length=200, default='フシギダネ')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default=1)
    lat = models.FloatField(default=None)
    lon = models.FloatField(default=None)
    appeared_at = models.DateTimeField(default=None)
    disappeared_at = models.DateTimeField(default=None)
    level = models.IntegerField(blank=True, default=1)
    health = models.IntegerField(blank=True, default=1)
    strength = models.IntegerField(blank=True, default=1)
    defence = models.IntegerField(blank=True, default=1)
    stamina = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return f"{self.pokemon.title} - ({self.lat}, {self.lon})"
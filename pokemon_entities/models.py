from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.TextField(max_length=200)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default=1)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(default=None)
    disappeared_at = models.DateTimeField(default=None)

    def __str__(self):
        return f"{self.pokemon.title} - ({self.lat}, {self.lon})"
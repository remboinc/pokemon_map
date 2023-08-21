from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название покемона')
    image = models.ImageField(upload_to='pokemon_images/', null=True, verbose_name='Изображение покемона')
    description = models.TextField(max_length=1000, verbose_name='Описание', default="Тут должно быть описание")
    title_en = models.CharField(max_length=200, default='title', verbose_name='Название на английском')
    title_jp = models.CharField(max_length=200, default='フシギダネ', verbose_name='Название на японском')
    evolution = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='related_evolution', verbose_name='Эволюция')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default=1, verbose_name='Что за покемон')
    lat = models.FloatField(default=None, verbose_name='Широта')
    lon = models.FloatField(default=None, verbose_name='Долгота')
    appeared_at = models.DateTimeField(default=None, verbose_name='Когда появился')
    disappeared_at = models.DateTimeField(default=None, verbose_name='Когда исчезнет')
    level = models.IntegerField(blank=True, default=1, verbose_name='Уровень')
    health = models.IntegerField(blank=True, default=1, verbose_name='Здоровье')
    strength = models.IntegerField(blank=True, default=1, verbose_name='Сила')
    defence = models.IntegerField(blank=True, default=1, verbose_name='Защита')
    stamina = models.IntegerField(blank=True, default=1, verbose_name='Выносливость')

    def __str__(self):
        return f"{self.pokemon.title} - ({self.lat}, {self.lon})"

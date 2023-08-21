from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название покемона')
    image = models.ImageField(upload_to='pokemon_images/', null=True, verbose_name='Изображение покемона')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    title_en = models.CharField(max_length=200, null=True, blank=True, verbose_name='Название на английском')
    title_jp = models.CharField(max_length=200, null=True, blank=True, verbose_name='Название на японском')
    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='next_evolution', verbose_name='Предыдущая эволюция')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, related_name='pokemon_entity', on_delete=models.CASCADE, verbose_name='Что за покемон')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Когда появился')
    disappeared_at = models.DateTimeField(verbose_name='Когда исчезнет')
    level = models.IntegerField(blank=True, verbose_name='Уровень')
    health = models.IntegerField(blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(blank=True, verbose_name='Сила')
    defence = models.IntegerField(blank=True, verbose_name='Защита')
    stamina = models.IntegerField(blank=True, verbose_name='Выносливость')

    def __str__(self):
        return f"{self.pokemon.title} - ({self.lat}, {self.lon})"

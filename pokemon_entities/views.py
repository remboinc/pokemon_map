import folium
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils import timezone

from pokemon_entities.models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    now = timezone.now()
    local_time = timezone.localtime(now)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons_entity = PokemonEntity.objects.filter(
        appeared_at__lte=local_time,
        disappeared_at__gte=local_time
    )
    add_pokemon(
        folium_map,
        pokemons_entity.lat,
        pokemons_entity.lon,
        image_url=request.build_absolute_uri(pokemons_entity.pokemon.image.url),
    )
    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url or DEFAULT_IMAGE_URL,
            'title_ru': pokemon.title,
        })



    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    now = timezone.now()
    local_time = timezone.localtime(now)
    pokemons_on_page = {}
    try:
        requested_pokemon = PokemonEntity.objects.get(id=pokemon_id)
        pokemons_on_page.update({
            'pokemon_id': requested_pokemon.id,
            'img_url': request.build_absolute_uri(requested_pokemon.pokemon.image.url),
            'title_ru': requested_pokemon.pokemon.title,
            'description': requested_pokemon.pokemon.description,
            "title_en": requested_pokemon.pokemon.title_en,
            "title_jp": requested_pokemon.pokemon.title_jp,
        })

        if requested_pokemon.pokemon.previous_evolution:
            related_evolution = requested_pokemon.pokemon.previous_evolution
            pokemons_on_page['previous_evolution'] = {
                'title_ru': related_evolution.title,
                'pokemon_id': related_evolution.id,
                'img_url': request.build_absolute_uri(related_evolution.image.url),
            }

        if requested_pokemon.pokemon.next_evolution.exists():
            related_evolution = requested_pokemon.pokemon.next_evolution.first()
            pokemons_on_page['next_evolution'] = {
                'title_ru': related_evolution.title,
                'pokemon_id': related_evolution.id,
                'img_url': request.build_absolute_uri(related_evolution.image.url),
            }

    except PokemonEntity.DoesNotExist:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons_entity = PokemonEntity.objects.filter(
        appeared_at__lte=local_time,
        disappeared_at__gte=local_time
    )
    add_pokemon(
        folium_map,
        pokemons_entity.lat,
        pokemons_entity.lon,
        image_url=request.build_absolute_uri(pokemons_entity.pokemon.image.url),
    )
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemons_on_page,
    })

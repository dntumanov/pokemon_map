import folium

from django.shortcuts import render, get_object_or_404

from pokemon_entities.models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/" \
                    "6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/" \
                    "width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    """Отображение покемона на карте"""
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    """Возвращает всех покемонов"""
    pokemons = Pokemon.objects.all()
    pokemons_enity = PokemonEntity.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_enity in pokemons_enity:
        image_path = request.build_absolute_uri(
            pokemon_enity.pokemon.get_image_absolute_url)
        add_pokemon(
            folium_map, pokemon_enity.lat,
            pokemon_enity.lon,
            image_path)

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons,
    })


def show_pokemon(request, pokemon_id):
    """Возвращает подробную информацию об одном покемоне"""
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    pokemon_enity = get_object_or_404(PokemonEntity, pokemon__id=pokemon_id)

    pokemon_view_on_page = {
        'pokemon_id': pokemon.id,
        'img_url': pokemon.image.url,
        'title_ru': pokemon.title_ru,
        'description': pokemon.description,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
    }
    image_path = request.build_absolute_uri(
        pokemon_enity.pokemon.get_image_absolute_url)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    add_pokemon(
        folium_map, pokemon_enity.lat,
        pokemon_enity.lon,
        image_path)

    if pokemon.previous_evolution:
        pokemon_view_on_page['previous_evolution'] = {
            'pokemon_id': pokemon.previous_evolution.id,
            'img_url': pokemon.previous_evolution.image.url,
            'title_ru': pokemon.previous_evolution.title_ru
        }

    if pokemon.next_evolution.all():
        pokemon = pokemon.next_evolution.all().first()
        pokemon_view_on_page['next_evolution'] = {
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url,
            'title_ru': pokemon.title_ru
        }

    return render(
        request, "pokemon.html",
        context={
            'map': folium_map._repr_html_(),
            'pokemon': pokemon_view_on_page})

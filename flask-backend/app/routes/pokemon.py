from flask import Blueprint, render_template, redirect
from ..models.db import db, Pokemon, Item


pokemon_router = Blueprint("pokemon", __name__, url_prefix= "/pokemon")


@pokemon_router.route("/")
def index():

    all_pokemon = Pokemon.query.all()
    all_pokemon_dict = {}
    for pokemon in all_pokemon:
        print(pokemon.to_dict())
        all_pokemon_dict[pokemon.id]=pokemon.to_dict()
    print(all_pokemon_dict)
    return all_pokemon_dict

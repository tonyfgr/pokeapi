#!/usr/bin/env python

import requests
import sys

def extract_pokemon_names(lmt=8):
    url = "https://pokeapi.co/api/v2/pokemon?limit={}".format(lmt)
    r = requests.get(url)
    pokemons = []
    if r.status_code == 200:
        data = r.json()
        for pokemon in data['results']:
            pokemons.append({
                "name": pokemon['name'],
                "url": pokemon['url']
            })
    return pokemons

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\nUsage:\n\t{} <limit>\n".format(sys.argv[0]))
        sys.exit(1)
    limit = int(sys.argv[-1])
    for pokemon in extract_pokemon_names(limit):
        print("[{}]({})".format(pokemon["name"], pokemon["url"]))

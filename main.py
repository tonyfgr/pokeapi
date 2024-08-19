#!/usr/bin/env python

from flask import Flask, jsonify
from linkextractor import extract_pokemon_names

app = Flask(__name__)

@app.route("/")
def index():
    return "Usage: http://<hostname>[:<prt>]/api/<id>"

@app.route("/api/<int:id>")
def api(id):
    pokemons = extract_pokemon_names(50)
    if 0 <= id < len(pokemons):
        return jsonify(pokemons[id])
    else:
        return jsonify({"error": "Pokemon not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0")

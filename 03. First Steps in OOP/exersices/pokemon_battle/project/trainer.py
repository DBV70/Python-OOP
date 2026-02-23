from .pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons: list[Pokemon] = []

    def add_pokemon(self, pokemon : Pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        pkm_to_release = next((p for p in self.pokemons if p.name == pokemon_name), None)
        if pkm_to_release:
            self.pokemons.remove(pkm_to_release)
            return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        for pkm in self.pokemons:
            result.append(f"- {pkm.pokemon_details()}")
        return '\n'.join(result)

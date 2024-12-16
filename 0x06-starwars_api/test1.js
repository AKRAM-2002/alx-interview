#!/usr/bin/node
const request = require('request');

// Base URL for PokeAPI
const BASE_URL = 'https://pokeapi.co/api/v2';

class PokemonAPI {
  // Get basic Pokemon information
  static getPokemon (nameOrId) {
    return new Promise((resolve, reject) => {
      request(`${BASE_URL}/pokemon/${nameOrId.toLowerCase()}`, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }

        if (response.statusCode !== 200) {
          reject(`Error: Status Code ${response.statusCode}`);
          return;
        }

        resolve(JSON.parse(body));
      });
    });
  }

  // Get Pokemon abilities
  static getPokemonAbilities (nameOrId) {
    return new Promise((resolve, reject) => {
      this.getPokemon(nameOrId)
        .then(pokemon => {
          const abilities = pokemon.abilities.map(item => ({
            name: item.ability.name,
            is_hidden: item.is_hidden
          }));
          resolve(abilities);
        })
        .catch(reject);
    });
  }

  // Get Pokemon types
  static getPokemonTypes (nameOrId) {
    return new Promise((resolve, reject) => {
      this.getPokemon(nameOrId)
        .then(pokemon => {
          const types = pokemon.types.map(item => item.type.name);
          resolve(types);
        })
        .catch(reject);
    });
  }

  // Get Pokemon stats
  static getPokemonStats (nameOrId) {
    return new Promise((resolve, reject) => {
      this.getPokemon(nameOrId)
        .then(pokemon => {
          const stats = pokemon.stats.reduce((acc, stat) => {
            acc[stat.stat.name] = stat.base_stat;
            return acc;
          }, {});
          resolve(stats);
        })
        .catch(reject);
    });
  }

  // Get Pokemon moves
  static getPokemonMoves (nameOrId) {
    return new Promise((resolve, reject) => {
      this.getPokemon(nameOrId)
        .then(pokemon => {
          const moves = pokemon.moves.map(item => item.move.name);
          resolve(moves);
        })
        .catch(reject);
    });
  }

  // Get multiple Pokemon
  static getMultiplePokemon (limit = 10, offset = 0) {
    return new Promise((resolve, reject) => {
      request(
                `${BASE_URL}/pokemon?limit=${limit}&offset=${offset}`,
                (error, response, body) => {
                  if (error) {
                    reject(error);
                    return;
                  }

                  if (response.statusCode !== 200) {
                    reject(`Error: Status Code ${response.statusCode}`);
                    return;
                  }

                  resolve(JSON.parse(body));
                }
      );
    });
  }

  // Search Pokemon by type
  static getPokemonByType (type) {
    return new Promise((resolve, reject) => {
      request(`${BASE_URL}/type/${type}`, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }

        if (response.statusCode !== 200) {
          reject(`Error: Status Code ${response.statusCode}`);
          return;
        }

        const data = JSON.parse(body);
        const pokemon = data.pokemon.map(item => item.pokemon.name);
        resolve(pokemon);
      });
    });
  }
}

// Example usage
async function runExamples () {
  try {
    // 1. Get basic information about a Pokemon
    console.log('\n1. Getting basic info for Pikachu:');
    const pikachuInfo = await PokemonAPI.getPokemon('pikachu');
    console.log({
      name: pikachuInfo.name,
      id: pikachuInfo.id,
      height: pikachuInfo.height,
      weight: pikachuInfo.weight
    });

    // 2. Get Pokemon abilities
    console.log('\n2. Getting Pikachu abilities:');
    const abilities = await PokemonAPI.getPokemonAbilities('pikachu');
    console.log(abilities);

    // 3. Get Pokemon types
    console.log('\n3. Getting Charizard types:');
    const types = await PokemonAPI.getPokemonTypes('charizard');
    console.log(types);

    // 4. Get Pokemon stats
    console.log('\n4. Getting Mewtwo stats:');
    const stats = await PokemonAPI.getPokemonStats('mewtwo');
    console.log(stats);

    // 5. Get first 5 Pokemon moves
    console.log('\n5. Getting first 5 Dragonite moves:');
    const moves = await PokemonAPI.getPokemonMoves('dragonite');
    console.log(moves.slice(0, 5));

    // 6. Get list of Pokemon (pagination)
    console.log('\n6. Getting first 5 Pokemon from the list:');
    const pokemonList = await PokemonAPI.getMultiplePokemon(5, 0);
    console.log(pokemonList.results);

    // 7. Get all electric type Pokemon
    console.log('\n7. Getting first 5 electric type Pokemon:');
    const electricPokemon = await PokemonAPI.getPokemonByType('electric');
    console.log(electricPokemon.slice(0, 5));
  } catch (error) {
    console.error('Error:', error);
  }
}

// Run the examples
runExamples();

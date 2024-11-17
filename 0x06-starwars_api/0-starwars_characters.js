#!/usr/bin/node
const request = require('request');

const movie_id = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api';

function getCharacter(url) {
    return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
            if (error) {
                reject(error);
                return;
            }
            resolve(JSON.parse(body));
        });
    });
}

request(`${baseUrl}/films/${movie_id}`, async (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        return;
    }

    const film = JSON.parse(body);
    const characters = film.characters;

    // Process characters in sequence to maintain order
    for (const url of characters) {
        try {
            const character = await getCharacter(url);
            console.log(character.name);
        } catch (error) {
            console.error('Error fetching character:', error);
        }
    }
});
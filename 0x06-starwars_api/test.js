#!/usr/bin/node
const request = require('request');

const movie_id = process.argv[2];

// Test with a public API
request(`https://swapi-api.alx-tools.com/api/films/${movie_id}`, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const data= JSON.parse(body);
  const characters = data.characters.map(url => 
        request(`${url}`, (error, response, body) => {
            if (error) {
                console.error('Error:', error);
                return;
            }
            const data = JSON.parse(body);
            console.log(data.name);
        })
    );
});

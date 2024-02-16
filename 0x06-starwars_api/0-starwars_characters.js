#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');

const id = process.argv[2]
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const characters = (id) => {

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    const movieData = JSON.parse(body);

    for (const characterLink of movieData.characters) {
      request(characterLink, (err, res, charBody) => {
        if (err) {
          console.error('Error:', err);
            return;
        }

        const characterData = JSON.parse(charBody);
          console.log(characterData.name);
       });
     }
  });
};

characters(id);

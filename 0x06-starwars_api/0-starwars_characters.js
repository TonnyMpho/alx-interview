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

    try {
      const movieData = JSON.parse(body);

      if (!movieData.characters || movieData.characters.length === 0) {
        console.log('No characters found for this movie.');
        return;
      }

      for (const characterLink of movieData.characters) {
        request(characterLink, (err, res, charBody) => {
          if (err) {
            console.error('Error:', err);
            return;
          }

          try {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          } catch (charParseError) {
            console.error('Error parsing character data:', charParseError);
          }
        });
      }
    } catch (parseError) {
      console.error('Error parsing movie data:', parseError);
    }
  });
};

characters(id);

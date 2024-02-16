#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');

const id = process.argv[2]
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status Code ${response.statusCode}`);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  if (!characters || characters.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  console.log(`Characters in ${filmData.title}:`);

  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error(`Error: Status Code ${charResponse.statusCode}`);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});

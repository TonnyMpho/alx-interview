#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');

const id = process.argv[2]
const url = `https://swapi-api.alx-tools.com/api/films/${id}`

const characters = (id) => {

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    const data = JSON.parse(body);
    const charactersLinks = data.characters;
    for (const link of charactersLinks) {
      request(link, (err, res, body) => {
        if (err) {
          console.error('Error:', err);
          return;
        }
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    }
  });
};
characters(id);

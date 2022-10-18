#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request.get(`https://swapi-api.hbtn.io/api/films/${id}`, (err, _, body) => {
  if (err) return;
  const filmsDetails = JSON.parse(body);
  filmsDetails.characters.forEach(c => {
    request.get(c, (err, _, body) => {
      if (err) return;
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});

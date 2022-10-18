#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

const getCharacterDetail = (c) => {
  const id = parseInt(c.match(/\d+/)[0]);
  return new Promise(resolve => {
    request.get(c, (err, _, body) => {
      if (err) return;
      const character = JSON.parse(body);
      resolve({ ...character, id: id });
    });
  });
};

const sortedNames = (id) => {
  request.get(`https://swapi-api.hbtn.io/api/films/${id}`, async (err, _, body) => {
    if (err) return;
    const filmsCharacters = JSON.parse(body).characters;
    for (let i = 0; i < filmsCharacters.length; i++) {
      const character = await getCharacterDetail(filmsCharacters[i]);
      console.log(character.name);
    }
  });
};

sortedNames(id);

#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
request.get(`https://swapi-api.hbtn.io/api/films/${id}`, (err, _, body) => {
  body = body ? JSON.parse(body) : null;
  console.log(body.title || err);
});

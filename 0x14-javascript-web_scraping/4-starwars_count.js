#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    const films = body ? JSON.parse(body) : null;
    const isHere = films.results.filter(f => f.characters.filter(c => c.includes('/18/')).length);
    console.log(isHere.length);
  }
});

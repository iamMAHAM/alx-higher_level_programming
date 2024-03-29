#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, _, body) => {
  if (err) return;
  fs.writeFile(filePath, body, (err) => err ? console.log(err) : '');
});

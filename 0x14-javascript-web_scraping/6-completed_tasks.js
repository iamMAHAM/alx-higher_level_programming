#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, _, body) => {
  const obj = {};
  if (err) return;
  const todos = JSON.parse(body);
  const userCompletedList = todos.filter(u => u.completed);
  const filtered = userCompletedList.map(u => {
    return u.id;
  });
  for (let i = 0; i < filtered.length; i++) {
    obj[i + 1] = filtered[i];
  }
  console.log(obj);
});

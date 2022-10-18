#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, _, body) => {
  if (err) return;
  const todos = JSON.parse(body);
  const userCompletedList = todos.filter(u => u.completed);
  const filtered = userCompletedList.map(u => {
    return u.id;
  });
  console.log(Object.assign({}, filtered));
});

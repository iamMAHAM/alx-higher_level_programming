#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

const userList = {};

request(url, (err, _, body) => {
  const list = JSON.parse(body);
  if (err) {
    console.log(err);
  } else {
    for (let i = 0; i < list.length; i++) {
      const key = list[i].userId;
      if (list[i].completed) {
        if (!userList[key]) {
          userList[key] = 1;
        } else {
          userList[key] += 1;
        }
      }
    }
    console.log(userList);
  }
});

#!/usr/bin/node


const request = require('request');
let id = process.argv[2];
let url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body.title);
  } else {
    console.log('Error code:' + res.statusCode);
  }
});

#!/usr/bin/node

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/$id';

const request = require('request');
request(url, function (_err, _res, body) {
  body = JSON.parse(body);
  console.log(body.tittle);
});

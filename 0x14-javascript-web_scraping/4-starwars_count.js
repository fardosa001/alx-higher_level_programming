#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let num = 0;
    for (const i in films) {
      const chars = films[i].characters;
      for (const j in chars) {
        if (chars[j].includes('18')) {
          num += 1;
        }
      }
    }
    console.log(num);
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});

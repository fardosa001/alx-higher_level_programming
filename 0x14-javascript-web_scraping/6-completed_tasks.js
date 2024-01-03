#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const completedTasks = {};
    const tasks = JSON.parse(body);

    for (const i in tasks) {
      if (tasks[i].completed) {
        if (completedTasks[tasks[i].userId] === undefined) {
          completedTasks[tasks[i].userId] = 1;
        } else {
          completedTasks[tasks[i].userId]++;
        }
      }
    }

    console.log(completedTasks);
  }
});

#!/usr/bin/node
// Script to computes the number of tasks completed by user id.
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const userTasksCompleted = {};
    todos.forEach((task) => {
      if (task.completed) {
        if (!userTasksCompleted[task.userId]) {
          userTasksCompleted[task.userId] = 1;
        } else {
          userTasksCompleted[task.userId]++;
        }
      }
    });
    console.log(userTasksCompleted);
  }
});

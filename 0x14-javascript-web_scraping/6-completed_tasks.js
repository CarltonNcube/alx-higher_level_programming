#!/usr/bin/node
// Computes the number of tasks completed by user id

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    
    // Create an object to store the count of completed tasks for each user
    const completedTasksByUser = {};

    // Count the completed tasks for each user
    tasks.forEach((task) => {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });

    console.log(completedTasksByUser);
  }
});
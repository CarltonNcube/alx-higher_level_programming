#!/usr/bin/node
// Counts the number of completed tasks per user ID from

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const tasks = safeJsonParse(body);

  if (tasks === null) {
    console.error('Error parsing API response');
    return;
  }

  const completedTasksByUser = {};

  tasks.forEach((task) => {
    if (task.completed) {
      completedTasksByUser[task.userId] = (completedTasksByUser
	      [task.userId] || 0) + 1;
    }
  });

  console.log(completedTasksByUser);
});

function safeJsonParse(jsonString) {
  return JSON.parse(jsonString) || null;
}


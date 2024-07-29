#!/usr/bin/node
const { createClient, print } = require('redis');
const promisify = require('util').promisify;

const client = createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const setNewSchool = async (schoolName, value) => {
    await client.SET(schoolName, value, print);
}

const displaySchoolValue = async (schoolName) => {
    await client.GET(schoolName, (err, reply) => {
        if (err) {
            console.log(`Error retrieving value for ${schoolName}: ${err}`);
        } else {
            console.log(reply);
        }
    });
}

const setNewSchoolPromise = promisify(setNewSchool);
const displaySchoolValuePromise = promisify(displaySchoolValue);

const main = async () => {
  displaySchoolValuePromise('Holberton');
  setNewSchoolPromise('HolbertonSanFrancisco', '100');
  displaySchoolValuePromise('HolbertonSanFrancisco');
}

main(); 

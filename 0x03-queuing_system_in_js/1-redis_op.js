#!/usr/bin/node
const { createClient, print } = require('redis');

const client = createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
    client.SET(schoolName, value, print);
}

const displaySchoolValue = (schoolName) => {
    client.GET(schoolName, (err, reply) => {
        if (err) {
            console.log(`Error retrieving value for ${schoolName}: ${err}`);
        } else {
            console.log(reply);
        }
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

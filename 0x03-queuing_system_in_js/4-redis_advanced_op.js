#!/usr/bin/node
const { createClient, print } = require('redis');

const client = createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});
client.on('connect', () => {
    console.log('Redis client connected to the server');
});


const hash_key = 'HolbertonSchools'
const hashFields = {
    'Portaland': 50,
    'Seattle': 80,
    'New York':20, 
    'Bogota':20,
    'Cali': 40,
    'Paris': 2
}
const hashFieldsArray = Object.entries(hashFields).flat();

try {
    client.HSET(hash_key, ...hashFieldsArray, print)
} catch (err) {
    console.log(`something went wrong ${err}`);
}

client.HGETALL(hash_key, (err, reply) => {
    if (err) {
        console.log(`Error retrieving value for ${hash_key}: ${err}`);
    } else {
        console.log(reply);
    }
});

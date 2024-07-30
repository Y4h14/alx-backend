#!/usr/bin/node
const { createClient, print } = require('redis');

const client = createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const channel = 'holberton school channel';

client.subscribe(channel);


client.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        client.unsubscribe(channel, (err) => {
            if (err) {
                console.log(err);
            } else {
                client.quit;
            }
        });
    }
});

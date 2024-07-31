#!/usr/bin/node
const { createClient } = require('redis');
const {promisify} = require('util');
const kue = require('kue');
const express = require('express');

const queue = kue.createQueue();
const client = createClient();
const app = express();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});
client.on('connect', () => {
    console.log('Redis client connected to the server');
});


//promisify Redis fucntions
const asyncGET = promisify(client.get).bind(client);
const asyncSET = promisify(client.set).bind(client);


const reserveSeat = async (number) => {
    await asyncSET('available_seats', number)
}

const getCurrentAvailableSeats = async () => {
    const seats =  await asyncGET('available_seats');
    return Number.parseInt(seats, 10);
}

reserveSeat(50);
let reservationEnabled = true;

app.get('/available_seats', (_, res)=>{
    getCurrentAvailableSeats()
    .then((seats) => {
        res.send({'numberOfAvailabeSeats': seats})
    });
});

app.get('/reserve_seat', (_, res) => {
    if (!reservationEnabled) {
        res.send({ 'status': 'Reservation are blocked' });
    }
    const job = queue.create('reserve_seat')
    .on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
    })
    .on('failure', (err) => {
        console.log(`Seat reservation job ${job.id} failed: ${err}`);
    })
    .save((err) => {
        if (err) {
            res.send({'status': 'reservation failed' })
        } else {
            res.send({'status':'Reservation in process'})
        }
    });
});

app.get('/process', (_,res) => {
    res.send({'status': 'Queue processing'});
    queue.process('reserve_seat', (job, done) => {
      getCurrentAvailableSeats()
      .then((result) => Number.parseInt(result || 0))
      .then((availableSeats) => {
        if (availableSeats >= 1) {
            reserveSeat(availableSeats - 1)
            .then(() => done());
        } else {
            reservationEnabled = false;
            done(new Error('Not enough seats available'));
        }
      });
    });
});

app.listen(1245, () => {
    console.log('Server listening on port 1245');
});

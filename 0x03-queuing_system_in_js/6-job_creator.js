#!/usr/bin/node
const kue =require('kue');

const queue = kue.createQueue();

const jobData = {
    'phoneNumber': 123456789,
    'message': 'some message'
}

const job = queue.create('push_notification_code', jobData)
    .on ('enqueue', ()=> {
        console.log('Notification job created', job.id);
    })
    .on('complete', () => {
        console.log('Notification job completed');
    })
    .on('failed attempt', ()=> {
        console.log('Notification job failed');
    })
    .save((err) => {
        if (err) {
            console.log(`Error creating job ${err}`);
        }
    });

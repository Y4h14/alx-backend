#!/usr/bin/node
const kue = require('kue');

const queue = kue.createQueue();


const createPushNotificationJobs = (jobs, queue) => {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
        } else {
            for (const jobObj of jobs) {
                const job = queue.create('push_notification_code_3', jobObj)
                .on ('complete', () => {
                    console.log(`Notification job created: ${job.id}`);
                })
                .on ('failed', (err) => {
                    console.log(`Notification job ${job.id} failed: ${err}`);
                })
                .on ('progress', (progress, data) => {
                    console.log(`Notification job ${job.id} ${progress}% complete`);
                })
                .save((err) => {
                    if (err) {
                        console.log(err);
                    } else {
                        console.log(`Notification job created: ${job.id}`);
                    }
                });
        }
    }
}

module.exports = createPushNotificationJobs;

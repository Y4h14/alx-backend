#!/usr/bin/node
import createPushNotificationJobs from './8-job';
const expect = require('chai').expect;
const kue = require('kue');

const queue = kue.createQueue();
const testQueue = queue.testMode;

describe('createPushNotificationJobs', () => {
    before(() => {
        testQueue.enter();
    });

    afterEach(() => {
        testQueue.clear();
    });

    after(() => {
        testQueue.exit()
    });

    it('create jobs for items in jobs array', () => {
        const jobs = [
            {phoneNumber: '123456', message: 'notification message1'},
            {phoneNumber: '654321', message: 'notification message2'}
        ];
        createPushNotificationJobs(jobs, queue);

        setTimeout(() => {
            expect(testQueue.jobs.length).to.equal(2);
            expect(testQueue.jobs[0].data).to.deep.equal(jobs[0]);
            expect(testQueue.jobs[1].data).to.deep.equal(jobs[1]);

            done(); // Notify Mocha that the test is complete
        }, 100);

   
    });
});

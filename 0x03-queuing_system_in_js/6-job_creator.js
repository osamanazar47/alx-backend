const kue = require('kue');
const redis = require('redis');

const job_data = {
  phoneNumber: '012345678',
  message: 'Hello from Kue',
};
const push_notification_code = kue.createQueue()

const job = push_notification_code.create('data', job_data).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
	job.on('complete', () => {
      console.log('Notification job completed');
    });

	job.on('failed', () => {
      console.log('Notification job failed');
	});
  }
});

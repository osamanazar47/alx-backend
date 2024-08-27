import redis from 'redis';

const client = redis.createClient()

client
  .on('connect', () => {
    console.log('Redis client connected to the server');
	client.subscribe('holberton school channel');
  })
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  })
  .on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
      client.unsubscribe('holberton school channel');
	  client.quit();
    }
  });

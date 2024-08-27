import redis from 'redis';

const client = redis.createClient();

client
  .on('ready', () => {
    console.log('Redis client connected to the server')
  })
  .on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`)
  })

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, value) => {
    if (err) {
      console.log(err);
	} else {
      console.log(value);
	}
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

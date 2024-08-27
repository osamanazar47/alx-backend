import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client
  .on('ready', async () => {
    console.log('Redis client connected to the server')
    await main();
  })
  .on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`)
  })

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  console.log(await promisify(client.GET).bind(client)(schoolName));
};

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}
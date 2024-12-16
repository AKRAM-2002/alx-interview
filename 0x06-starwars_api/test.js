const axios = require('axios').default;

const data = {
  "name": "victor",
  "job": "writer"
}

async function addUser(data) {
  try {
    const response = await axios.post(`https://reqres.in/api/users`, data);
    console.log(response);
  } catch (error) {
    console.error(error);
  }
}

addUser()
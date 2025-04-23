const knex = require('knex');

const db = knex({
  client:'pg',
  connection:{
    host: 'localhost',
    port: '5432',
    user: 'postgres',
    password: '1234',
    database: 'users'
  }
})

function createUser({user}){
  return db('users').insert(
    {
      username:user
    }
  )
  .returning('*')
}

module.exports = {
  createUser
}
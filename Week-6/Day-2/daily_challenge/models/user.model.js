const db = require('../config/db');

module.exports = {
  async createUser(user, hashedPassword) {
    return db.transaction(async trx => {
      await trx('users').insert(user);
      await trx('hashpwd').insert({ username: user.username, password: hashedPassword });
    });
  },

  getAllUsers() {
    return db('users');
  },

  getUserById(id) {
    return db('users').where({ id }).first();
  },

  updateUser(id, updates) {
    return db('users').where({ id }).update(updates);
  },

  getHashedPassword(username) {
    return db('hashpwd').where({ username }).first();
  }
};

const knex = require('knex')(require('../config/knexfile').development);

const getAll = () => knex('tasks');
const getById = (id) => knex('tasks').where({ id }).first();
const create = (data) => knex('tasks').insert(data).returning('*');
const update = (id, data) => knex('tasks').where({ id }).update(data).returning('*');
const remove = (id) => knex('tasks').where({ id }).del();

module.exports = { getAll, getById, create, update, remove };

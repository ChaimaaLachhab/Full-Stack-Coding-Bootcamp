const knex = require('knex')(require('../knexfile').development);

exports.getAllPosts = async (req, res) => {
  const posts = await knex('posts').select('*');
  console.log("All posts fetched successfully");
  console.log(posts);
  posts ? res.json(posts) : res.status(404).json({ error: 'Not found' });
};

exports.getPostById = async (req, res) => {
  const post = await knex('posts').where('id', req.params.id).first();
  post ? res.json(post) : res.status(404).json({ error: 'Not found' });
};

exports.createPost = async (req, res) => {
  const [id] = await knex('posts').insert(req.body).returning('id');
  res.status(201).json({ id });
};

exports.updatePost = async (req, res) => {
  const updated = await knex('posts').where('id', req.params.id).update(req.body);
  updated ? res.json({ message: 'Updated' }) : res.status(404).json({ error: 'Not found' });
};

exports.deletePost = async (req, res) => {
  const deleted = await knex('posts').where('id', req.params.id).del();
  deleted ? res.json({ message: 'Deleted' }) : res.status(404).json({ error: 'Not found' });
};

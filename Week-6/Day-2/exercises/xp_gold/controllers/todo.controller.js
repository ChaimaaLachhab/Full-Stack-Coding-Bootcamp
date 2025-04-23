const Todo = require('../models/todoModel');

exports.getAllTodos = async (req, res) => {
  const todos = await Todo.getAll();
  res.json(todos);
};

exports.getTodoById = async (req, res) => {
  const todo = await Todo.getById(req.params.id);
  if (!todo) return res.status(404).json({ message: 'Todo not found' });
  res.json(todo);
};

exports.createTodo = async (req, res) => {
  const { title } = req.body;
  if (!title) return res.status(400).json({ message: 'Title is required' });

  const [newTodo] = await Todo.create({ title });
  res.status(201).json(newTodo);
};

exports.updateTodo = async (req, res) => {
  const { title, completed } = req.body;
  const [updatedTodo] = await Todo.update(req.params.id, { title, completed });
  if (!updatedTodo) return res.status(404).json({ message: 'Todo not found' });
  res.json(updatedTodo);
};

exports.deleteTodo = async (req, res) => {
  const deleted = await Todo.remove(req.params.id);
  if (!deleted) return res.status(404).json({ message: 'Todo not found' });
  res.status(204).send();
};

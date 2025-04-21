const express = require('express');
const router = express.Router();
let todos = [];
let nextId = 1;

// Get
router.get('/', (req, res) => res.json(todos));

// Create
router.post('/', (req, res) => {
  const todo = { id: nextId++, ...req.body };
  todos.push(todo);
  res.status(201).json(todo);
});

// Update
router.put('/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = todos.findIndex(todo => todo.id === id);
  if (index !== -1) {
    todos[index] = { id, ...req.body };
    res.json(todos[index]);
  } else {
    res.status(404).send('Todo not found');
  }
});

// Delete
router.delete('/:id', (req, res) => {
  const id = parseInt(req.params.id);
  todos = todos.filter(todo => todo.id !== id);
  res.status(204).send();
});

module.exports = router;

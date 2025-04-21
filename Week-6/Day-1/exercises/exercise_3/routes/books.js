const express = require('express');
const router = express.Router();
let books = [];
let nextId = 1;

// Get
router.get('/', (req, res) => res.json(books));

// Add
router.post('/', (req, res) => {
  const book = { id: nextId++, ...req.body };
  books.push(book);
  res.status(201).json(book);
});

// Update
router.put('/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = books.findIndex(book => book.id === id);
  if (index !== -1) {
    books[index] = { id, ...req.body };
    res.json(books[index]);
  } else {
    res.status(404).send('Book not found');
  }
});

// Delete
router.delete('/:id', (req, res) => {
  const id = parseInt(req.params.id);
  books = books.filter(book => book.id !== id);
  res.status(204).send();
});

module.exports = router;

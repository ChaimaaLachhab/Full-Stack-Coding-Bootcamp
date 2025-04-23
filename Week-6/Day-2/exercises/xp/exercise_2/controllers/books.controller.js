let books = require('../models/bookModel');
  
  exports.getAllBooks = (req, res) => {
    res.json(books);
  };
  
  exports.getBookById = (req, res) => {
    const book = books.find(b => b.id == req.params.bookId);
    book ? res.json(book) : res.status(404).json({ message: 'Book not found' });
  };
  
  exports.createBook = (req, res) => {
    const newBook = { id: books.length + 1, ...req.body };
    books.push(newBook);
    res.status(201).json(newBook);
  };
  
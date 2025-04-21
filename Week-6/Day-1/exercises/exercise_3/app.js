const express = require('express');
const app = express();
const bookRoutes = require('./routes/books');

app.use(express.json());
app.use('/books', bookRoutes);

app.listen(3000, () => console.log('Server running on http://localhost:3000'));

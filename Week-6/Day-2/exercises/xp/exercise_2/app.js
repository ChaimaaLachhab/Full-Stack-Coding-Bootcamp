const express = require('express');
const app = express();

const bookRoutes = require('./server/routes/books.routes');
app.use(express.json());

app.use('/api/books', bookRoutes);

const PORT = 5000;
app.listen(PORT, () => console.log(`Book API running on port ${PORT}`));

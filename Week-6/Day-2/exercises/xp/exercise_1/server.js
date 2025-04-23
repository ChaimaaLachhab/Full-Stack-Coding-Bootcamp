const express = require('express');
const app = express();
require('dotenv').config();

const postRoutes = require('./routes/posts.routes');
app.use(express.json());

app.use('/posts', postRoutes);

// 404 handler
app.use((req, res) => {
  res.status(404).json({ error: 'Route not found' });
});

const PORT = 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));


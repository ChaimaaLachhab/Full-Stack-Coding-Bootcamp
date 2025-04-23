const express = require('express');
const app = express();
const todoRoutes = require('./server/routes/todoRoutes');

app.use(express.json());
app.use('/api/todos', todoRoutes);

app.use((req, res) => {
  res.status(404).json({ message: 'Route not found' });
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});

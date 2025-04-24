// app.js
const express = require('express');
const taskRoutes = require('./routes/tasks');

const app = express();
const port = 3000;

app.use(express.json());
app.use('/tasks', taskRoutes);

app.listen(port, () => {
  console.log(`Task Management API running at http://localhost:${port}`);
});

const express = require('express');
const app = express();
const userRoutes = require('./routes/user.routes');

app.use(express.json());
app.use('/api', userRoutes);

app.listen(5000, () => {
  console.log('Server running on http://localhost:5000');
});

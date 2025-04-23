const express = require('express');
const app = express();
const questionRoutes = require('./server/routes/question.routes');
const cors = require('cors');
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

app.use('/api/questions', questionRoutes);

app.listen(5000, () => {
  console.log('Quiz server running on http://localhost:5000');
});


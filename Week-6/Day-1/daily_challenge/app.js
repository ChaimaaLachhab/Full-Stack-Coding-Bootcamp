// app.js
const express = require('express');
const quizRouter = require('./routes/quiz');

const app = express();
const port = 3000;

app.use(express.json());
app.use('/quiz', quizRouter);

app.listen(port, () => {
  console.log(`Trivia Quiz Game running at http://localhost:${port}`);
});

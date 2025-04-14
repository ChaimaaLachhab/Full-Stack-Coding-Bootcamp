const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const emojis = require('./emojis');

const app = express();
const PORT = 3000;

app.use(express.static('public'));
app.use(bodyParser.json());

let leaderboard = [];
let currentQuestion = {};

function generateQuestion() {
  const correct = emojis[Math.floor(Math.random() * emojis.length)];
  const options = [correct.name];

  while (options.length < 4) {
    const random = emojis[Math.floor(Math.random() * emojis.length)];
    if (!options.includes(random.name)) {
      options.push(random.name);
    }
  }

  options.sort(() => Math.random() - 0.5);

  currentQuestion = {
    emoji: correct.emoji,
    correct: correct.name,
    options
  };
  return currentQuestion;
}

app.get('/api/question', (req, res) => {
  const question = generateQuestion();
  res.json({
    emoji: question.emoji,
    options: question.options
  });
});

app.post('/api/guess', (req, res) => {
  const { guess, player } = req.body;
  const correct = currentQuestion.correct;
  const result = guess === correct;

  let playerScore = leaderboard.find(p => p.name === player);
  if (!playerScore) {
    leaderboard.push({ name: player, score: 0 });
    playerScore = leaderboard.find(p => p.name === player);
  }

  if (result) playerScore.score++;

  res.json({ correct, score: playerScore.score });
});

app.get('/api/leaderboard', (req, res) => {
  const sorted = leaderboard.sort((a, b) => b.score - a.score).slice(0, 5);
  res.json(sorted);
});

app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));

const express = require('express');
const router = express.Router();

const triviaQuestions = [
  { question: "What is the capital of France?", answer: "Paris" },
  { question: "Which planet is known as the Red Planet?", answer: "Mars" },
  { question: "What is the largest mammal in the world?", answer: "Blue whale" },
];

let currentQuestionIndex = 0;
let score = 0;

// GET
router.get('/', (req, res) => {
  if (currentQuestionIndex >= triviaQuestions.length) {
    return res.redirect('/quiz/score');
  }

  const currentQuestion = triviaQuestions[currentQuestionIndex].question;
  res.json({ question: currentQuestion });
});

// POST
router.post('/', (req, res) => {
  const userAnswer = req.body.answer;

  if (!userAnswer) {
    return res.status(400).json({ error: 'Answer is required.' });
  }

  const correctAnswer = triviaQuestions[currentQuestionIndex].answer;

  let isCorrect = false;
  if (userAnswer.trim().toLowerCase() === correctAnswer.toLowerCase()) {
    score++;
    isCorrect = true;
  }

  currentQuestionIndex++;

  if (currentQuestionIndex < triviaQuestions.length) {
    return res.json({
      correct: isCorrect,
      nextQuestion: triviaQuestions[currentQuestionIndex].question,
    });
  } else {
    return res.redirect('/quiz/score');
  }
});

// GET
router.get('/score', (req, res) => {
  const finalScore = score;
  
  currentQuestionIndex = 0;
  score = 0;

  res.json({ message: `Quiz Over! Your final score is ${finalScore}/${triviaQuestions.length}` });
});

module.exports = router;

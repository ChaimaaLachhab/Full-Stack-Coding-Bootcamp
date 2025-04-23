const express = require('express');
const router = express.Router();
const { getQuestionWithOptions, submitAnswer } = require('../controllers/question.controller');

router.get('/next/:index', getQuestionWithOptions);
router.post('/answer', submitAnswer);

module.exports = router;

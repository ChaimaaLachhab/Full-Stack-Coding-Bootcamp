const knex = require("knex")(require("../../knexfile").development);

exports.getQuestionWithOptions = async (req, res) => {
  const index = parseInt(req.params.index);
  const question = await knex("questions")
    .select()
    .limit(1)
    .offset(index)
    .first();
  if (!question) return res.status(404).json({ message: "No more questions." });

  const options = await knex("questions_options")
    .join("options", "questions_options.option_id", "options.id")
    .where("questions_options.question_id", question.id)
    .select("options.id", "options.option");

  res.json({ question, options });
};

exports.submitAnswer = async (req, res) => {
  const { questionId, selectedOption } = req.body;

  const question = await knex("questions").where({ id: questionId }).first();

  const correctOption = await knex("options")
    .where({ id: question.correct_answer })
    .first();

  const isCorrect = selectedOption === correctOption.option;

  res.json({ correct: isCorrect });
};

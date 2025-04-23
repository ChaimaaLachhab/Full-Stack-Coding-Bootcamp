/**
 * @param { import("knex").Knex } knex
 * @returns { Promise<void> }
 */
exports.seed = async function(knex) {
  // Supprimer les données dans l’ordre inverse des dépendances
  await knex('questions_options').del();
  await knex('questions').del();
  await knex('options').del();

  // Insérer les options
  const insertedOptions = await knex('options').insert([
    { option: 'Paris' },       // 1
    { option: 'London' },      // 2
    { option: 'Berlin' },      // 3
    { option: 'Mars' },        // 4
    { option: 'Jupiter' },     // 5
    { option: 'Saturn' },      // 6
    { option: 'Shakespeare' }, // 7
    { option: 'Dickens' },     // 8
    { option: 'Hemingway' }    // 9
  ]).returning(['id', 'option']);

  // Utilitaire pour retrouver l'id d'une option
  const getOptionId = (text) => insertedOptions.find(o => o.option === text).id;

  // Insérer les questions avec la bonne réponse
  await knex('questions').insert([
    { id: 1, question: 'What is the capital of France?', correct_answer: getOptionId('Paris') },
    { id: 2, question: 'Which planet is known as the Red Planet?', correct_answer: getOptionId('Mars') },
    { id: 3, question: 'Who wrote "To Be or Not To Be"?', correct_answer: getOptionId('Shakespeare') }
  ]);

  // Mapper les options aux questions (facultatif si tu utilises la table `questions_options`)
  await knex('questions_options').insert([
    { question_id: 1, option_id: getOptionId('Paris') },
    { question_id: 1, option_id: getOptionId('London') },
    { question_id: 1, option_id: getOptionId('Berlin') },

    { question_id: 2, option_id: getOptionId('Mars') },
    { question_id: 2, option_id: getOptionId('Jupiter') },
    { question_id: 2, option_id: getOptionId('Saturn') },

    { question_id: 3, option_id: getOptionId('Shakespeare') },
    { question_id: 3, option_id: getOptionId('Dickens') },
    { question_id: 3, option_id: getOptionId('Hemingway') }
  ]);
};
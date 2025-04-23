/**
 * @param { import("knex").Knex } knex
 * @returns { Promise<void> }
 */
exports.up = function(knex) {
    return knex.schema.createTable('questions_options', (table) => {
      table.integer('question_id').unsigned().references('id').inTable('questions').onDelete('CASCADE');
      table.integer('option_id').unsigned().references('id').inTable('options').onDelete('CASCADE');
      table.primary(['question_id', 'option_id']);
    });
  };
  
  /**
   * @param { import("knex").Knex } knex
   * @returns { Promise<void> }
   */
  exports.down = function(knex) {
    return knex.schema.dropTable('questions_options');
  };
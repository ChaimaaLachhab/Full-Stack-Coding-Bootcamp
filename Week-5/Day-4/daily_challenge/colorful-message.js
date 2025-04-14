const chalk = require('chalk');

function displayColorfulMessage() {
  console.log(chalk.blue.bgYellow.bold('🚀 Welcome to your colorful Node.js challenge!'));
}

module.exports = displayColorfulMessage;

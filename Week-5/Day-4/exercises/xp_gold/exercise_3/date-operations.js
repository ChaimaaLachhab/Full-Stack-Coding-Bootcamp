const { addDays, format } = require('date-fns');

function showDate() {
  const now = new Date();
  const newDate = addDays(now, 5);
  const formatted = format(newDate, 'yyyy-MM-dd');
  console.log('Date +5 days:', formatted);
}

module.exports = showDate;

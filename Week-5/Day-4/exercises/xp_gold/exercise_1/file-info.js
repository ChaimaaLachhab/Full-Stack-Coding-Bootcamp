const fs = require('fs');
const path = require('path');

function showFileInfo() {
  const filePath = path.join(__dirname, 'data', 'example.txt');

  if (fs.existsSync(filePath)) {
    const stats = fs.statSync(filePath);
    console.log('File exists:', true);
    console.log('Size:', stats.size, 'bytes');
    console.log('Created at:', stats.birthtime);
  } else {
    console.log('File does not exist.');
  }
}

module.exports = showFileInfo;

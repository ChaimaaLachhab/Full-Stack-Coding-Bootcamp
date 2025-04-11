import { readFile, writeFile } from './fileManager.js';

const content = readFile('./Hello World.txt');
writeFile('./Bye World.txt', 'kokokoko');

console.log('File written successfully!');

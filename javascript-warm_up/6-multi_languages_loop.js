#!/usr/bin/node
const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let output = '';

for (const language of languages) {
  output += `${language}\n`;
}

console.log(output.slice(0, -1));

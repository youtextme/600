#!/usr/bin/env node
/** Upgrade vocab to daily-usable words with kid-friendly example sentences */
const fs = require('fs');
const path = require('path');

const BANK = path.join(__dirname, 'essay-bank.json');
const bank = JSON.parse(fs.readFileSync(BANK, 'utf8'));

const DAILY_WORDS = {
  'essay-001': [
    { word: 'fascinating', definition: 'Extremely interesting — makes you want to learn more', exampleSentence: '"That is fascinating, Ms. Luz!" I told my teacher.' },
    { word: 'observe', definition: 'To watch carefully and notice details', exampleSentence: 'I observe how the fish glow when Dad turns off the lights.' },
    { word: 'remarkable', definition: 'Worthy of attention — surprisingly impressive', exampleSentence: 'Grandpa said fireflies are a remarkable invention of nature.' },
    { word: 'collaborate', definition: 'To work together toward the same goal', exampleSentence: 'The squid and bacteria collaborate to survive.' },
    { word: 'definitely', definition: 'Without any doubt — for sure', exampleSentence: 'I will definitely ask Dad about glowing ocean water.' },
  ],
};

bank.forEach(essay => {
  if (DAILY_WORDS[essay.id]) {
    essay.words = DAILY_WORDS[essay.id];
    return;
  }
  essay.words = (essay.words || []).map(w => ({
    ...w,
    exampleSentence: w.exampleSentence || `"That is truly ${w.word}," I said to my friend.`,
  }));
});

fs.writeFileSync(BANK, JSON.stringify(bank, null, 2));
console.log('Upgraded vocab examples for daily use.');

#!/usr/bin/env node
/**
 * Converts free-text questions to multiple-choice with reveal hints.
 * Run once after editing essay-bank.json
 */
const fs = require('fs');
const path = require('path');

const BANK = path.join(__dirname, 'essay-bank.json');

const DISTRACTOR_POOL = [
  'Electric light bulbs', 'Volcanic eruptions', 'Wind and storms',
  'Photosynthesis only', 'Random luck', 'Magnetic fields',
  'They never change', 'Only at night', 'Only on land',
  'To scare humans', 'For no reason', 'Pure decoration',
  'Solar panels', 'Burning wood', 'Echoes and sound',
  'Gravity alone', 'Empty space', 'Plastic pollution',
  'Ancient myths only', 'Computer code', 'Radio waves',
  'They compete only', 'They stay silent', 'They avoid water',
  'One year exactly', 'Never', 'Only in summer',
  'To look pretty', 'To make noise', 'To sleep better',
];

function capitalize(s) {
  if (!s) return s;
  return s.charAt(0).toUpperCase() + s.slice(1);
}

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function labelForAnswer(a) {
  const s = capitalize(String(a).trim());
  if (s.length > 60) return s.slice(0, 57) + '…';
  return s;
}

function pickDistractors(question, essayQuestions, correctLabel, n) {
  const used = new Set([correctLabel.toLowerCase()]);
  const fromOthers = essayQuestions
    .filter(q => q.id !== question.id)
    .flatMap(q => (q.answers || []).map(labelForAnswer))
    .filter(l => !used.has(l.toLowerCase()));

  const pool = [...fromOthers, ...DISTRACTOR_POOL.map(capitalize)];
  const out = [];
  for (const d of shuffle(pool)) {
    if (out.length >= n) break;
    if (!used.has(d.toLowerCase())) {
      used.add(d.toLowerCase());
      out.push(d);
    }
  }
  while (out.length < n) {
    out.push(`Option ${out.length + 1} (not in story)`);
  }
  return out.slice(0, n);
}

function buildRevealHint(q, correctLabel) {
  const hint = q.hint || 'Reread the passage carefully.';
  const storyBit = q.storyQuote || hint;
  return `The story said: "${storyBit}" — the answer is **${correctLabel}**.`;
}

function migrateQuestion(q, essayQuestions) {
  if (q.options && q.options.length >= 4 && typeof q.correctIndex === 'number') {
    if (!q.revealHint) {
      q.revealHint = buildRevealHint(q, q.options[q.correctIndex]);
    }
    return q;
  }

  const correctLabel = labelForAnswer((q.answers || ['Unknown'])[0]);
  const distractors = pickDistractors(q, essayQuestions, correctLabel, 3);
  const options = shuffle([correctLabel, ...distractors]);
  const correctIndex = options.findIndex(o => o === correctLabel);

  return {
    id: q.id,
    question: q.question,
    options,
    correctIndex,
    revealHint: buildRevealHint(q, correctLabel),
    explanation: q.explanation,
    hint: q.hint,
  };
}

function dailyWord(w) {
  if (w.exampleSentence) return w;
  const examples = {
    observe: 'I observed that the fish were glowing near the boat.',
    fascinating: 'That discovery is fascinating — tell me more!',
    appreciate: 'I appreciate how you explained that to me.',
    curious: 'I am curious about what lives in the deep ocean.',
    remarkable: 'It is remarkable how fireflies flash in patterns.',
    definitely: 'I definitely want to research that tonight.',
    apparently: 'Apparently, trees share food through underground networks.',
    elaborate: 'Can you elaborate on how that works?',
    precise: 'Scientists need precise measurements for experiments.',
    investigate: 'Let us investigate why the water glows.',
  };
  const key = w.word.toLowerCase();
  return {
    ...w,
    exampleSentence: examples[key] || `Try saying: "That is truly ${w.word}."`,
  };
}

const bank = JSON.parse(fs.readFileSync(BANK, 'utf8'));
bank.forEach(essay => {
  essay.words = (essay.words || []).map(dailyWord);
  essay.questions = (essay.questions || []).map(q => migrateQuestion(q, essay.questions));
});
fs.writeFileSync(BANK, JSON.stringify(bank, null, 2));
console.log(`Migrated ${bank.length} essays to MCQ format.`);

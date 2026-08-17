#!/usr/bin/env node
/**
 * generate-week.js
 * Picks 7 unused essays, assigns Sun–Sat dates, updates state.
 * Run every Sunday 8:00 AM KST via GitHub Actions.
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const DATA = path.join(ROOT, 'data');
const BANK_PATH = path.join(__dirname, 'essay-bank.json');

function getKSTDate(d = new Date()) {
  const utc = d.getTime() + d.getTimezoneOffset() * 60000;
  return new Date(utc + 9 * 60 * 60000);
}

function formatDate(d) {
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${y}-${m}-${day}`;
}

function getWeekStartSunday(d = getKSTDate()) {
  const copy = new Date(d);
  const day = copy.getDay(); // 0 = Sunday
  copy.setDate(copy.getDate() - day);
  copy.setHours(0, 0, 0, 0);
  return copy;
}

function getISOWeekId(d) {
  const date = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
  date.setUTCDate(date.getUTCDate() + 4 - (date.getUTCDay() || 7));
  const yearStart = new Date(Date.UTC(date.getUTCFullYear(), 0, 1));
  const weekNo = Math.ceil(((date - yearStart) / 86400000 + 1) / 7);
  return `${date.getUTCFullYear()}-W${String(weekNo).padStart(2, '0')}`;
}

function loadJSON(p, fallback) {
  try {
    return JSON.parse(fs.readFileSync(p, 'utf8'));
  } catch {
    return fallback;
  }
}

function main() {
  const bank = loadJSON(BANK_PATH, []);
  if (!bank.length) {
    console.error('essay-bank.json is empty');
    process.exit(1);
  }

  const statePath = path.join(DATA, 'state.json');
  const state = loadJSON(statePath, { usedWords: [], usedTopics: [], usedEssayIds: [], totalEssaysServed: 0 });

  // Pick 7 essays not yet used; reset pool if exhausted
  let available = bank.filter(e => !state.usedEssayIds.includes(e.id));
  if (available.length < 7) {
    console.log('Essay pool exhausted — resetting usedEssayIds (words/topics persist)');
    state.usedEssayIds = [];
    available = [...bank];
  }

  // Shuffle Fisher-Yates
  for (let i = available.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [available[i], available[j]] = [available[j], available[i]];
  }

  const selected = available.slice(0, 7);
  const weekStart = getWeekStartSunday();
  const weekId = getISOWeekId(weekStart);

  const days = selected.map((essay, i) => {
    const date = new Date(weekStart);
    date.setDate(date.getDate() + i);
    return {
      id: formatDate(date),
      date: formatDate(date),
      dayIndex: i,
      essayId: essay.id,
      title: essay.title,
      topic: essay.topic,
      words: essay.words,
      grammarRules: essay.grammarRules,
      passageHtml: essay.passageHtml,
      questions: essay.questions,
      curiosityHooks: essay.curiosityHooks,
      shareMessage: essay.shareMessage
    };
  });

  const week = {
    weekId,
    weekStart: formatDate(weekStart),
    generatedAt: new Date().toISOString(),
    timezone: 'Asia/Seoul',
    days
  };

  const meta = {
    weekId,
    weekStart: formatDate(weekStart),
    generatedAt: new Date().toISOString(),
    timezone: 'Asia/Seoul',
    unlockHour: 15,
    version: (loadJSON(path.join(DATA, 'meta.json'), {}).version || 0) + 1
  };

  // Update state — track words & topics so future banks skip repeats
  selected.forEach(essay => {
    if (!state.usedEssayIds.includes(essay.id)) state.usedEssayIds.push(essay.id);
    if (!state.usedTopics.includes(essay.topic)) state.usedTopics.push(essay.topic);
    essay.words.forEach(w => {
      if (!state.usedWords.includes(w.word)) state.usedWords.push(w.word);
    });
  });
  state.totalEssaysServed += 7;
  state.lastGenerated = new Date().toISOString();

  fs.writeFileSync(path.join(DATA, 'week.json'), JSON.stringify(week, null, 2));
  fs.writeFileSync(path.join(DATA, 'meta.json'), JSON.stringify(meta, null, 2));
  fs.writeFileSync(statePath, JSON.stringify(state, null, 2));

  console.log(`Generated week ${weekId} (${formatDate(weekStart)} – ${days[6].date})`);
  console.log(`Essays: ${selected.map(e => e.id).join(', ')}`);
  console.log(`Total words in vault: ${state.usedWords.length} | Essays served: ${state.totalEssaysServed}`);
}

main();

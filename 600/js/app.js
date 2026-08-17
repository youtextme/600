/**
 * 600 — Kid-first daily discovery (age 9)
 * Week: Monday → Sunday | Unlock: 3 PM KST
 */

import {
  speak, speakWord, speakEncourage, speakCorrect, speakHint, speakCelebrate, loadVoices
} from './voice.js';

const KST_OFFSET = 9 * 60;
const DAY_LABELS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
const LETTERS = ['A', 'B', 'C', 'D'];

const $ = (sel) => document.querySelector(sel);

let weekData = null;
let selectedDayIndex = null;

// ─── KST time ─────────────────────────────────────────────────────

function nowKST() {
  const now = new Date();
  const utc = now.getTime() + now.getTimezoneOffset() * 60000;
  return new Date(utc + KST_OFFSET * 60000);
}

function getUnlockTime(dateStr) {
  const [y, m, d] = dateStr.split('-').map(Number);
  return new Date(Date.UTC(y, m - 1, d, 6, 0, 0)); // 3 PM KST
}

function isDayUnlocked(day) {
  return nowKST() >= getUnlockTime(day.date);
}

function getActiveDayIndex() {
  if (!weekData?.days) return 0;
  let last = -1;
  for (let i = 0; i < weekData.days.length; i++) {
    if (isDayUnlocked(weekData.days[i])) last = i;
  }
  return Math.max(0, last);
}

function formatCountdown(ms) {
  const h = Math.floor(ms / 3600000);
  const m = Math.floor((ms % 3600000) / 60000);
  return `${h}h ${m}m`;
}

// ─── Data ─────────────────────────────────────────────────────────

async function loadData() {
  const base = document.querySelector('meta[name="base-path"]')?.content || './';
  const res = await fetch(`${base}data/week.json?t=${Date.now()}`);
  weekData = await res.json();
}

function progressKey(dayId) {
  return `600-v2-${weekData.weekId}-${dayId}`;
}

function loadProgress(dayId) {
  try {
    return JSON.parse(localStorage.getItem(progressKey(dayId)) || '{}');
  } catch {
    return {};
  }
}

function saveProgress(dayId, data) {
  localStorage.setItem(progressKey(dayId), JSON.stringify(data));
}

function countCompletedDays() {
  return weekData.days.filter(d => loadProgress(d.id).quizComplete).length;
}

// ─── Week strip ───────────────────────────────────────────────────

function renderWeekStrip() {
  const strip = $('#week-strip');
  strip.innerHTML = '';
  const activeIdx = getActiveDayIndex();

  weekData.days.forEach((day, i) => {
    const unlocked = isDayUnlocked(day);
    const done = loadProgress(day.id).quizComplete;

    const pill = document.createElement('div');
    pill.className = 'day-pill';
    if (!unlocked) pill.classList.add('locked');
    if (i === (selectedDayIndex ?? activeIdx)) pill.classList.add('active');
    if (done) pill.classList.add('done');

    pill.innerHTML = `
      <span class="day-label">${DAY_LABELS[i]}</span>
      <span class="check-mark">✓</span>
      <span class="day-icon">${done ? '' : unlocked ? '📖' : '🔒'}</span>
      <span class="day-title">${day.title}</span>
    `;

    if (unlocked) {
      pill.addEventListener('click', () => {
        selectedDayIndex = i;
        renderWeekStrip();
        renderDay(i);
      });
    }
    strip.appendChild(pill);
  });

  $('#streak-badge').textContent = `${countCompletedDays()}/7 done`;

  const countdownEl = $('#countdown');
  const nextLocked = weekData.days.find(d => !isDayUnlocked(d));
  if (nextLocked) {
    const diff = getUnlockTime(nextLocked.date) - new Date();
    if (diff > 0) {
      countdownEl.textContent = `⏳ "${nextLocked.title}" unlocks in ${formatCountdown(diff)}`;
      countdownEl.classList.remove('hidden');
    } else countdownEl.classList.add('hidden');
  } else countdownEl.classList.add('hidden');
}

// ─── Day content ──────────────────────────────────────────────────

function renderDay(index) {
  const day = weekData.days[index];
  if (!day || !isDayUnlocked(day)) return;

  $('#loading').classList.add('hidden');
  $('#main-content').classList.remove('hidden');

  const done = loadProgress(day.id).quizComplete;
  $('#mission-tag').textContent = done ? '✅ Completed!' : `Mission · ${DAY_LABELS[index]}`;
  $('#essay-title').textContent = day.title;

  const vocabBar = $('#vocab-bar');
  vocabBar.innerHTML = '';
  (day.words || []).forEach(w => {
    const chip = document.createElement('button');
    chip.className = 'vocab-chip';
    chip.type = 'button';
    chip.innerHTML = `
      <div class="word-row">
        <span class="word">${w.word}</span>
        <span class="speaker" aria-label="Hear word">🔊</span>
      </div>
      <span class="example">${w.exampleSentence || w.definition}</span>
    `;
    chip.addEventListener('click', () => {
      speakWord(w.word);
      showToast(w.definition);
    });
    vocabBar.appendChild(chip);
  });

  $('#passage').innerHTML = day.passageHtml;

  document.querySelectorAll('.vocab-word').forEach(el => {
    el.addEventListener('click', () => {
      speakWord(el.dataset.word || el.textContent);
    });
  });

  $('#curiosity-list').innerHTML = (day.curiosityHooks || [])
    .map(h => `<li>${h}</li>`).join('');

  renderQuiz(day);
  if (done) showReportCard(day, false);
  else $('#report-card').classList.add('hidden');
}

// ─── MCQ Quiz ─────────────────────────────────────────────────────

function renderQuiz(day) {
  const container = $('#questions');
  container.innerHTML = '';
  const progress = loadProgress(day.id);
  if (!progress.answers) progress.answers = {};

  (day.questions || []).forEach((q, qi) => {
    const saved = progress.answers[q.id] || {};
    const block = document.createElement('div');
    block.className = 'question-block';
    if (saved.correct) block.classList.add('correct');

    const options = q.options || [];
    const letters = LETTERS.slice(0, options.length);

    block.innerHTML = `
      <div class="question-num">Question ${qi + 1} of ${day.questions.length}</div>
      <div class="question-text">${q.question}</div>
      <div class="options" role="radiogroup"></div>
      <div class="reveal-hint" id="hint-${q.id}"></div>
    `;

    const optionsEl = block.querySelector('.options');
    const hintEl = block.querySelector('.reveal-hint');

    options.forEach((opt, oi) => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'option-btn';
      btn.dataset.index = oi;
      btn.innerHTML = `<span class="letter">${letters[oi]}</span><span>${opt}</span>`;
      if (saved.correct) btn.disabled = true;
      if (saved.correct && oi === q.correctIndex) btn.classList.add('correct-opt');

      btn.addEventListener('click', () => handleAnswer(day, q, oi, btn, block, hintEl, optionsEl));
      optionsEl.appendChild(btn);
    });

    if (saved.revealShown && q.revealHint) {
      hintEl.innerHTML = formatHint(q.revealHint);
      hintEl.classList.add('visible');
    }

    container.appendChild(block);
  });
}

async function handleAnswer(day, q, chosenIndex, btn, block, hintEl, optionsEl) {
  const progress = loadProgress(day.id);
  if (!progress.answers) progress.answers = {};
  if (!progress.answers[q.id]) progress.answers[q.id] = { wrongCount: 0 };
  const ans = progress.answers[q.id];
  if (ans.correct) return;

  const buttons = [...optionsEl.querySelectorAll('.option-btn')];

  if (chosenIndex === q.correctIndex) {
    ans.correct = true;
    ans.firstTry = (ans.wrongCount || 0) === 0;
    btn.classList.add('correct-opt');
    buttons.forEach(b => b.disabled = true);
    block.classList.add('correct');
    saveProgress(day.id, progress);
    await speakCorrect();
    checkQuizComplete(day);
    return;
  }

  // Wrong answer
  ans.wrongCount = (ans.wrongCount || 0) + 1;
  block.classList.add('wrong-pulse');
  setTimeout(() => block.classList.remove('wrong-pulse'), 400);

  if (ans.wrongCount === 1) {
    await speakEncourage();
    saveProgress(day.id, progress);
    return;
  }

  // Second wrong — reveal hint with answer
  ans.revealShown = true;
  if (q.revealHint) {
    hintEl.innerHTML = formatHint(q.revealHint);
    hintEl.classList.add('visible');
    await speakHint(q.revealHint);
  }
  saveProgress(day.id, progress);
}

function formatHint(text) {
  return text.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
}

function checkQuizComplete(day) {
  const progress = loadProgress(day.id);
  const allDone = day.questions.every(q => progress.answers?.[q.id]?.correct);
  if (allDone) {
    progress.quizComplete = true;
    saveProgress(day.id, progress);
    showReportCard(day, true);
    renderWeekStrip();
  }
}

function showReportCard(day, withVoice) {
  const progress = loadProgress(day.id);
  let firstTry = 0;
  let retries = 0;

  day.questions.forEach(q => {
    const a = progress.answers?.[q.id];
    if (!a?.correct) return;
    if (a.firstTry) firstTry++;
    else retries++;
  });

  const total = day.questions.length;
  $('#score-message').textContent =
    firstTry === total
      ? '🌟 Every answer right on the first try! You read like a pro.'
      : retries > 0
        ? '💪 You stuck with it and figured it out. That is what curious minds do!'
        : '✅ All done! You are building an awesome reading habit.';

  $('#first-try-count').textContent = firstTry;
  $('#retry-count').textContent = retries;
  $('#report-card').classList.remove('hidden');
  $('#report-card').scrollIntoView({ behavior: 'smooth', block: 'center' });

  if (withVoice) speakCelebrate();

  $('#share-btn').onclick = () => shareProgress(day);
  $('#retry-quiz-btn').onclick = () => {
    const p = loadProgress(day.id);
    delete p.quizComplete;
    p.answers = {};
    saveProgress(day.id, p);
    $('#report-card').classList.add('hidden');
    renderQuiz(day);
    renderWeekStrip();
  };
}

function shareProgress(day) {
  const msg = day.shareMessage || `I finished today's 600 reading: ${day.title}!`;
  navigator.clipboard.writeText(msg).then(() => {
    showToast('Copied! Paste in WhatsApp 📱');
  }).catch(() => {
    const ta = document.createElement('textarea');
    ta.value = msg;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToast('Copied! Paste in WhatsApp 📱');
  });
}

function showToast(text) {
  const t = $('#toast');
  t.textContent = text;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2800);
}

// ─── Init ─────────────────────────────────────────────────────────

async function init() {
  try {
    loadVoices();
    await loadData();
    selectedDayIndex = getActiveDayIndex();
    renderWeekStrip();
    renderDay(selectedDayIndex);

    setInterval(() => {
      const prev = selectedDayIndex;
      renderWeekStrip();
      const active = getActiveDayIndex();
      if (active !== prev) {
        selectedDayIndex = active;
        renderDay(active);
      }
    }, 60000);

    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('./sw.js').catch(() => {});
    }
  } catch (err) {
    $('#loading').textContent = 'Oops — could not load. Try refreshing!';
    console.error(err);
  }
}

init();

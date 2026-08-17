/**
 * 600 — Daily discovery reader for Ayaan
 * Unlock: 3:00 PM KST daily | Week refresh: Sunday 8:00 AM KST
 */

const KST_OFFSET = 9 * 60; // minutes ahead of UTC
const UNLOCK_HOUR = 15; // 3 PM

const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => document.querySelectorAll(sel);

let weekData = null;
let metaData = null;
let selectedDayIndex = null;

// ─── Time helpers (KST) ───────────────────────────────────────────

function nowKST() {
  const now = new Date();
  const utc = now.getTime() + now.getTimezoneOffset() * 60000;
  return new Date(utc + KST_OFFSET * 60000);
}

function parseDateKST(dateStr) {
  const [y, m, d] = dateStr.split('-').map(Number);
  return new Date(Date.UTC(y, m - 1, d, KST_OFFSET / 60 - 12, 0, 0));
}

function getUnlockTime(dateStr) {
  const [y, m, d] = dateStr.split('-').map(Number);
  // 3 PM KST = 6 AM UTC
  return new Date(Date.UTC(y, m - 1, d, 6, 0, 0));
}

function isDayUnlocked(day) {
  return nowKST() >= getUnlockTime(day.date);
}

function getActiveDayIndex() {
  if (!weekData?.days) return 0;
  let lastUnlocked = -1;
  for (let i = 0; i < weekData.days.length; i++) {
    if (isDayUnlocked(weekData.days[i])) lastUnlocked = i;
  }
  return Math.max(0, lastUnlocked);
}

function formatCountdown(ms) {
  const h = Math.floor(ms / 3600000);
  const m = Math.floor((ms % 3600000) / 60000);
  const s = Math.floor((ms % 60000) / 1000);
  return `${h}h ${m}m ${s}s`;
}

// ─── Data loading ─────────────────────────────────────────────────

async function loadData() {
  const base = document.querySelector('meta[name="base-path"]')?.content || './';
  const [weekRes, metaRes] = await Promise.all([
    fetch(`${base}data/week.json?t=${Date.now()}`),
    fetch(`${base}data/meta.json?t=${Date.now()}`)
  ]);
  weekData = await weekRes.json();
  metaData = await metaRes.json();
}

// ─── Progress (localStorage) ──────────────────────────────────────

function progressKey(dayId) {
  return `600-progress-${weekData.weekId}-${dayId}`;
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

// ─── Speech ───────────────────────────────────────────────────────

function speak(text) {
  if (!window.speechSynthesis) {
    showToast('Speech not supported on this device');
    return;
  }
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'en-US';
  u.rate = 0.85;
  const voices = speechSynthesis.getVoices();
  const en = voices.find(v => v.lang.startsWith('en') && v.name.includes('Google'))
    || voices.find(v => v.lang.startsWith('en'));
  if (en) u.voice = en;
  speechSynthesis.speak(u);
}

// ─── UI: Week strip ───────────────────────────────────────────────

function renderWeekStrip() {
  const strip = $('#week-strip');
  strip.innerHTML = '';
  const activeIdx = getActiveDayIndex();
  const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

  weekData.days.forEach((day, i) => {
    const unlocked = isDayUnlocked(day);
    const progress = loadProgress(day.id);
    const quizDone = progress.quizComplete;

    const pill = document.createElement('div');
    pill.className = 'day-pill';
    if (!unlocked) pill.classList.add('locked');
    if (i === (selectedDayIndex ?? activeIdx)) pill.classList.add('active');
    if (quizDone) pill.classList.add('done');

    const d = new Date(day.date + 'T00:00:00');
    pill.innerHTML = `
      <span class="day-label">${days[d.getDay()]}</span>
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

  // Countdown to next unlock
  const countdownEl = $('#countdown');
  const nextLocked = weekData.days.find(d => !isDayUnlocked(d));
  if (nextLocked) {
    const unlockAt = getUnlockTime(nextLocked.date);
    const diff = unlockAt - new Date();
    if (diff > 0) {
      countdownEl.textContent = `Next essay unlocks in ${formatCountdown(diff)} — "${nextLocked.title}"`;
      countdownEl.classList.remove('hidden');
    } else {
      countdownEl.classList.add('hidden');
    }
  } else {
    countdownEl.classList.add('hidden');
  }
}

// ─── UI: Day content ──────────────────────────────────────────────

function renderDay(index) {
  const day = weekData.days[index];
  if (!day || !isDayUnlocked(day)) return;

  $('#loading').classList.add('hidden');
  $('#main-content').classList.remove('hidden');

  $('#essay-title').textContent = day.title;

  // Vocab bar
  const vocabBar = $('#vocab-bar');
  vocabBar.innerHTML = '';
  day.words.forEach(w => {
    const chip = document.createElement('button');
    chip.className = 'vocab-chip';
    chip.innerHTML = `<span>${w.word}</span><span class="speaker">🔊</span>`;
    chip.title = w.definition;
    chip.addEventListener('click', () => speak(w.word));
    vocabBar.appendChild(chip);
  });

  // Passage
  $('#passage').innerHTML = day.passageHtml;

  $$('.vocab-word').forEach(el => {
    el.addEventListener('click', () => {
      speak(el.dataset.word || el.textContent);
      showToast(el.title || el.textContent);
    });
  });

  // Grammar
  const rules = day.grammarRules.map(r => r.name).join(' · ');
  $('#grammar-note').innerHTML = `<strong>Grammar you're absorbing:</strong> ${rules}`;

  // Curiosity
  const curList = $('#curiosity-list');
  curList.innerHTML = day.curiosityHooks.map(h => `<li>${h}</li>`).join('');

  renderQuiz(day);
  $('#report-card').classList.add('hidden');
}

// ─── Quiz ─────────────────────────────────────────────────────────

function normalizeAnswer(s) {
  return s.trim().toLowerCase().replace(/[.,!?;:'"]/g, '').replace(/\s+/g, ' ');
}

function answersMatch(input, accepted) {
  const n = normalizeAnswer(input);
  return accepted.some(a => {
    const na = normalizeAnswer(a);
    return n === na || n.includes(na) || na.includes(n);
  });
}

function renderQuiz(day) {
  const container = $('#questions');
  container.innerHTML = '';
  const progress = loadProgress(day.id);
  if (!progress.answers) progress.answers = {};

  day.questions.forEach((q, qi) => {
    const block = document.createElement('div');
    block.className = 'question-block';
    block.dataset.qid = q.id;

    const saved = progress.answers[q.id];
    if (saved?.correct) block.classList.add('answered-correct');
    else if (saved?.attempts > 1) block.classList.add('answered-retry');

    block.innerHTML = `
      <div class="question-text">${qi + 1}. ${q.question}</div>
      <button class="hint-btn" type="button">💡 Show hint</button>
      <div class="hint-text">${q.hint}</div>
      <input class="answer-input" type="text" placeholder="Type your answer…" ${saved?.correct ? 'disabled' : ''} value="${saved?.lastAnswer || ''}">
      <button class="check-btn" ${saved?.correct ? 'disabled' : ''}>Check</button>
      <div class="feedback"></div>
    `;

    const hintBtn = block.querySelector('.hint-btn');
    const hintText = block.querySelector('.hint-text');
    const input = block.querySelector('.answer-input');
    const checkBtn = block.querySelector('.check-btn');
    const feedback = block.querySelector('.feedback');

    hintBtn.addEventListener('click', () => {
      hintText.classList.add('visible');
      if (!progress.answers[q.id]) progress.answers[q.id] = { attempts: 0, hints: 0 };
      progress.answers[q.id].hints = (progress.answers[q.id].hints || 0) + 1;
      saveProgress(day.id, progress);
    });

    checkBtn.addEventListener('click', () => {
      if (!progress.answers[q.id]) progress.answers[q.id] = { attempts: 0, hints: 0 };
      const ans = progress.answers[q.id];
      ans.attempts = (ans.attempts || 0) + 1;
      ans.lastAnswer = input.value;

      if (answersMatch(input.value, q.answers)) {
        ans.correct = true;
        ans.firstTry = ans.attempts === 1 && (ans.hints || 0) === 0;
        feedback.textContent = `✓ ${q.explanation}`;
        feedback.className = 'feedback show correct';
        block.classList.add('answered-correct');
        input.disabled = true;
        checkBtn.disabled = true;
        saveProgress(day.id, progress);
        checkQuizComplete(day);
      } else {
        feedback.textContent = 'Not quite — reread the passage and try again. Good questioners persist.';
        feedback.className = 'feedback show retry';
        block.classList.add('answered-retry');
        saveProgress(day.id, progress);
      }
    });

    input.addEventListener('keydown', e => {
      if (e.key === 'Enter') checkBtn.click();
    });

    container.appendChild(block);
  });

  if (progress.quizComplete) showReportCard(day);
}

function checkQuizComplete(day) {
  const progress = loadProgress(day.id);
  const allCorrect = day.questions.every(q => progress.answers?.[q.id]?.correct);
  if (allCorrect) {
    progress.quizComplete = true;
    saveProgress(day.id, progress);
    showReportCard(day);
    renderWeekStrip();
  }
}

function showReportCard(day) {
  const progress = loadProgress(day.id);
  let firstTry = 0;
  let retries = 0;

  day.questions.forEach(q => {
    const a = progress.answers?.[q.id];
    if (!a) return;
    if (a.firstTry) firstTry++;
    else retries++;
  });

  const total = day.questions.length;
  const pct = Math.round((firstTry / total) * 100);

  $('#score-display').textContent = `${firstTry}/${total}`;
  $('#score-message').textContent =
    firstTry === total
      ? '🌟 Perfect on the first try! You read like a scientist.'
      : firstTry >= total / 2
        ? 'Strong work! The retries made your understanding sharper.'
        : 'You stuck with it — that curiosity is what matters most.';

  $('#first-try-count').textContent = firstTry;
  $('#retry-count').textContent = retries;
  $('#report-card').classList.remove('hidden');

  $('#share-btn').onclick = () => shareProgress(day, firstTry, total);
  $('#retry-quiz-btn').onclick = () => {
    const p = loadProgress(day.id);
    delete p.quizComplete;
    Object.keys(p.answers || {}).forEach(k => delete p.answers[k]);
    saveProgress(day.id, p);
    renderQuiz(day);
    $('#report-card').classList.add('hidden');
  };
}

// ─── Share ────────────────────────────────────────────────────────

function shareProgress(day, firstTry, total) {
  const msg = day.shareMessage;
  navigator.clipboard.writeText(msg).then(() => {
    showToast('Copied! Paste into WhatsApp 📱');
  }).catch(() => {
    const ta = document.createElement('textarea');
    ta.value = msg;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToast('Copied! Paste into WhatsApp 📱');
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
    await loadData();
    selectedDayIndex = getActiveDayIndex();
    renderWeekStrip();
    renderDay(selectedDayIndex);

    // Refresh countdown every minute
    setInterval(() => {
      const prev = selectedDayIndex;
      renderWeekStrip();
      if (getActiveDayIndex() !== prev) {
        selectedDayIndex = getActiveDayIndex();
        renderDay(selectedDayIndex);
      }
    }, 60000);

    // Load voices for speech
    if (window.speechSynthesis) {
      speechSynthesis.getVoices();
      speechSynthesis.onvoiceschanged = () => speechSynthesis.getVoices();
    }
  } catch (err) {
    $('#loading').textContent = 'Could not load today\'s essay. Check back soon.';
    console.error(err);
  }
}

init();

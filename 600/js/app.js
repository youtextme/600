/**
 * 600 — World-class kid discovery app (age 9)
 * Step flow · MCQ wizard · curiosity hooks · responsive
 */

import {
  emojiForTopic, buildCuriosityHook, WONDER_PROMPTS, GROWTH, pick
} from './expert.js';
import {
  speak, speakWord, speakEncourage, speakCorrect, speakHint, speakCelebrate, loadVoices
} from './voice.js';

const KST_OFFSET = 9 * 60;
const DAY_LABELS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
const LETTERS = ['A', 'B', 'C', 'D'];
const STEPS = ['hook', 'words', 'story', 'quiz'];

const $ = (s) => document.querySelector(s);
const $$ = (s) => document.querySelectorAll(s);

let weekData = null;
let selectedDayIndex = null;
let currentDay = null;
let currentStep = 'hook';
let quizIndex = 0;
let readAloudActive = false;

// ─── Time (KST) ───────────────────────────────────────────────────

function nowKST() {
  const n = new Date();
  return new Date(n.getTime() + n.getTimezoneOffset() * 60000 + KST_OFFSET * 60000);
}

function getUnlockTime(dateStr) {
  const [y, m, d] = dateStr.split('-').map(Number);
  return new Date(Date.UTC(y, m - 1, d, 6, 0, 0));
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

// ─── Data & progress ──────────────────────────────────────────────

async function loadData() {
  const base = $('meta[name="base-path"]')?.content || './';
  const res = await fetch(`${base}data/week.json?t=${Date.now()}`);
  weekData = await res.json();
}

function progressKey(dayId) {
  return `600-v3-${weekData.weekId}-${dayId}`;
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

function getDayProgress(day) {
  const p = loadProgress(day.id);
  return {
    hook: true,
    words: !!p.wordsDone,
    story: !!p.storyDone,
    quiz: !!p.quizComplete,
    ...p,
  };
}

// ─── Step navigation ──────────────────────────────────────────────

function goToStep(step) {
  currentStep = step;
  STEPS.forEach(s => {
    $(`#panel-${s}`)?.classList.toggle('active', s === step);
  });
  $('#panel-done')?.classList.toggle('active', step === 'done');
  $('#panel-done')?.classList.toggle('hidden', step !== 'done');

  $$('.step-btn').forEach(btn => {
    const s = btn.dataset.step;
    btn.classList.toggle('active', s === step);
    if (currentDay) {
      const p = getDayProgress(currentDay);
      btn.classList.toggle('done-step', p[s]);
    }
  });

  $$('.bn-item').forEach(btn => {
    const s = btn.dataset.step;
    btn.classList.toggle('active', s === step);
    if (currentDay) {
      btn.classList.toggle('done-step', getDayProgress(currentDay)[s]);
    }
  });

  updateJourneyBar();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function updateJourneyBar() {
  if (!currentDay) return;
  const p = getDayProgress(currentDay);
  let pct = 0;
  if (p.quiz) pct = 100;
  else if (currentStep === 'quiz') pct = 75;
  else if (currentStep === 'story' || p.storyDone) pct = 50;
  else if (currentStep === 'words' || p.wordsDone) pct = 35;
  else if (currentStep === 'hook') pct = 10;
  $('#journey-fill').style.width = `${pct}%`;
}

// ─── Week strip ───────────────────────────────────────────────────

function renderWeekStrip() {
  const strip = $('#week-strip');
  strip.innerHTML = '';
  const activeIdx = getActiveDayIndex();

  weekData.days.forEach((day, i) => {
    const unlocked = isDayUnlocked(day);
    const done = loadProgress(day.id).quizComplete;

    const pill = document.createElement('button');
    pill.type = 'button';
    pill.className = 'day-pill';
    pill.setAttribute('role', 'tab');
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

  const doneCount = weekData.days.filter(d => loadProgress(d.id).quizComplete).length;
  $('#streak-badge').textContent = `${doneCount}/7 ✓`;

  const countdownEl = $('#countdown');
  const nextLocked = weekData.days.find(d => !isDayUnlocked(d));
  if (nextLocked) {
    const diff = getUnlockTime(nextLocked.date) - new Date();
    if (diff > 0) {
      countdownEl.textContent = `⏳ Next adventure unlocks in ${formatCountdown(diff)}`;
      countdownEl.classList.remove('hidden');
    } else countdownEl.classList.add('hidden');
  } else countdownEl.classList.add('hidden');
}

// ─── Enrich passage with wonder pauses ────────────────────────────

function enrichPassage(html) {
  const div = document.createElement('div');
  div.innerHTML = html;
  const ps = [...div.querySelectorAll('p')];
  let wonderIdx = 0;
  ps.forEach((p, i) => {
    if (i > 0 && i % 3 === 0 && wonderIdx < WONDER_PROMPTS.length) {
      const box = document.createElement('p');
      box.className = 'wonder-pause';
      box.textContent = `💭 ${WONDER_PROMPTS[wonderIdx++]}`;
      p.before(box);
    }
  });
  return div.innerHTML;
}

// ─── Render day ───────────────────────────────────────────────────

function renderDay(index) {
  const day = weekData.days[index];
  if (!day || !isDayUnlocked(day)) return;

  currentDay = day;
  quizIndex = 0;

  $('#loading').classList.add('hidden');
  $('#main-content').classList.remove('hidden');
  $('#bottom-nav').classList.remove('hidden');

  const prog = getDayProgress(day);
  const done = prog.quizComplete;

  $('#hero-emoji').textContent = emojiForTopic(day.topic);
  $('#mission-tag').textContent = done ? '✅ Completed!' : `Adventure · ${DAY_LABELS[index]}`;
  $('#essay-title').textContent = day.title;
  $('#curiosity-hook').textContent = buildCuriosityHook(day);

  // Vocab carousel
  const vocabBar = $('#vocab-bar');
  vocabBar.innerHTML = '';
  const dots = $('#vocab-dots');
  dots.innerHTML = '';

  (day.words || []).forEach((w, wi) => {
    const card = document.createElement('div');
    card.className = 'vocab-card';
    card.innerHTML = `
      <div class="word">${w.word}</div>
      <div class="def">${w.definition}</div>
      <div class="example">"${w.exampleSentence || w.definition}"</div>
      <button type="button" class="hear-btn">🔊 Hear it</button>
    `;
    card.querySelector('.hear-btn').addEventListener('click', () => {
      speakWord(w.word, w.definition);
    });
    vocabBar.appendChild(card);

    const dot = document.createElement('span');
    if (wi === 0) dot.classList.add('on');
    dots.appendChild(dot);
  });

  vocabBar.addEventListener('scroll', () => {
    const idx = Math.round(vocabBar.scrollLeft / (vocabBar.querySelector('.vocab-card')?.offsetWidth + 12 || 1));
    dots.querySelectorAll('span').forEach((d, i) => d.classList.toggle('on', i === idx));
  }, { passive: true });

  // Story
  $('#passage').innerHTML = enrichPassage(day.passageHtml);
  document.querySelectorAll('.vocab-word').forEach(el => {
    el.addEventListener('click', () => speakWord(el.dataset.word || el.textContent));
  });

  $('#curiosity-list').innerHTML = (day.curiosityHooks || [])
    .map(h => `<li>${h}</li>`).join('');

  setupReadProgress();
  setupReadAloud(day);

  if (done) {
    goToStep('done');
    showReportCard(day, false);
  } else {
    const resume = prog.storyDone ? 'quiz' : prog.wordsDone ? 'story' : 'hook';
    goToStep(resume);
    renderQuizWizard(day);
  }

  renderWeekStrip();
}

// ─── Reading progress ─────────────────────────────────────────────

function setupReadProgress() {
  const passage = $('#passage');
  const fill = $('#read-progress-fill');
  const label = $('#read-progress-label');

  function onScroll() {
    const rect = passage.getBoundingClientRect();
    const vh = window.innerHeight;
    const total = passage.scrollHeight;
    const seen = Math.min(total, Math.max(0, vh - rect.top));
    const pct = Math.min(100, Math.round((seen / total) * 100));
    fill.style.width = `${pct}%`;
    label.textContent = `${pct}% read`;
    if (currentDay && pct >= 85) {
      const p = loadProgress(currentDay.id);
      p.storyDone = true;
      saveProgress(currentDay.id, p);
    }
  }

  $('.scroll-main').onscroll = onScroll;
  window.onscroll = onScroll;
  onScroll();
}

// ─── Read aloud ───────────────────────────────────────────────────

function setupReadAloud(day) {
  const btn = $('#read-aloud-btn');
  btn.onclick = async () => {
    if (readAloudActive) {
      speechSynthesis.cancel();
      readAloudActive = false;
      btn.textContent = '🔊 Read aloud';
      return;
    }
    readAloudActive = true;
    btn.textContent = '⏹ Stop';
    const text = $('#passage').innerText;
    await speak(text, { rate: 0.88, pitch: 1.02 });
    readAloudActive = false;
    btn.textContent = '🔊 Read aloud';
  };
}

// ─── Quiz wizard (one question at a time) ──────────────────────────

function renderQuizWizard(day) {
  quizIndex = 0;
  renderOneQuestion(day);
  renderQuizDots(day);
}

function renderQuizDots(day) {
  const dots = $('#quiz-dots');
  dots.innerHTML = '';
  day.questions.forEach((_, i) => {
    const d = document.createElement('span');
    const prog = loadProgress(day.id);
    const qid = day.questions[i].id;
    if (prog.answers?.[qid]?.correct) d.classList.add('on');
    else if (i === quizIndex) d.classList.add('on');
    dots.appendChild(d);
  });
}

function renderOneQuestion(day) {
  const stage = $('#quiz-stage');
  const progress = loadProgress(day.id);
  if (!progress.answers) progress.answers = {};

  // Skip to first unanswered
  while (quizIndex < day.questions.length && progress.answers[day.questions[quizIndex].id]?.correct) {
    quizIndex++;
  }

  if (quizIndex >= day.questions.length) {
    checkQuizComplete(day);
    return;
  }

  const q = day.questions[quizIndex];
  const saved = progress.answers[q.id] || {};
  const block = document.createElement('div');
  block.className = 'question-block';

  block.innerHTML = `
    <div class="question-num">Question ${quizIndex + 1} of ${day.questions.length}</div>
    <div class="question-text">${q.question}</div>
    <div class="options" role="radiogroup"></div>
    <div class="reveal-hint"></div>
    <div class="quiz-next-wrap hidden"></div>
  `;

  const optionsEl = block.querySelector('.options');
  const hintEl = block.querySelector('.reveal-hint');

  (q.options || []).forEach((opt, oi) => {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'option-btn';
    btn.innerHTML = `<span class="letter">${LETTERS[oi]}</span><span>${opt}</span>`;
    if (saved.correct && oi === q.correctIndex) btn.classList.add('correct-opt');
    if (!saved.correct) {
      btn.addEventListener('click', () => handleAnswer(day, q, oi, btn, block, hintEl, optionsEl));
    } else {
      btn.disabled = true;
    }
    optionsEl.appendChild(btn);
  });

  if (saved.revealShown && q.revealHint) {
    hintEl.innerHTML = formatHint(q.revealHint);
    hintEl.classList.add('visible');
  }

  stage.innerHTML = '';
  stage.appendChild(block);
  renderQuizDots(day);
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
    saveProgress(day.id, progress);
    await speakCorrect(pick(GROWTH.correct));

    setTimeout(() => {
      quizIndex++;
      renderOneQuestion(day);
    }, 900);
    return;
  }

  ans.wrongCount = (ans.wrongCount || 0) + 1;
  btn.classList.add('wrong-flash');
  setTimeout(() => btn.classList.remove('wrong-flash'), 450);

  if (ans.wrongCount === 1) {
    await speakEncourage(pick(GROWTH.wrong1));
    saveProgress(day.id, progress);
    return;
  }

  ans.revealShown = true;
  if (q.revealHint) {
    hintEl.innerHTML = formatHint(q.revealHint);
    hintEl.classList.add('visible');
    await speakHint(q.revealHint);
  }
  saveProgress(day.id, progress);
}

function formatHint(t) {
  return t.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
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
  goToStep('done');

  const progress = loadProgress(day.id);
  let firstTry = 0, retries = 0;
  day.questions.forEach(q => {
    const a = progress.answers?.[q.id];
    if (!a?.correct) return;
    if (a.firstTry) firstTry++;
    else retries++;
  });

  const total = day.questions.length;
  $('#score-message').textContent =
    firstTry === total
      ? pick(GROWTH.complete) + ' Every answer on the first try!'
      : pick(GROWTH.complete);

  $('#first-try-count').textContent = firstTry;
  $('#retry-count').textContent = retries;

  if (withVoice) {
    speakCelebrate(pick(GROWTH.complete));
    launchConfetti();
  }

  $('#share-btn').onclick = () => shareProgress(day);
  $('#retry-quiz-btn').onclick = () => {
    const p = loadProgress(day.id);
    delete p.quizComplete;
    p.answers = {};
    quizIndex = 0;
    saveProgress(day.id, p);
    goToStep('quiz');
    renderQuizWizard(day);
    renderWeekStrip();
  };
}

// ─── Confetti (lightweight) ───────────────────────────────────────

function launchConfetti() {
  const canvas = $('#confetti');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  const pieces = Array.from({ length: 80 }, () => ({
    x: Math.random() * canvas.width,
    y: -10,
    r: 4 + Math.random() * 6,
    d: 2 + Math.random() * 4,
    c: Math.random() > 0.5 ? '#000' : '#16a34a',
  }));

  let frame = 0;
  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    pieces.forEach(p => {
      p.y += p.d;
      p.x += Math.sin(frame * 0.05 + p.x) * 0.8;
      ctx.fillStyle = p.c;
      ctx.fillRect(p.x, p.y, p.r, p.r);
    });
    frame++;
    if (frame < 120) requestAnimationFrame(draw);
    else ctx.clearRect(0, 0, canvas.width, canvas.height);
  }
  draw();
}

// ─── Share & toast ────────────────────────────────────────────────

function shareProgress(day) {
  const msg = day.shareMessage || `I finished today's 600 adventure: ${day.title}!`;
  navigator.clipboard.writeText(msg).then(() => {
    showToast('Copied! Paste in WhatsApp 📱');
  }).catch(() => {
    const ta = document.createElement('textarea');
    ta.value = msg;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToast('Copied!');
  });
}

function showToast(text) {
  const t = $('#toast');
  t.textContent = text;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2800);
}

// ─── Wire UI ──────────────────────────────────────────────────────

function wireUI() {
  $('#start-btn').addEventListener('click', () => goToStep('words'));

  $('#words-done-btn').addEventListener('click', () => {
    if (currentDay) {
      const p = loadProgress(currentDay.id);
      p.wordsDone = true;
      saveProgress(currentDay.id, p);
    }
    goToStep('story');
  });

  $('#story-done-btn').addEventListener('click', () => {
    if (currentDay) {
      const p = loadProgress(currentDay.id);
      p.storyDone = true;
      saveProgress(currentDay.id, p);
      renderQuizWizard(currentDay);
    }
    goToStep('quiz');
  });

  $$('.step-btn, .bn-item').forEach(btn => {
    btn.addEventListener('click', () => {
      const step = btn.dataset.step;
      if (!step || step === currentStep) return;
      if (step === 'quiz' && currentDay) renderQuizWizard(currentDay);
      goToStep(step);
    });
  });
}

// ─── Init ─────────────────────────────────────────────────────────

async function init() {
  try {
    loadVoices();
    wireUI();
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
    $('#loading').innerHTML = '<p>Oops — tap refresh and try again!</p>';
    console.error(err);
  }
}

init();

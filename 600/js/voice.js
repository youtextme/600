/**
 * Kid-friendly voice — warmer, less robotic.
 * Prefers natural premium voices on iOS/Android/desktop.
 */

let voiceCache = null;

const VOICE_PRIORITY = [
  'Samantha', 'Karen', 'Daniel', 'Moira', 'Tessa',
  'Google UK English Female', 'Google US English', 'Microsoft Zira',
  'Microsoft Aria', 'Microsoft Jenny', 'Fiona', 'Victoria',
];

export function loadVoices() {
  if (!window.speechSynthesis) return [];
  voiceCache = speechSynthesis.getVoices();
  return voiceCache;
}

function pickVoice() {
  const voices = loadVoices();
  if (!voices.length) return null;
  for (const name of VOICE_PRIORITY) {
    const v = voices.find(x => x.name.includes(name));
    if (v) return v;
  }
  return voices.find(v => v.lang.startsWith('en') && !v.name.toLowerCase().includes('compact'))
    || voices.find(v => v.lang.startsWith('en'));
}

export function speak(text, { rate = 0.94, pitch = 1.08, onEnd } = {}) {
  if (!window.speechSynthesis) return Promise.resolve();

  return new Promise(resolve => {
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'en-US';
    u.rate = rate;
    u.pitch = pitch;
    const voice = pickVoice();
    if (voice) u.voice = voice;

    u.onend = () => {
      onEnd?.();
      resolve();
    };
    u.onerror = () => resolve();
    speechSynthesis.speak(u);
  });
}

export function speakWord(word) {
  return speak(word, { rate: 0.82, pitch: 1.0 });
}

export function speakEncourage() {
  const lines = [
    "Not quite! That's okay — great minds try again. Check the passage if you need to.",
    "Hmm, not that one! You've got this. Reread the story and pick again.",
    "So close! Take another look at the passage. I believe in you.",
  ];
  return speak(lines[Math.floor(Math.random() * lines.length)], { rate: 0.92, pitch: 1.1 });
}

export function speakCorrect() {
  const lines = [
    "Yes! Nailed it!",
    "That's right! Brilliant!",
    "Correct! You're on fire today!",
  ];
  return speak(lines[Math.floor(Math.random() * lines.length)], { rate: 0.96, pitch: 1.12 });
}

export function speakHint(hintText) {
  const clean = hintText.replace(/\*\*/g, '');
  return speak(clean, { rate: 0.9, pitch: 1.05 });
}

export function speakCelebrate() {
  return speak("Amazing! You finished today's mission! Green tick for you!", { rate: 0.95, pitch: 1.15 });
}

if (typeof window !== 'undefined' && window.speechSynthesis) {
  loadVoices();
  speechSynthesis.onvoiceschanged = loadVoices;
}

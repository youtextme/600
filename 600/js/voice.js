/**
 * Warmer, kid-friendly voice selection
 */
let voiceCache = [];

const VOICE_PRIORITY = [
  'Samantha', 'Karen', 'Tessa', 'Moira', 'Daniel',
  'Google UK English Female', 'Google US English',
  'Microsoft Aria', 'Microsoft Jenny', 'Microsoft Zira',
  'Fiona', 'Victoria', 'Google UK English Male',
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
  return voices.find(v => v.lang.startsWith('en') && !/compact|novelty/i.test(v.name))
    || voices.find(v => v.lang.startsWith('en'));
}

export function speak(text, { rate = 0.92, pitch = 1.06, onEnd } = {}) {
  if (!window.speechSynthesis || !text) return Promise.resolve();

  return new Promise(resolve => {
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'en-US';
    u.rate = rate;
    u.pitch = pitch;
    const voice = pickVoice();
    if (voice) u.voice = voice;
    u.onend = () => { onEnd?.(); resolve(); };
    u.onerror = () => resolve();
    speechSynthesis.speak(u);
  });
}

export function speakWord(word, definition) {
  const line = definition
    ? `${word}. ${definition}`
    : word;
  return speak(line, { rate: 0.8, pitch: 1.0 });
}

export function speakEncourage(line) {
  return speak(line, { rate: 0.9, pitch: 1.08 });
}

export function speakCorrect(line) {
  return speak(line, { rate: 0.95, pitch: 1.12 });
}

export function speakHint(hintText) {
  return speak(hintText.replace(/\*\*/g, ''), { rate: 0.88, pitch: 1.04 });
}

export function speakCelebrate(line) {
  return speak(line, { rate: 0.93, pitch: 1.14 });
}

if (typeof window !== 'undefined' && window.speechSynthesis) {
  loadVoices();
  speechSynthesis.onvoiceschanged = loadVoices;
}

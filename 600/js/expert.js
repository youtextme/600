/**
 * Child-learning design principles (ages 8–10)
 * Based on: SDT (autonomy/competence/relatedness), cognitive load theory,
 * curiosity-gap research, growth mindset, and mobile UX for children.
 */

export const TOPIC_EMOJI = {
  'Bioluminescence': '🌊',
  'Fungal Tree Networks': '🌲',
  'Mantis Shrimp': '🦐',
  'Ancient Honey': '🍯',
  'Tardigrades': '🔬',
  'Viking Sunstone Navigation': '🧭',
  'Hummingbird Metabolism': '🐦',
  'Octopus Intelligence': '🐙',
  'Quantum Bird Navigation': '🐦',
  'Slime Mold Solving Mazes': '🧫',
  'Pompeii Bread Ovens': '🏛️',
  'Whale Song Culture': '🐋',
  'Bioluminescent Caves': '🦇',
  'Axolotl Regeneration': '🦎',
  'Ant Supercolonies': '🐜',
  'Memory Palace Technique History': '🧠',
  'Black Hole Light Bending': '🌌',
  'Venus Flytrap Mechanics': '🪴',
  'Silk Road Paper': '📜',
  'Coral Spawning Sync': '🪸',
  'Earthquake Animal Behavior': '🌍',
};

export function emojiForTopic(topic) {
  return TOPIC_EMOJI[topic] || '✨';
}

export function buildCuriosityHook(day) {
  const hooks = day.curiosityHooks || [];
  if (hooks[0]) return hooks[0];
  return `What if everything you thought about ${day.topic || 'this'} was only half the story?`;
}

export const WONDER_PROMPTS = [
  'Pause — what surprised you just now?',
  'Would you want to see this in real life? Why?',
  'What question would you ask a scientist about this?',
];

export const GROWTH = {
  wrong1: [
    "Good try! Scientists miss things all the time — look back at the story.",
    "Not that one, and that's okay! Check the passage and pick again.",
    "Hmm! Your brain is working — reread that part and have another go.",
  ],
  correct: [
    "Yes! You figured it out!",
    "That's it! Brilliant thinking!",
    "Nailed it! Your curiosity paid off!",
  ],
  complete: [
    "You did it! Today's mission is complete!",
    "Amazing! You finished the whole adventure!",
    "Wow — you read, learned new words, AND aced the quiz!",
  ],
};

export function pick(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

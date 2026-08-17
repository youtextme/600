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
  'essay-002': [
    { word: 'connected', definition: 'Linked together so parts affect one another', exampleSentence: 'My teacher said trees stay connected even when we cannot see the roots.' },
    { word: 'communicate', definition: 'To share information or messages', exampleSentence: 'I told my friend that trees might communicate through fungi underground.' },
    { word: 'discover', definition: 'To find something new or hidden', exampleSentence: 'Grandpa and I discovered mushrooms linked to an old oak tree.' },
    { word: 'network', definition: 'A system where many parts are linked together', exampleSentence: 'I explained to Ms. Chen that the forest works like a secret network.' },
    { word: 'underground', definition: 'Below the surface of the ground', exampleSentence: 'We learned that the biggest part of a fungus lives underground.' },
  ],
  'essay-003': [
    { word: 'incredible', definition: 'Hard to believe but true — amazing', exampleSentence: '"That mantis shrimp is incredible," I told my lab partner.' },
    { word: 'powerful', definition: 'Having great strength or force', exampleSentence: 'My friend said its punch is powerful enough to break aquarium glass.' },
    { word: 'colorful', definition: 'Full of bright, varied colors', exampleSentence: 'Grandpa laughed when I said the shrimp is more colorful than my art box.' },
    { word: 'compare', definition: 'To look at two things and notice how they are alike or different', exampleSentence: 'Ms. Ortiz asked us to compare the shrimp\'s eyes to ours.' },
    { word: 'protective', definition: 'Keeping someone or something safe from harm', exampleSentence: 'I said the hard shell is protective, like wearing a helmet.' },
  ],
  'essay-004': [
    { word: 'ancient', definition: 'Very, very old — from long ago', exampleSentence: 'This honey is ancient — older than my whole school, I told Grandpa.' },
    { word: 'preserve', definition: 'To keep something from spoiling or being destroyed', exampleSentence: 'Bees preserve honey so it lasts for years, Ms. Kim explained.' },
    { word: 'evidence', definition: 'Proof that something is true or happened', exampleSentence: 'I showed my friend the jar as evidence that honey never spoils.' },
    { word: 'appreciate', definition: 'To be thankful for something and understand its value', exampleSentence: 'I appreciate how hard bees work to make each drop of honey.' },
    { word: 'extraordinary', definition: 'Very unusual and impressively special', exampleSentence: 'Grandma said it is extraordinary that honey outlasted whole empires.' },
  ],
  'essay-005': [
    { word: 'survive', definition: 'To stay alive through difficult conditions', exampleSentence: 'Tardigrades can survive almost anything, I told my teacher.' },
    { word: 'microscopic', definition: 'Too tiny to see without a microscope', exampleSentence: 'They are microscopic, so we need special tools to see them.' },
    { word: 'extreme', definition: 'Very intense, severe, or far from normal', exampleSentence: 'My friend said extreme heat does not even kill them.' },
    { word: 'adapt', definition: 'To change in ways that help you handle new conditions', exampleSentence: 'I explained to Grandpa that they adapt when conditions get tough.' },
    { word: 'resilient', definition: 'Able to recover quickly or withstand hard times', exampleSentence: 'Ms. Lopez called them the most resilient animals on Earth.' },
  ],
  'essay-006': [
    { word: 'navigate', definition: 'To find your way across land or sea', exampleSentence: 'Vikings used a sunstone to navigate across foggy seas, I learned.' },
    { word: 'direction', definition: 'The way something is moving or facing', exampleSentence: 'The stone helped them find direction when the sun was hidden.' },
    { word: 'determine', definition: 'To figure out or decide something carefully', exampleSentence: 'I asked my teacher how they determined north without a compass.' },
    { word: 'ancient', definition: 'Very, very old — from long ago', exampleSentence: 'Grandpa said this ancient trick was smarter than it sounds.' },
    { word: 'clever', definition: 'Smart in a quick, creative way', exampleSentence: 'My friend agreed the Vikings were clever navigators.' },
  ],
  'essay-007': [
    { word: 'energy', definition: 'Power that lets you move, think, and stay active', exampleSentence: 'A hummingbird needs tons of energy to hover, Ms. Park said.' },
    { word: 'rapid', definition: 'Happening very quickly', exampleSentence: 'Its heart beats at a rapid speed — faster than mine ever could.' },
    { word: 'consume', definition: 'To eat or use something up', exampleSentence: 'I told Grandpa they consume more sugar than I eat in a week.' },
    { word: 'astonishing', definition: 'Extremely surprising — hard to believe', exampleSentence: 'The amount they eat is astonishing for such a tiny bird.' },
    { word: 'efficient', definition: 'Getting good results without wasting time or effort', exampleSentence: 'My friend said their wings are incredibly efficient.' },
  ],
  'essay-008': [
    { word: 'intelligent', definition: 'Very smart and quick to learn', exampleSentence: 'Octopuses are so intelligent, I told my science teacher.' },
    { word: 'escape', definition: 'To get away from a place or danger', exampleSentence: 'I watched a video where one tried to escape through a tiny gap.' },
    { word: 'curious', definition: 'Eager to learn and explore new things', exampleSentence: 'Grandpa said they are curious and will open jars just to explore.' },
    { word: 'problem', definition: 'Something difficult that needs a solution', exampleSentence: 'My friend and I tried to solve the same puzzle the octopus beat.' },
    { word: 'impressive', definition: 'Making you admire something because it is so good', exampleSentence: 'Ms. Torres said their problem-solving skills are impressive.' },
  ],
  'essay-009': [
    { word: 'navigate', definition: 'To find your way across long distances', exampleSentence: 'Birds navigate thousands of miles without maps, I explained to Dad.' },
    { word: 'mysterious', definition: 'Hard to understand or explain — full of secrets', exampleSentence: 'Grandpa called their inner compass mysterious and amazing.' },
    { word: 'direction', definition: 'The way something is moving or facing', exampleSentence: 'My teacher said they sense direction using light in their eyes.' },
    { word: 'investigate', definition: 'To look closely and ask questions to find answers', exampleSentence: 'Scientists investigate how birds know where to fly each season.' },
    { word: 'remarkable', definition: 'Worthy of attention — surprisingly impressive', exampleSentence: 'I told my friend it is remarkable that robins find the same yard every year.' },
  ],
  'essay-010': [
    { word: 'solution', definition: 'An answer to a problem or puzzle', exampleSentence: 'The slime mold found a solution to the maze faster than I expected.' },
    { word: 'navigate', definition: 'To find a path through something tricky', exampleSentence: 'I asked Ms. Reed how something without a brain can navigate.' },
    { word: 'surprisingly', definition: 'In a way that catches you off guard', exampleSentence: 'Surprisingly, it chose the shortest path every single time.' },
    { word: 'organize', definition: 'To arrange things in a clear, planned order', exampleSentence: 'My friend said it can organize itself like a living map.' },
    { word: 'efficient', definition: 'Getting good results without wasting time or effort', exampleSentence: 'Grandpa called that an efficient way to hunt for food.' },
  ],
  'essay-011': [
    { word: 'ancient', definition: 'Very, very old — from long ago', exampleSentence: 'The bread ovens in Pompeii are ancient, my history teacher said.' },
    { word: 'preserve', definition: 'To keep something from being destroyed over time', exampleSentence: 'Ash helped preserve the bakery for almost two thousand years.' },
    { word: 'discover', definition: 'To find something that was hidden or unknown', exampleSentence: 'Archaeologists discover loaves still marked with baker stamps.' },
    { word: 'tradition', definition: 'A custom passed down through many generations', exampleSentence: 'Grandma said baking bread is a tradition in almost every culture.' },
    { word: 'appreciate', definition: 'To value something and be thankful for it', exampleSentence: 'I appreciate that we can still see how Romans made their daily bread.' },
  ],
  'essay-012': [
    { word: 'communicate', definition: 'To share messages or information', exampleSentence: 'Whales communicate through songs that travel for miles underwater.' },
    { word: 'gradually', definition: 'Slowly, little by little over time', exampleSentence: 'The melody gradually changed over many years, Ms. Flynn explained.' },
    { word: 'significant', definition: 'Important and meaningful', exampleSentence: 'I told Grandpa that whale songs are significant to their culture.' },
    { word: 'culture', definition: 'Shared customs, beliefs, and ways of a group', exampleSentence: 'My friend said each pod has its own song culture.' },
    { word: 'extraordinary', definition: 'Very unusual and impressively special', exampleSentence: 'It is extraordinary that songs cross entire oceans.' },
  ],
  'essay-013': [
    { word: 'magnificent', definition: 'Extremely beautiful and impressive', exampleSentence: 'The cave ceiling looked magnificent, like a starry sky, I whispered to Mom.' },
    { word: 'observe', definition: 'To watch carefully and notice details', exampleSentence: 'Our guide told us to observe quietly so we would not disturb the glowworms.' },
    { word: 'mysterious', definition: 'Strange and hard to explain — full of wonder', exampleSentence: 'Grandpa said the glowing cave feels mysterious and peaceful.' },
    { word: 'glowing', definition: 'Giving off a soft light', exampleSentence: 'I told my teacher the worms stay glowing all year round.' },
    { word: 'explore', definition: 'To travel through a place to learn about it', exampleSentence: 'My friend wants to explore more caves after our field trip.' },
  ],
  'essay-014': [
    { word: 'regenerate', definition: 'To grow back something that was lost or damaged', exampleSentence: 'Axolotls can regenerate lost limbs, Ms. Huang told our class.' },
    { word: 'remarkable', definition: 'Worthy of attention — surprisingly impressive', exampleSentence: 'I told Grandpa that their healing power is remarkable.' },
    { word: 'investigate', definition: 'To study something closely to understand how it works', exampleSentence: 'Doctors investigate axolotls to learn how regeneration works.' },
    { word: 'eventually', definition: 'After some time has passed', exampleSentence: 'Eventually, a new tail grows back completely.' },
    { word: 'significant', definition: 'Important and meaningful', exampleSentence: 'My friend said this could be significant for medicine someday.' },
  ],
  'essay-015': [
    { word: 'colony', definition: 'A group of the same kind living and working together', exampleSentence: 'An ant colony can stretch across entire countries, I learned.' },
    { word: 'cooperate', definition: 'To work together toward the same goal', exampleSentence: 'Ms. Diaz said ants cooperate like teammates on a huge project.' },
    { word: 'enormous', definition: 'Extremely large — much bigger than normal', exampleSentence: 'I told Grandpa the supercolony is enormous — billions of ants.' },
    { word: 'organize', definition: 'To arrange people or tasks in a planned way', exampleSentence: 'They organize jobs so every ant has a role to play.' },
    { word: 'territory', definition: 'An area that a person or group controls or defends', exampleSentence: 'My friend said each colony defends its territory fiercely.' },
  ],
  'essay-016': [
    { word: 'memorize', definition: 'To learn something well enough to remember it', exampleSentence: 'I use a memory palace to memorize my spelling words, I told Ms. Walsh.' },
    { word: 'imagine', definition: 'To picture something in your mind', exampleSentence: 'Grandpa taught me to imagine each fact in a room of my house.' },
    { word: 'technique', definition: 'A special method or way of doing something', exampleSentence: 'My friend said this technique helps her remember speeches.' },
    { word: 'organize', definition: 'To put things in a clear, useful order', exampleSentence: 'I organize ideas by placing them on familiar shelves in my mind.' },
    { word: 'consider', definition: 'To think carefully about something before deciding', exampleSentence: 'My teacher asked me to consider using it for history dates too.' },
  ],
  'essay-017': [
    { word: 'gravity', definition: 'The force that pulls objects toward each other', exampleSentence: 'Gravity can bend starlight near a black hole, Mr. Santos explained.' },
    { word: 'theory', definition: 'An idea that explains how something works', exampleSentence: 'I told Grandpa Einstein\'s theory predicted this long before we saw it.' },
    { word: 'observe', definition: 'To watch carefully and gather information', exampleSentence: 'Astronomers observe how light curves around massive objects.' },
    { word: 'significant', definition: 'Very important and worth paying attention to', exampleSentence: 'My friend said this was a significant proof of general relativity.' },
    { word: 'fascinating', definition: 'Extremely interesting — makes you want to learn more', exampleSentence: 'I find it fascinating that space itself can act like a lens.' },
  ],
  'essay-018': [
    { word: 'trigger', definition: 'To cause something to start happening', exampleSentence: 'The flytrap needs two touches to trigger its snap, I explained.' },
    { word: 'precise', definition: 'Exact and accurate — not sloppy or vague', exampleSentence: 'Ms. Cole said the plant\'s timing is incredibly precise.' },
    { word: 'curious', definition: 'Wanting to know more about something', exampleSentence: 'I was curious why it counts to two before closing.' },
    { word: 'mechanism', definition: 'The parts and way something works', exampleSentence: 'Grandpa compared the trap\'s mechanism to a mousetrap spring.' },
    { word: 'patient', definition: 'Able to wait calmly without rushing', exampleSentence: 'The plant stays patient and waits for the right moment to snap.' },
  ],
  'essay-019': [
    { word: 'connect', definition: 'To join or link people, places, or ideas together', exampleSentence: 'Paper helped connect empires along the Silk Road, my teacher said.' },
    { word: 'trade', definition: 'To exchange goods with others', exampleSentence: 'Merchants used it to record trade across deserts and mountains.' },
    { word: 'significant', definition: 'Very important and worth remembering', exampleSentence: 'I told Grandpa that paper was a significant invention for the world.' },
    { word: 'spread', definition: 'To move or reach many people or places', exampleSentence: 'Ideas spread faster once writing traveled on lightweight paper.' },
    { word: 'invention', definition: 'Something new that someone created', exampleSentence: 'My friend called paper one of the greatest inventions ever.' },
  ],
  'essay-020': [
    { word: 'synchronize', definition: 'To happen at the exact same time', exampleSentence: 'All the corals synchronize their spawning on one moonlit night.' },
    { word: 'magnificent', definition: 'Extremely beautiful and impressive', exampleSentence: 'Grandpa said the reef looks magnificent when it turns into pink snow.' },
    { word: 'gradually', definition: 'Slowly, little by little over time', exampleSentence: 'The eggs gradually rise until the whole ocean shimmers.' },
    { word: 'ecosystem', definition: 'A community of living things and their environment', exampleSentence: 'Ms. Rivera explained how spawning keeps the whole ecosystem healthy.' },
    { word: 'fortunate', definition: 'Lucky — having good things happen', exampleSentence: 'I feel fortunate that we got to watch it on a school dive trip.' },
  ],
  'essay-021': [
    { word: 'predict', definition: 'To say what will happen before it does', exampleSentence: 'Some animals seem to predict earthquakes before people feel them.' },
    { word: 'behavior', definition: 'The way someone or something acts', exampleSentence: 'My teacher asked us to note any unusual animal behavior before a quake.' },
    { word: 'sensitive', definition: 'Easily affected by small changes', exampleSentence: 'Grandpa said dogs are sensitive to vibrations we cannot feel.' },
    { word: 'observe', definition: 'To watch carefully and notice details', exampleSentence: 'I observe how our cat hides under the bed before storms.' },
    { word: 'fortunately', definition: 'Luckily — it is a good thing that', exampleSentence: 'Fortunately, scientists study these signs to help keep people safe.' },
  ],
};

const EXPECTED = 21;
const ids = Object.keys(DAILY_WORDS);
if (ids.length !== EXPECTED) {
  console.error(`Expected ${EXPECTED} essays in DAILY_WORDS, got ${ids.length}`);
  process.exit(1);
}

let updated = 0;
const missing = [];

bank.forEach(essay => {
  const words = DAILY_WORDS[essay.id];
  if (!words) {
    missing.push(essay.id);
    return;
  }
  if (words.length !== 5) {
    console.error(`${essay.id}: expected 5 words, got ${words.length}`);
    process.exit(1);
  }
  essay.words = words;
  updated += 1;
});

if (missing.length) {
  console.error(`Missing DAILY_WORDS for: ${missing.join(', ')}`);
  process.exit(1);
}

fs.writeFileSync(BANK, JSON.stringify(bank, null, 2));
console.log(`Upgraded vocab for ${updated} essays (${updated * 5} daily-use words).`);

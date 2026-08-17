#!/usr/bin/env python3
"""Build essay-bank.json: merge existing essays 001-007 with new essays 008-021."""
import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
BANK_PATH = SCRIPT_DIR / "essay-bank.json"

GRAMMAR = [
    {"id": "past-perfect", "name": "Past Perfect (had + verb)"},
    {"id": "although", "name": "Although / Even though"},
    {"id": "em-dash", "name": "Em dashes for emphasis"},
]


def vw(word, definition):
    return (
        f'<span class="vocab-word" data-word="{word}" '
        f'title="{definition}">{word}</span>'
    )


NEW_ESSAYS = [
    {
        "id": "essay-008",
        "title": "The Eight-Armed Escape Artist",
        "topic": "Octopus Intelligence",
        "words": [
            {"word": "cephalopod", "definition": "A marine mollusk such as an octopus or squid with a large head and tentacles"},
            {"word": "cognition", "definition": "The mental process of acquiring knowledge through thought, experience, and senses"},
            {"word": "chromatophore", "definition": "A pigment cell that allows some animals to change color by expanding or contracting"},
            {"word": "dexterous", "definition": "Skillful and coordinated, especially with the hands or limbs"},
            {"word": "invertebrate", "definition": "An animal without a backbone, such as an octopus, insect, or jellyfish"},
        ],
        "grammarRules": GRAMMAR,
        "passageHtml": (
            "<p>In 2016, when keepers at the New Zealand National Aquarium had arrived one morning, their most famous resident—a common octopus named Inky—had vanished. "
            "Security cameras later showed he had squeezed through a gap in his tank lid, crossed the floor, and slid down a drainpipe fifty meters long to reach the open sea. "
            "Although the escape had looked like a cartoon caper, biologists had recognized something deeper: Inky had planned. He had tested the lid, remembered the drain's location, and timed his move when the building had been quiet. "
            "Even though octopuses had lived only two or three years, this "
            + vw("invertebrate", "An animal without a backbone, such as an octopus, insect, or jellyfish")
            + " had outsmarted a facility built to contain sharks.</p>"
            "<p>Octopuses belong to the "
            + vw("cephalopod", "A marine mollusk such as an octopus or squid with a large head and tentacles")
            + " family—soft-bodied hunters whose ancestors had discarded shells millions of years ago and replaced armor with brains. "
            "Roughly two-thirds of an octopus's neurons sit in its arms, not its head, so each tentacle had partly thought for itself while still coordinating with the whole animal. "
            "Researchers had watched octopuses unscrew jar lids from the inside, open childproof pill bottles, and navigate mazes they had learned yesterday. "
            "Although birds and mammals had usually claimed the spotlight in animal-intelligence studies, cephalopods had forced scientists to ask whether "
            + vw("cognition", "The mental process of acquiring knowledge through thought, experience, and senses")
            + " required a skeleton—or even a familiar brain layout.</p>"
            "<p>Their camouflage had been equally astonishing. Millions of "
            + vw("chromatophore", "A pigment cell that allows some animals to change color by expanding or contracting")
            + "s—tiny sacs of pigment beneath the skin—had expanded and contracted under neural control until the animal matched coral, sand, or a threatening predator's pattern in less than a second. "
            "Some species had rippled waves of color across their bodies during courtship, a display researchers had compared to living video screens. "
            "Even though the octopus had possessed no bones, its body had been "
            + vw("dexterous", "Skillful and coordinated, especially with the hands or limbs")
            + " enough to manipulate tools—coconut shells carried as portable shelters, rocks used to barricade den entrances. "
            "Divers had filmed veined octopuses stacking shells like stone walls before bedtime.</p>"
            "<p>Tool use had once been considered uniquely human, then extended to chimpanzees and crows. When Jennifer Mather and colleagues had documented octopuses collecting coconut halves, the definition of intelligence had widened again. "
            "Although an octopus brain had been shaped like a doughnut—wrapping around its esophagus—experiments had shown long-term memory, discrimination between individual humans, and playful behavior. "
            "One lab octopus had learned to squirt water at a researcher it disliked while staying polite to others. Even though the animal had never seen that person harm it, it had remembered a prior unpleasant handling session.</p>"
            "<p>Wild octopuses had also solved ecological puzzles. They had raided crab traps, entered them through the bait door, eaten the catch, and left the way they had come. "
            "Fishermen had cursed the losses until cameras had proved the thief was an armored ghost with no bones—only "
            + vw("cognition", "The mental process of acquiring knowledge through thought, experience, and senses")
            + " and patience. "
            "Although humans had built locks and alarms, the octopus had treated obstacles as puzzles worth tasting with suckers lined with chemoreceptors—each arm had literally smelled its way forward.</p>"
            "<p>Conservation had grown urgent as warming oceans had stressed reef habitats. Because octopuses had matured fast and died young, populations had bounced back quickly when protected—but trawling and pollution had still erased local giants like the giant Pacific octopus. "
            "Marine biologists had argued that respecting "
            + vw("cephalopod", "A marine mollusk such as an octopus or squid with a large head and tentacles")
            + " intelligence meant tighter welfare rules in labs and restaurants. "
            "Several countries had already tightened laws on boiling live animals without stunning.</p>"
            "<p>Next time you see a photo of an octopus changing color like a LED screen, remember Inky sliding toward freedom through a drain meant for rainwater. "
            "The animal had possessed no passport, no map, no thumbs—only eight "
            + vw("dexterous", "Skillful and coordinated, especially with the hands or limbs")
            + " arms, a doughnut brain, and a "
            + vw("chromatophore", "A pigment cell that allows some animals to change color by expanding or contracting")
            + " wardrobe. "
            "Although we had spent centuries calling spineless creatures simple, the octopus had rewritten the syllabus. "
            "Evolution had built a mind from slime and nerve—and it had escaped before breakfast.</p>"
        ),
        "questions": [
            {"id": "q1", "question": "How did Inky the octopus escape from the New Zealand aquarium?",
             "hint": "Think drainpipe and tank lid.",
             "answers": ["through a drainpipe", "squeezed through tank lid into drain", "crossed floor and slid down drainpipe to sea", "escaped via drainpipe to the ocean"],
             "explanation": "Inky squeezed through a gap in his tank lid, crossed the floor, and slid down a fifty-meter drainpipe to reach the open sea."},
            {"id": "q2", "question": "What are chromatophores and what do they allow octopuses to do?",
             "hint": "Pigment cells under the skin.",
             "answers": ["pigment cells for color change", "change color and camouflage", "expand and contract to match surroundings", "color-changing skin cells"],
             "explanation": "Chromatophores are pigment cells beneath the skin that expand and contract, letting octopuses change color and camouflage in under a second."},
            {"id": "q3", "question": "Why is it unusual that so many octopus neurons are in the arms?",
             "hint": "Arms partly think for themselves.",
             "answers": ["each arm partly thinks independently", "neurons in arms not just the brain", "tentacles process information locally", "distributed intelligence in limbs"],
             "explanation": "About two-thirds of an octopus's neurons are in its arms, so each tentacle can process information and act with partial independence while coordinating with the body."},
            {"id": "q4", "question": "What evidence showed octopuses use tools in the wild?",
             "hint": "Coconut shells and rocks.",
             "answers": ["coconut shell shelters", "carrying coconut halves", "stacking rocks to barricade dens", "using shells and rocks as tools"],
             "explanation": "Researchers documented octopuses carrying coconut shell halves as portable shelters and stacking rocks to barricade their dens—behaviors classified as tool use."},
            {"id": "q5", "question": "What does the passage suggest about cognition and backbones?",
             "hint": "Invertebrates can still be smart.",
             "answers": ["cognition doesn't require a backbone", "invertebrates can be intelligent", "no skeleton needed for complex thinking", "cephalopods challenge old assumptions"],
             "explanation": "Octopus intelligence shows that advanced cognition does not require a backbone or a familiar brain layout—challenging assumptions that only vertebrates think in complex ways."},
        ],
        "curiosityHooks": [
            "Grandpa, if two-thirds of an octopus brain is in its arms, do you think each arm has its own personality?",
            "Mom, could an octopus really open a childproof pill bottle—and should we childproof our snack jars from one?",
            "If Inky escaped through a drainpipe to the ocean, do you think he remembered the way back to visit his tank?",
        ],
        "shareMessage": (
            "Today's reading was about octopus intelligence! 🐙🧠\n\n"
            "Inky escaped a New Zealand aquarium by squeezing through his tank lid and sliding down a 50-meter drainpipe to the sea!\n\n"
            "Octopuses change color using chromatophores, use tools like coconut shells, and have most of their neurons in their arms. "
            "Scientists now know cognition doesn't require a backbone.\n\n"
            "Ask us how chromatophores work and why Inky's escape amazed biologists!"
        ),
    },
    {
        "id": "essay-009",
        "title": "The Compass Hidden in a Bird's Eye",
        "topic": "Quantum Bird Navigation",
        "words": [
            {"word": "magnetoreception", "definition": "The ability to detect Earth's magnetic field for orientation or navigation"},
            {"word": "cryptochrome", "definition": "A light-sensitive protein found in plants and animals that may react to magnetic fields"},
            {"word": "migratory", "definition": "Relating to seasonal movement from one region to another"},
            {"word": "entanglement", "definition": "A quantum physics phenomenon where paired particles remain linked across distance"},
            {"word": "orientation", "definition": "The ability to determine one's position or direction relative to surroundings"},
        ],
        "grammarRules": GRAMMAR,
        "passageHtml": (
            "<p>Every autumn, when frost had begun to silver the meadows of northern Europe, a small songbird called the European robin had vanished from garden feeders as if pulled by an invisible thread. "
            "Within weeks, the same individuals had appeared in olive groves along the Mediterranean—hundreds of miles south—without maps, without GPS, without parents to guide them. "
            "Ornithologists had tracked these "
            + vw("migratory", "Relating to seasonal movement from one region to another")
            + " routes for decades, yet one mystery had refused to fade: how did a creature weighing less than a deck of cards navigate across continents in darkness and storm?</p>"
            "<p>Scientists had long suspected birds could sense Earth's magnetic field—a sense called "
            + vw("magnetoreception", "The ability to detect Earth's magnetic field for orientation or navigation")
            + ". "
            "Experiments in the 1960s had shown caged robins attempted to hop in the correct seasonal direction even when they had never seen the sky outdoors. "
            "Although magnets placed beside cages had confused them, researchers had still lacked a mechanism. "
            "Even though iron filings in beaks had once been proposed, later studies had found no reliable magnetic mineral in most songbirds.</p>"
            "<p>The breakthrough had come from an unlikely marriage—biology and quantum physics. "
            "In the early 2000s, biophysicists had proposed that a protein called "
            + vw("cryptochrome", "A light-sensitive protein found in plants and animals that may react to magnetic fields")
            + " in a robin's retina might act as a living compass. "
            "When blue light struck the protein, electrons had jumped between linked molecules in a way physicists called radical pairs. "
            "Earth's magnetic field had subtly altered how those pairs evolved, creating a chemical signal the brain could read as "
            + vw("orientation", "The ability to determine one's position or direction relative to surroundings")
            + " data. "
            "Although the idea had sounded bizarre, lab tests had shown robins became disoriented under radio waves that should disturb quantum states—but not under other frequencies.</p>"
            "<p>Quantum "
            + vw("entanglement", "A quantum physics phenomenon where paired particles remain linked across distance")
            + "—spooky linked behavior between particles—had usually been discussed in particle colliders, not in feathers. "
            "Yet the radical-pair model had suggested birds might harness effects that had once seemed too fragile for warm, noisy living tissue. "
            "Even though skeptics had argued biological systems could not preserve quantum coherence, robin experiments had kept pointing toward the retina. "
            "Migratory warblers, finches, and geese had likely shared similar machinery, tuned by evolution across millions of years of night flights.</p>"
            "<p>Navigation had never relied on magnetism alone. Birds had also used the sun's arc, star patterns, landmarks, and even smells carried on wind. "
            "Young birds on their first journey had often traveled with experienced adults, learning routes that had been refined across generations. "
            "Although a single sense could fail beneath cloud or pollution, the combined toolkit had made "
            + vw("migratory", "Relating to seasonal movement from one region to another")
            + " flight remarkably reliable. "
            "Radar had recorded vast rivers of birds moving on clear nights—millions of beating hearts steering by rules humans had only begun to decode.</p>"
            "<p>Climate change had shifted timing and habitats, forcing some populations to arrive after peak food had passed. "
            "Light pollution had blurred star fields above cities, and electromagnetic noise from human devices had raised new questions about whether quantum compasses could still calibrate cleanly. "
            "Conservationists had urged darker skies along flyways because even though satellites now tracked flocks from space, each bird still had to find its own way on the wing.</p>"
            "<p>Next time you hear a robin in spring, consider what had happened in the months you had not seen it—a crossing of seas and mountains guided partly by light hitting "
            + vw("cryptochrome", "A light-sensitive protein found in plants and animals that may react to magnetic fields")
            + " molecules in the eye. "
            "Although we had invented compasses from lodestone and silicon, evolution had beat us to quantum "
            + vw("magnetoreception", "The ability to detect Earth's magnetic field for orientation or navigation")
            + " by ages. "
            "The robin had carried a map written in physics too strange for the birds themselves to name—and precise enough to bring them home.</p>"
        ),
        "questions": [
            {"id": "q1", "question": "What is magnetoreception in birds?",
             "hint": "Sensing Earth's magnetic field.",
             "answers": ["detecting Earth's magnetic field", "magnetic field sense for navigation", "ability to sense magnetism for orientation"],
             "explanation": "Magnetoreception is the ability to detect Earth's magnetic field, which birds use alongside other cues to navigate during migration."},
            {"id": "q2", "question": "What role might cryptochrome play in robin navigation?",
             "hint": "Light-sensitive protein in the retina.",
             "answers": ["quantum compass in the eye", "reacts to light and magnetic field", "creates chemical signals from radical pairs", "retina protein for orientation"],
             "explanation": "Cryptochrome in the retina may form radical pairs when hit by blue light; Earth's magnetic field alters their behavior, producing signals the brain interprets as directional information."},
            {"id": "q3", "question": "Why did radio waves of specific frequencies disorient robins in experiments?",
             "hint": "They disturb quantum states.",
             "answers": ["disrupt quantum radical pairs", "interfere with quantum compass", "disturb cryptochrome mechanism", "affect quantum navigation"],
             "explanation": "Researchers found robins lost orientation under radio waves expected to disrupt quantum radical-pair states, supporting the quantum compass hypothesis."},
            {"id": "q4", "question": "Besides magnetoreception, what other cues do migratory birds use?",
             "hint": "Sun, stars, landmarks, smells.",
             "answers": ["sun and stars", "landmarks and smells", "sun, stars, landmarks, and odors", "multiple navigation cues combined"],
             "explanation": "Birds combine magnetic sensing with the sun's position, star patterns, landmarks, wind-borne smells, and social learning from experienced flock members."},
            {"id": "q5", "question": "Why is quantum entanglement mentioned in a bird navigation essay?",
             "hint": "Radical pairs link quantum physics to biology.",
             "answers": ["radical pairs use quantum effects", "linked particles in compass model", "quantum physics in cryptochrome mechanism", "entanglement related to radical-pair theory"],
             "explanation": "The radical-pair model connects bird navigation to quantum phenomena like entanglement, suggesting living systems may exploit fragile quantum effects for orientation."},
        ],
        "curiosityHooks": [
            "Grandpa, do you think robins see a colorful magnetic field overlay on the world like a video game map?",
            "Mom, if our phones give off radio waves, could they confuse migrating birds flying over our house?",
            "Scientists put magnets next to bird cages and the birds got lost—should we hide our fridge magnets during migration season?",
        ],
        "shareMessage": (
            "Today's essay was about quantum bird navigation! 🐦🧭\n\n"
            "Migratory birds like robins may use a protein called cryptochrome in their eyes as a quantum compass, "
            "detecting Earth's magnetic field through radical-pair chemistry.\n\n"
            "Experiments show specific radio waves disorient them—supporting a quantum magnetoreception theory! "
            "They also navigate by sun, stars, landmarks, and smells.\n\n"
            "Ask us what cryptochrome is and why quantum entanglement matters to songbirds!"
        ),
    },
    {
        "id": "essay-010",
        "title": "The Brainless Navigator",
        "topic": "Slime Mold Solving Mazes",
        "words": [
            {"word": "protist", "definition": "A single-celled or simple multicellular organism that is neither plant, animal, nor fungus"},
            {"word": "amoeboid", "definition": "Having a shapeless, flowing form that moves by extending pseudopods"},
            {"word": "aggregation", "definition": "The gathering of separate parts into a cluster or mass"},
            {"word": "algorithm", "definition": "A step-by-step procedure for solving a problem or completing a task"},
            {"word": "decentralized", "definition": "Organized so that control or decision-making is spread across many parts rather than one center"},
        ],
        "grammarRules": GRAMMAR,
        "passageHtml": (
            "<p>In a laboratory at Hokkaido University, researchers had printed a maze on agar gel—the kind of puzzle children solve with pencils, except this one had been sized for a yellow blob the consistency of oatmeal. "
            "The blob was Physarum polycephalum, a slime mold, and it had no eyes, no neurons, no mouth in any familiar sense. "
            "Food pellets had been placed at the maze's entrance and exit. "
            "Within hours, the organism had sent exploratory threads through every corridor, then retracted dead ends until a single efficient path had connected the snacks. "
            "Although the creature had possessed no brain, it had solved the maze faster than some undergraduate volunteers had managed on paper.</p>"
            "<p>Slime molds are "
            + vw("protist", "A single-celled or simple multicellular organism that is neither plant, animal, nor fungus")
            + "s—life forms that had puzzled taxonomists for centuries. "
            "Most of their life cycle, a single cell called a plasmodium had crawled in an "
            + vw("amoeboid", "Having a shapeless, flowing form that moves by extending pseudopods")
            + " fashion, extending pseudopods and streaming cytoplasm toward food or moisture. "
            "When conditions had turned harsh, thousands of individual cells had undergone "
            + vw("aggregation", "The gathering of separate parts into a cluster or mass")
            + ", fusing into a mobile slug that could crawl toward light before sprouting spore-bearing stalks. "
            "Even though the word mold had suggested fungus, the behavior had looked more like cooperative social protest than rotting bread.</p>"
            "<p>Tokyo rail planners had noticed something odd when they had mapped Physarum's growth between oat flakes arranged like stations around Tokyo. "
            "The mold's network had closely resembled the real subway layout—efficient, redundant where needed, minimal where possible. "
            "Computer scientists had compared the pattern to the shortest-path "
            + vw("algorithm", "A step-by-step procedure for solving a problem or completing a task")
            + " Dijkstra had invented decades earlier. "
            "Although no programmer had written code into the cell membrane, the slime had approximated optimal routing through simple local rules: extend toward food, retreat from dead ends, strengthen successful tubes.</p>"
            "<p>That "
            + vw("decentralized", "Organized so that control or decision-making is spread across many parts rather than one center")
            + " strategy had fascinated engineers designing robot swarms and wireless networks. "
            "Each filament had reacted only to chemical gradients nearby—no central command had shouted orders. "
            "Yet the whole plasmodium had behaved as if it had planned globally. "
            "Biophysicists had measured electrical pulses rippling through the network, suggesting communication without synapses. "
            "Even though textbooks had defined intelligence as requiring neurons, slime molds had forced a rewrite.</p>"
            "<p>Experiments had grown stranger. Physarum had learned to ignore harmless stimuli while avoiding harmful ones—a primitive habituation memory that had persisted for days. "
            "It had navigated bridges between disconnected platforms, choosing narrower spans when wide ones had carried simulated predator signals. "
            "Although the mechanism had remained debated, cytoskeletal rearrangement and externalized memory in slime trails had both been implicated. "
            "The creature had literally left notes in its own mucus.</p>"
            "<p>Medical researchers had even deployed slime molds to model blood vessel growth toward tumors, because both systems had solved similar transport problems under constraint. "
            "Although no hospital had yet prescribed Physarum, the "
            + vw("protist", "A single-celled or simple multicellular organism that is neither plant, animal, nor fungus")
            + " had become a living computer cheaper than silicon for certain optimization puzzles.</p>"
            "<p>Next time you feel stuck on a maze worksheet, remember the yellow smear that had beaten you without a cortex—streaming, retracting, committing to the shortest path like a commuter who had never bought a ticket. "
            "Evolution had written an "
            + vw("algorithm", "A step-by-step procedure for solving a problem or completing a task")
            + " in protoplasm, "
            + vw("decentralized", "Organized so that control or decision-making is spread across many parts rather than one center")
            + " and patient. "
            "Although we had crowned brains kings of problem-solving, the maze had belonged to the "
            + vw("amoeboid", "Having a shapeless, flowing form that moves by extending pseudopods")
            + " blob that had finished lunch first.</p>"
        ),
        "questions": [
            {"id": "q1", "question": "How did Physarum polycephalum solve the laboratory maze?",
             "hint": "It explored then retracted dead ends.",
             "answers": ["explored all paths then kept shortest route", "sent threads through corridors and retracted dead ends", "connected food pellets with efficient path", "trial and error then single optimal path"],
             "explanation": "The slime mold extended through all maze corridors, then withdrew from dead ends until only the shortest path between food pellets remained."},
            {"id": "q2", "question": "What surprised scientists about the Tokyo subway experiment?",
             "hint": "Oat flakes represented stations.",
             "answers": ["mold network matched real subway layout", "similar to Tokyo rail network", "efficient network like subway design", "resembled actual subway map"],
             "explanation": "When oat flakes were placed like Tokyo train stations, Physarum's connecting network closely resembled the efficient layout of the real subway system."},
            {"id": "q3", "question": "What does decentralized mean in the context of slime mold behavior?",
             "hint": "No central brain gives orders.",
             "answers": ["no central control", "decisions spread across filaments", "local rules without central command", "many parts act independently but coordinate"],
             "explanation": "Slime mold uses decentralized control—each filament responds to local chemical cues without a central brain, yet the whole organism finds efficient global solutions."},
            {"id": "q4", "question": "Why are slime molds classified as protists rather than fungi?",
             "hint": "They are neither plant, animal, nor fungus.",
             "answers": ["not truly fungi", "protist kingdom not fungus", "single-celled amoeboid organism", "different from fungal molds"],
             "explanation": "Slime molds like Physarum are protists—neither plants, animals, nor true fungi—often living as amoeboid plasmodia that aggregate under stress."},
            {"id": "q5", "question": "What evidence suggests slime molds can learn or remember?",
             "hint": "Habituation and slime trails.",
             "answers": ["habituation to harmless stimuli", "avoid harmful stimuli for days", "memory in slime trails", "learned to ignore safe signals"],
             "explanation": "Physarum shows habituation—learning to ignore repeated harmless stimuli while avoiding harmful ones—and may store information in external slime trails."},
        ],
        "curiosityHooks": [
            "Grandma, could a blob with no brain really design a subway map better than city planners?",
            "Dad, if slime mold leaves memory in its mucus trail, is that like writing notes on the sidewalk?",
            "Scientists use slime mold to study tumor blood vessels—should we call it Dr. Oatmeal?",
        ],
        "shareMessage": (
            "Today's reading was about slime mold solving mazes! 🟡🧩\n\n"
            "Physarum polycephalum has no brain but finds the shortest path through mazes by exploring and retracting dead ends. "
            "It even mimicked Tokyo's subway when oat flakes marked stations!\n\n"
            "Its decentralized algorithm inspires robot swarms and network design. "
            "It can learn through habituation and may remember via slime trails.\n\n"
            "Ask us what a protist is and how a brainless blob outsmarted a puzzle!"
        ),
    },
    {
        "id": "essay-011",
        "title": "Bread Rises from the Ashes",
        "topic": "Pompeii Bread Ovens",
        "words": [
            {"word": "thermopolium", "definition": "An ancient Roman street-side food counter where hot food and drinks were sold"},
            {"word": "carbonized", "definition": "Turned into carbon; preserved by charring rather than decay"},
            {"word": "pumice", "definition": "Light volcanic rock full of air bubbles, formed during explosive eruptions"},
            {"word": "artisan", "definition": "A skilled craftsperson who makes things by hand using traditional methods"},
            {"word": "fermentation", "definition": "The chemical breakdown of substances by yeast or bacteria, often producing gas that makes dough rise"},
        ],
        "grammarRules": GRAMMAR,
        "passageHtml": (
            "<p>When Mount Vesuvius had erupted in 79 CE, ash and "
            + vw("pumice", "Light volcanic rock full of air bubbles, formed during explosive eruptions")
            + " had buried Pompeii so quickly that some residents had died mid-step. "
            "Yet in the ruins, archaeologists had later found something oddly domestic: loaves of bread still sitting in ovens, still round, still scored with baker's marks as if the next customer had been seconds away. "
            "Although the city had become a grave, its kitchens had frozen like photographs—preserved not by intent but by catastrophe.</p>"
            "<p>Roman Pompeii had been crowded with "
            + vw("thermopolium", "An ancient Roman street-side food counter where hot food and drinks were sold")
            + "s—colorful counters where workers had grabbed hot stews, wine, and snacks without cooking at home. "
            "Painted menus had advertised lentils, fish sauce, and roasted nuts. "
            "Behind many counters, brick ovens had glowed from dawn until the streets had emptied. "
            "Even though apartment dwellers had lacked kitchens, the thermopolium had functioned like a fast-food lane with frescoed walls.</p>"
            "<p>Bread had been central to Roman life—so central that bakers had formed guilds and politicians had distributed free loaves to win votes. "
            "An "
            + vw("artisan", "A skilled craftsperson who makes things by hand using traditional methods")
            + " baker had mixed flour, water, and starter culture, then kneaded dough until gluten had formed elastic strands. "
            + vw("Fermentation", "The chemical breakdown of substances by yeast or bacteria, often producing gas that makes dough rise")
            + " had filled the dough with bubbles; steam and heat in the oven had set the crumb into airy architecture. "
            "Although modern yeast packets had not existed, sourdough cultures had been passed between families for generations.</p>"
            "<p>The eruption had "
            + vw("carbonized", "Turned into carbon; preserved by charring rather than decay")
            + " organic matter in an instant—bread, wooden shelves, even figs in a jar had turned to charcoal shells holding shape. "
            "One famous loaf from the House of the Baker had borne a stamp reading property of Celer, slave of Q. Granius Verus—ownership pressed into crust. "
            "Researchers had used CT scans to peek inside without crumbling the loaf, revealing air pockets frozen mid-rise. "
            "Even though two millennia had passed, the geometry of Roman baking had remained readable.</p>"
            "<p>Ovens themselves had been engineering marvels. Thick domes had stored heat from fires built on the floor, which had later been swept aside so dough could bake on hot tiles. "
            "Bakers had rotated loaves with long paddles; ashes had been vented through flues. "
            "Although Pompeii's ovens had varied in size, the workflow had matched bakeries across the empire—from North Africa to Britain. "
            "When Vesuvius had roared, many fires had still been warm.</p>"
            "<p>Modern bakers had attempted recipes from "
            + vw("carbonized", "Turned into carbon; preserved by charring rather than decay")
            + " crumbs and written sources. "
            "They had discovered Roman bread had often been denser than baguettes, sometimes spiced with bay leaf or fennel, sometimes sweetened with grape must. "
            "Experimental archaeologists had rebuilt "
            + vw("thermopolium", "An ancient Roman street-side food counter where hot food and drinks were sold")
            + " counters at living-history sites, serving passersby flatbread cooked in replica furnaces. "
            "Although no recipe had survived verbatim from the doomed city, the ovens had told their own story in brick and ash.</p>"
            "<p>Walk Pompeii today and you can still step into a baker's shop where the millstones had stopped turning mid-grind. "
            "The "
            + vw("artisan", "A skilled craftsperson who makes things by hand using traditional methods")
            + " who had shaped those loaves had expected tomorrow's sales, not volcanic burial. "
            "Although tragedy had preserved the scene, it had also interrupted ordinary hunger—the simplest human rhythm. "
            "Next time you smell fresh bread, remember Pompeii's ovens: "
            + vw("fermentation", "The chemical breakdown of substances by yeast or bacteria, often producing gas that makes dough rise")
            + " paused forever, meals waiting for customers who had never returned.</p>"
        ),
        "questions": [
            {"id": "q1", "question": "What is a thermopolium in ancient Pompeii?",
             "hint": "Street-side food counter.",
             "answers": ["Roman street food counter", "hot food and drink shop", "ancient fast-food counter", "street-side snack bar"],
             "explanation": "A thermopolium was a Roman street-side counter where workers bought hot food and drinks, often equipped with brick ovens behind the serving area."},
            {"id": "q2", "question": "How did the Vesuvius eruption preserve bread loaves?",
             "hint": "Heat and ash carbonized organic matter.",
             "answers": ["carbonized them", "charred and preserved shape", "turned bread to carbon shells", "instant carbonization from heat and ash"],
             "explanation": "The eruption's intense heat and ash carbonized organic materials, charring bread and other items while preserving their shapes like charcoal shells."},
            {"id": "q3", "question": "What did CT scans reveal about carbonized Pompeii bread?",
             "hint": "Air pockets inside the loaf.",
             "answers": ["air pockets frozen mid-rise", "internal bubble structure", "crumb structure preserved", "fermentation bubbles visible inside"],
             "explanation": "CT scans of carbonized loaves revealed internal air pockets frozen during rising, showing Roman bread's texture without destroying the artifact."},
            {"id": "q4", "question": "Why was bread politically important in Roman cities?",
             "hint": "Free loaves and baker guilds.",
             "answers": ["free bread for votes", "bakers guilds and political distribution", "politicians gave loaves for support", "central to Roman civic life"],
             "explanation": "Bread was so essential that bakers formed guilds and politicians distributed free loaves to win public support, making baking central to urban life."},
            {"id": "q5", "question": "How did Roman bakers heat their ovens before baking bread?",
             "hint": "Fire on the floor, then swept away.",
             "answers": ["fire on oven floor then swept out", "heated dome with fire then baked on tiles", "stored heat in thick dome", "burned fuel inside then removed ashes"],
             "explanation": "Roman ovens used fires built on the floor to heat thick domed walls; ashes were swept aside before dough was baked on the hot tiles."},
        ],
        "curiosityHooks": [
            "Grandma, archaeologists found bread still in the oven from the day Vesuvius erupted—would you try a recipe recreated from 2,000-year-old crumbs?",
            "Mom, Roman fast-food shops had painted menus like ours—what do you think was their version of a combo meal?",
            "The baker stamped 'property of Celer, slave of...' on loaves—who do you think really made the bread?",
        ],
        "shareMessage": (
            "Today's essay was about Pompeii bread ovens! 🍞🌋\n\n"
            "When Vesuvius buried Pompeii in 79 CE, thermopolia (Roman street food counters) froze mid-service. "
            "Bread loaves carbonized in ovens—still round with baker's marks!\n\n"
            "CT scans reveal air pockets from fermentation frozen mid-rise. "
            "Roman bakers used sourdough, thick domed ovens, and stamped ownership on crusts.\n\n"
            "Ask us what a thermopolium is and how volcanic ash preserved ancient lunch!"
        ),
    },
    {
        "id": "essay-012",
        "title": "Songs That Cross Oceans",
        "topic": "Whale Song Culture",
        "words": [
            {"word": "cetacean", "definition": "A marine mammal such as a whale, dolphin, or porpoise"},
            {"word": "dialect", "definition": "A regional or group-specific form of language or communication"},
            {"word": "acoustic", "definition": "Relating to sound or the sense of hearing"},
            {"word": "pod", "definition": "A social group of whales or dolphins that travel and feed together"},
            {"word": "repertoire", "definition": "The full set of songs, calls, or performances an individual or group can produce"},
        ],
        "grammarRules": GRAMMAR,
        "passageHtml": (
            "<p>In 1970, when bioacoustician Roger Payne had first played humpback whale recordings for audiences, listeners had wept. "
            "The sounds had risen and fallen like slow jazz—moans, chirps, glissandos spanning octaves no human singer could sustain underwater. "
            "Although sailors had heard whale calls for centuries, scientists had dismissed them as random noise until Payne had shown structure, repetition, and change across seasons. "
            "Even though the ocean had seemed silent from shore, humpbacks had been broadcasting culture.</p>"
            "<p>Whales are "
            + vw("cetacean", "A marine mammal such as a whale, dolphin, or porpoise")
            + "s—mammals that had returned to the sea and evolved "
            + vw("acoustic", "Relating to sound or the sense of hearing")
            + " superpowers. "
            "Sound had traveled four times faster in water than air and had carried for hundreds of miles along deep channels. "
            "Each humpback "
            + vw("pod", "A social group of whales or dolphins that travel and feed together")
            + " had shared feeding grounds, migration routes, and—remarkably—songs that had shifted year to year like pop charts. "
            "Males had sung long suites during breeding season, sometimes for hours without pause. "
            "Although the songs had clearly mattered for mating, the exact message had remained partly mysterious—advertising fitness, coordinating groups, or echo-mapping coastlines had all been proposed. "
            "What had stunned researchers was cultural transmission: when one population had invented a new phrase, neighboring groups had often adopted it until an old "
            + vw("repertoire", "The full set of songs, calls, or performances an individual or group can produce")
            + " had been replaced entirely within a decade. "
            "Even though whales had no written scores, they had rewritten hits faster than some human towns had changed radio playlists.</p>"
            "<p>Distinct "
            + vw("dialect", "A regional or group-specific form of language or communication")
            + "s had mapped onto geography. "
            "Pacific humpbacks had sounded unlike Atlantic ones; pods off Australia had carried phrases unknown near Hawaii until a revolutionary song had swept eastward like a trend. "
            "Biologists had tracked the spread using hydrophones—underwater microphones anchored to the seafloor. "
            "Although genetics had shown whales were related across oceans, their "
            + vw("acoustic", "Relating to sound or the sense of hearing")
            + " identities had been learned, not inherited.</p>"
            "<p>Other "
            + vw("cetacean", "A marine mammal such as a whale, dolphin, or porpoise")
            + "s had displayed vocal culture too. "
            "Orca pods had passed unique call sets across generations—family accents so stable that researchers had identified clans by ear alone. "
            "Sperm whales had clicked in codas, rhythmic patterns that had differed between clans like Morse code accents. "
            "Although dolphins had whistled signature names for themselves, humpbacks had composed the ocean's longest mixtapes.</p>"
            "<p>Human noise had threatened these channels. "
            "Shipping engines, naval sonar, and seismic surveys had cluttered the frequencies whales had used for song and navigation. "
            "When COVID-19 had briefly slowed global shipping in 2020, scientists had recorded quieter seas and stress hormones dropping in some "
            + vw("cetacean", "A marine mammal such as a whale, dolphin, or porpoise")
            + " populations. "
            "Even though regulations had begun limiting speed near breeding grounds, the underwater soundscape had never returned to the silence whales had known a century ago.</p>"
            "<p>Next time you hear a whale recording, remember it had not been a solo—it had been one voice in a "
            + vw("pod", "A social group of whales or dolphins that travel and feed together")
            + " learning a "
            + vw("dialect", "A regional or group-specific form of language or communication")
            + " that had changed every season. "
            "Although we had mapped continents with satellites, whales had mapped belonging with sound. "
            "Their "
            + vw("repertoire", "The full set of songs, calls, or performances an individual or group can produce")
            + " had been memory, identity, and invitation rolled into one long note beneath the waves.</p>"
        ),
        "questions": [
            {"id": "q1", "question": "What did Roger Payne demonstrate about humpback whale sounds in 1970?",
             "hint": "Not random noise—structured songs.",
             "answers": ["structured repeatable songs", "whale sounds have patterns", "songs change across seasons", "not random but organized vocalizations"],
             "explanation": "Roger Payne showed humpback vocalizations were structured, repeating songs that changed across seasons—not random noise as previously assumed."},
            {"id": "q2", "question": "How do whale songs spread between populations?",
             "hint": "New phrases adopted like trends.",
             "answers": ["cultural transmission", "neighboring groups adopt new phrases", "songs spread like trends", "learned not inherited"],
             "explanation": "Whale populations culturally transmit songs—when one group invents new phrases, neighbors often adopt them until entire repertoires are replaced within years."},
            {"id": "q3", "question": "What is a whale dialect in this passage?",
             "hint": "Regional differences in song.",
             "answers": ["regional song differences", "group-specific vocal patterns", "geographic variation in whale songs", "unique phrases per region"],
             "explanation": "Whale dialects are region-specific vocal patterns—Pacific humpbacks sound different from Atlantic ones, with distinct phrases tied to geography."},
            {"id": "q4", "question": "Why is sound especially important for cetaceans underwater?",
             "hint": "Travels far and fast in water.",
             "answers": ["sound travels far underwater", "acoustic communication over long distances", "faster and farther than in air", "hundreds of miles through water"],
             "explanation": "Sound travels about four times faster in water than air and can carry hundreds of miles along deep channels, making acoustic communication essential for cetaceans."},
            {"id": "q5", "question": "What happened to ocean noise during the 2020 shipping slowdown?",
             "hint": "Quieter seas, less stress.",
             "answers": ["seas got quieter", "lower stress hormones in whales", "reduced shipping noise", "quieter oceans during COVID slowdown"],
             "explanation": "When global shipping slowed during COVID-19, scientists recorded quieter oceans and decreased stress hormones in some whale populations."},
        ],
        "curiosityHooks": [
            "Grandpa, humpback whales rewrite their hit songs every few years—do you think they're copying each other like TikTok trends?",
            "Mom, orca families have accents passed down like our family recipes—can you hear the difference on a recording?",
            "When the oceans got quieter during COVID, whales relaxed—should ships slow down near whale highways?",
        ],
        "shareMessage": (
            "Today's reading was about whale song culture! 🐋🎵\n\n"
            "Humpback whales sing structured songs that change like pop charts, spreading new phrases between pods across oceans. "
            "Roger Payne's 1970 recordings proved they weren't random noise.\n\n"
            "Different regions have dialects; orcas and sperm whales pass vocal traditions too. "
            "Quieter seas during COVID lowered whale stress!\n\n"
            "Ask us what a cetacean repertoire is and how whale songs travel like trends!"
        ),
    },
    {
        "id": "essay-013",
        "title": "Stars on the Cave Ceiling",
        "topic": "Bioluminescent Caves",
        "words": [
            {"word": "subterranean", "definition": "Existing, occurring, or found below the surface of the earth"},
            {"word": "speleological", "definition": "Relating to the scientific study of caves and cave systems"},
            {"word": "guano", "definition": "Accumulated droppings of seabirds or bats, often rich in nutrients"},
            {"word": "phototrophic", "definition": "Capable of using light as an energy source for growth"},
            {"word": "troglodytic", "definition": "Adapted to living in caves or underground environments"},
        ],
        "grammarRules": GRAMMAR,
        "passageHtml": (
            "<p>When explorer Floyd Collins had crawled into Kentucky limestone in the 1920s, he had carried lanterns—not because he had expected treasure, but because darkness there had been absolute. "
            "Yet in caves halfway around the world, from New Zealand to Vietnam, visitors today had witnessed something that had looked like bottled galaxies: thousands of blue-green points hanging from ceilings, drifting on threads, pulsing softly as if breathing. "
            "Although these were not stars, they had fooled the eye with the same quiet wonder.</p>"
            "<p>Waitomo Cave on New Zealand's North Island had become famous for "
            + vw("subterranean", "Existing, occurring, or found below the surface of the earth")
            + " glowworm displays. "
            "The worms—actually larval fungus gnats—had spun silk snares beaded with sticky droplets and had lit their tails with biochemical light to lure flying insects into traps. "
            "Tour boats had drifted beneath constellations reflected in underground rivers while guides had spoken in whispers so as not to disturb hunting. "
            "Even though the scene had looked magical, it had been predation dressed as astronomy.</p>"
            "<p>Other glowing caves had hosted "
            + vw("phototrophic", "Capable of using light as an energy source for growth")
            + " bacteria on walls fed by minerals in dripping water. "
            + vw("Speleological", "Relating to the scientific study of caves and cave systems")
            + " teams had mapped chambers where microbial mats had shone faintly green, powered not by sun but by chemical energy in the rock. "
            "Although life without daylight had once seemed impossible, "
            + vw("troglodytic", "Adapted to living in caves or underground environments")
            + " ecosystems had proved otherwise—bats, blind fish, pale crayfish, and fungi all threading a food web in perpetual twilight.</p>"
            "<p>Bat colonies had often anchored these systems. "
            "Centuries of "
            + vw("guano", "Accumulated droppings of seabirds or bats, often rich in nutrients")
            + " had piled on cave floors, feeding insects and fungi that had in turn fed other cave dwellers. "
            "When tourists had first entered some chambers with torches, sensitive glowworm colonies had blinked out—disturbed by light, air currents, or carbon dioxide from breath. "
            "Although guides had switched to red-filtered lamps, conservationists had still debated how many visitors a fragile ceiling could tolerate.</p>"
            "<p>Photographers had struggled to capture the glow without flash that would harm larvae. "
            "Long exposures had turned underground streams into mirrors doubling the illusion of sky. "
            "Scientists had measured light output per worm and had found it remarkably efficient—cold radiance evolved to attract prey, not heat the cave. "
            "Even though engineers had copied firefly chemistry for sensors, glowworms had perfected lure design without patents.</p>"
            "<p>Climate change and land use had threatened water tables that had fed these caves. "
            "Pollution from agriculture had altered drip chemistry; drought had slowed the growth of stalactites that had taken millennia to form. "
            "Although "
            + vw("speleological", "Relating to the scientific study of caves and cave systems")
            + " surveys had documented new chambers with remote robots, many glowworm populations had remained vulnerable to a single season of wrong humidity.</p>"
            "<p>Next time you flip off a bedroom light, imagine a boat gliding under a "
            + vw("subterranean", "Existing, occurring, or found below the surface of the earth")
            + " firmament woven from silk and "
            + vw("guano", "Accumulated droppings of seabirds or bats, often rich in nutrients")
            + "-fed insects—each point a "
            + vw("troglodytic", "Adapted to living in caves or underground environments")
            + " hunter advertising dinner in photons. "
            "Although the cave had never seen sunrise, it had invented its own night sky—and had kept it burning since before the first human had thought to strike flint.</p>"
        ),
        "questions": [
            {"id": "q1", "question": "What creates the glowing display in New Zealand's Waitomo Cave?",
             "hint": "Larvae, not stars.",
             "answers": ["glowworm larvae", "fungus gnat larvae", "glowworms with bioluminescent tails", "larval fungus gnats"],
             "explanation": "Waitomo's glowworms are larval fungus gnats that produce bioluminescent light at their tails to lure insects into sticky silk snares."},
            {"id": "q2", "question": "Why is guano important in cave ecosystems?",
             "hint": "Bat droppings feed other life.",
             "answers": ["nutrient source on cave floor", "feeds insects and fungi", "bat droppings support food web", "accumulated droppings nourish cave life"],
             "explanation": "Guano from bat colonies piles on cave floors, providing nutrients that support insects, fungi, and other organisms in the underground food web."},
            {"id": "q3", "question": "What does troglodytic mean for cave organisms?",
             "hint": "Adapted to underground life.",
             "answers": ["adapted to cave life", "living underground", "cave-adapted species", "suited to dark cave environments"],
             "explanation": "Troglodytic describes organisms adapted to cave or underground environments—often with specialized traits for darkness, humidity, and limited food."},
            {"id": "q4", "question": "Why do tour guides limit light and noise in glowworm caves?",
             "hint": "Disturbance harms larvae.",
             "answers": ["protect glowworm colonies", "light and CO2 disturb larvae", "avoid disrupting hunting", "sensitive to torchlight and breath"],
             "explanation": "Bright light, air currents, and carbon dioxide from tourists can disturb or harm glowworm larvae, so guides use dim red-filtered lamps and quiet voices."},
            {"id": "q5", "question": "How can bacteria glow in caves without sunlight?",
             "hint": "Phototrophic from chemical energy.",
             "answers": ["phototrophic bacteria on walls", "chemical energy from minerals", "minerals in dripping water", "microbial mats using chemical light energy"],
             "explanation": "Some cave bacteria are phototrophic in a broader ecological sense, using energy from minerals in dripping water rather than sunlight to grow on cave walls."},
        ],
        "curiosityHooks": [
            "Grandma, glowworm caves look like riding a boat under the Milky Way—would you go if the ceiling is made of hungry larvae?",
            "Mom, if bat poop feeds the whole cave food web, who do you think is the real landlord—the bats or the glowworms?",
            "Tour guides whisper so they don't scare the worms—do you think the cave notices when we visit?",
        ],
        "shareMessage": (
            "Today's essay was about bioluminescent caves! ✨🦇\n\n"
            "Waitomo Cave in New Zealand glows with fungus gnat larvae that use tail-light to lure prey into silk traps—like stars made of hunters!\n\n"
            "Bat guano feeds underground ecosystems; speleologists study troglodytic life adapted to eternal dark. "
            "Tourist lights can harm fragile glowworm colonies.\n\n"
            "Ask us what guano is and why cave ceilings look like galaxies!"
        ),
    },
    {
        "id": "essay-014",
        "title": "The Salamander That Rewrites Its Body",
        "topic": "Axolotl Regeneration",
        "words": [
            {"word": "neotenic", "definition": "Retaining juvenile features into adulthood, such as gills in an axolotl"},
            {"word": "blastema", "definition": "A mass of cells capable of developing into missing organs or limbs"},
            {"word": "amphibian", "definition": "A cold-blooded vertebrate such as a frog or salamander that often lives both in water and on land"},
            {"word": "regenerative", "definition": "Having the ability to regrow lost or damaged tissue"},
            {"word": "salamander", "definition": "A tailed amphibian with a long body and short legs, often found near water"},
        ],
        "grammarRules": GRAMMAR,
        "passageHtml": (
            "<p>In the ancient canals of Xochimilco near Mexico City, a creature with a permanent smile and feathery gills had paddled through water lettuce as if time had forgotten to ask it to grow up. "
            "The axolotl—an "
            + vw("amphibian", "A cold-blooded vertebrate such as a frog or salamander that often lives both in water and on land")
            + " that had remained "
            + vw("neotenic", "Retaining juvenile features into adulthood, such as gills in an axolotl")
            + "—had kept its larval gills and aquatic lifestyle throughout adulthood while cousins had crawled onto land and transformed. "
            "Although Aztec legends had linked the animal to the god Xolotl, modern biologists had valued it for a different miracle: when an axolotl had lost a leg, the leg had come back.</p>"
            "<p>Regeneration had baffled surgeons for centuries. "
            "Humans had scarred where salamanders had rebuilt. "
            "If a researcher had amputated an axolotl limb at the wrist, cells near the cut had dedifferentiated—shed their specialized identities—and gathered into a "
            + vw("blastema", "A mass of cells capable of developing into missing organs or limbs")
            + ", a blob of potential that had known exactly which bones, nerves, and claws had been missing. "
            "Within weeks, a perfect replacement had grown—joints, digits, and all. "
            "Even though mammals had limited "
            + vw("regenerative", "Having the ability to regrow lost or damaged tissue")
            + " capacity in liver and skin, axolotls had treated major injury like a software update.</p>"
            "<p>Heart tissue, spinal cord segments, even parts of the brain had regenerated in experiments. "
            "Scientists had mapped genes that had switched on after wounding— pathways that had stayed silent in mice and humans. "
            "Although cancer risk often rose when cells had proliferated wildly, axolotls had somehow balanced growth with control. "
            "One theory had suggested their "
            + vw("neotenic", "Retaining juvenile features into adulthood, such as gills in an axolotl")
            + " state had preserved youthful healing programs other "
            + vw("salamander", "A tailed amphibian with a long body and short legs, often found near water")
            + "s had shut off at metamorphosis.</p>"
            "<p>Wild axolotls had neared extinction as Mexico City had expanded. "
            "Pollution, invasive fish, and drained wetlands had shrunk their native range to a handful of channels. "
            "Conservationists had bred captive colonies in labs worldwide—not only to save the species but because the "
            + vw("regenerative", "Having the ability to regrow lost or damaged tissue")
            + " secrets had might one day help burn victims or amputees. "
            "Even though pet trade demand had spread pink and white morphs across aquariums, the drabber wild type had remained genetically precious.</p>"
            "<p>Medical teams had tested axolotl-inspired therapies—drugs that had nudged human cells toward "
            + vw("blastema", "A mass of cells capable of developing into missing organs or limbs")
            + "-like behavior, scaffolds seeded with stem cells, immune tweaks to reduce scarring. "
            "Although no clinic had yet grown a human arm from scratch, toe tips in children had hinted that our ancestors had once carried more repair code than adults had used. "
            "The axolotl had simply kept the full manual open.</p>"
            "<p>Next time you see a photo of an axolotl with frilly gills, remember what those gills had hidden—a "
            + vw("salamander", "A tailed amphibian with a long body and short legs, often found near water")
            + " that had refused land but had mastered reassembly. "
            "Although we had learned to transplant organs from donors, the axolotl had carried its spare parts inside every wound. "
            "Evolution had written "
            + vw("regenerative", "Having the ability to regrow lost or damaged tissue")
            + " instructions in a smiling "
            + vw("amphibian", "A cold-blooded vertebrate such as a frog or salamander that often lives both in water and on land")
            + "—and had left scientists racing to read them before the canals had gone quiet forever.</p>"
        ),
        "questions": [
            {"id": "q1", "question": "What does neotenic mean for axolotls?",
             "hint": "They keep juvenile features as adults.",
             "answers": ["keep juvenile features in adulthood", "retain larval gills as adults", "never fully metamorphose", "adult with juvenile traits"],
             "explanation": "Neotenic axolotls retain juvenile features like external gills and an aquatic lifestyle into adulthood instead of metamorphosing into land-dwelling salamanders."},
            {"id": "q2", "question": "What is a blastema in limb regeneration?",
             "hint": "Mass of cells at the wound site.",
             "answers": ["mass of cells that regrows limb", "regenerative cell cluster", "dedifferentiated cells at cut", "blob that rebuilds missing parts"],
             "explanation": "A blastema is a mass of dedifferentiated cells at an amputation site that reorganizes and develops into the missing limb structures."},
            {"id": "q3", "question": "Why are wild axolotls endangered?",
             "hint": "Pollution, invasive fish, habitat loss.",
             "answers": ["pollution and habitat loss", "Mexico City expansion", "invasive fish and drained wetlands", "shrunken native range"],
             "explanation": "Wild axolotls have nearly vanished from their native Xochimilco canals due to pollution, invasive predators, and wetland drainage from urban expansion."},
            {"id": "q4", "question": "What body parts besides limbs can axolotls regenerate?",
             "hint": "Heart, spine, brain parts.",
             "answers": ["heart and spinal cord", "brain tissue", "heart, spinal cord, brain parts", "multiple organs and tissues"],
             "explanation": "Axolotls can regenerate not only limbs but also heart tissue, spinal cord segments, and parts of the brain in laboratory studies."},
            {"id": "q5", "question": "Why do scientists study axolotls for human medicine?",
             "hint": "Regenerative genes and minimal scarring.",
             "answers": ["learn regeneration for human healing", "genes for regrowing tissue", "reduce scarring and regrow limbs", "medical applications for amputees and burns"],
             "explanation": "Researchers study axolotl regeneration to discover genetic pathways that could help humans regrow tissue, reduce scarring, and someday improve treatments for amputees and burn victims."},
        ],
        "curiosityHooks": [
            "Grandpa, axolotls can regrow parts of their brain—do you think that means they forget what hurt them?",
            "Mom, if scientists crack axolotl regeneration, would you want a bandage that grows a new finger?",
            "Aztecs named the axolotl after a god—do you think they knew it could grow its leg back?",
        ],
        "shareMessage": (
            "Today's reading was about axolotl regeneration! 🦎✨\n\n"
            "Neotenic axolotls keep gills as adults and regrow limbs, hearts, spinal cords, even brain parts via blastema cell clusters!\n\n"
            "Wild populations in Mexico City canals are endangered, but lab studies may help human healing someday. "
            "They scar less and rebuild perfectly.\n\n"
            "Ask us what a blastema is and why axolotls never grow up onto land!"
        ),
    },
    {
        "id": "essay-015",
        "title": "One Colony to Rule Them All",
        "topic": "Ant Supercolonies",
        "words": [
            {"word": "pheromone", "definition": "A chemical signal released by an animal that affects others of its species"},
            {"word": "unicolonial", "definition": "Forming a single cooperative colony that spans vast areas without territorial conflict"},
            {"word": "invasive", "definition": "Spreading aggressively into new environments and disrupting native species"},
            {"word": "superorganism", "definition": "A group of organisms behaving as a coordinated whole, like ants in a colony"},
            {"word": "territorial", "definition": "Defending a defined area against others of the same species"},
        ],
        "grammarRules": GRAMMAR,
        "passageHtml": (
            "<p>When entomologist Luc Passera had sampled Argentine ants along the Mediterranean coast in the 1990s, he had expected fierce border wars—the usual "
            + vw("territorial", "Defending a defined area against others of the same species")
            + " skirmishes that had kept ant colonies separate for millennia. "
            "Instead, nests separated by hundreds of miles had accepted each other's workers as family. "
            "Although the ants had belonged to different hills, they had behaved like one empire without internal borders—a "
            + vw("unicolonial", "Forming a single cooperative colony that spans vast areas without territorial conflict")
            + " network stretching from Italy to Portugal.</p>"
            "<p>Most ant colonies had recognized nestmates by smell—cuticular hydrocarbons, "
            + vw("pheromone", "A chemical signal released by an animal that affects others of its species")
            + "-like signatures learned at birth. "
            "Outsiders had been attacked on sight. "
            "Argentine ants introduced to new continents by human shipping had carried unusually uniform scents, as if every worker had worn the same ID badge. "
            "Even though native ants had struggled with local diseases and predators, the invaders had cooperated across landscapes the size of small countries.</p>"
            "<p>Scientists had dubbed the largest examples "
            + vw("superorganism", "A group of organisms behaving as a coordinated whole, like ants in a colony")
            + "s—collectives where individuals had sacrificed reproduction to queens while sharing food, brood, and defense like cells in a body. "
            "A "
            + vw("superorganism", "A group of organisms behaving as a coordinated whole, like ants in a colony")
            + " in southern Japan had spanned tens of millions of nests. "
            "Workers had marched in trails visible from satellite imagery, overwhelming crickets, caterpillars, and native ant species. "
            "Although each ant had possessed a brain smaller than a pinhead, the swarm had outcompeted specialists through sheer coordinated mass.</p>"
            "<p>The Argentine ant had become a textbook "
            + vw("invasive", "Spreading aggressively into new environments and disrupting native species")
            + " species—riding cargo and potted plants to California, Hawaii, Australia, and South Africa. "
            "Where supercolonies had formed, biodiversity had often dropped. "
            "Ground-nesting birds had lost insect prey; native ants that had dispersed seeds had vanished. "
            "Even though pesticides had temporarily thinned trails, survivors had rebound unless entire regions had been treated simultaneously—a nearly impossible task once the "
            + vw("unicolonial", "Forming a single cooperative colony that spans vast areas without territorial conflict")
            + " web had spread.</p>"
            "<p>Researchers had experimented with disruption—introducing rival scents, spreading pathogens specific to the invader, or encouraging native predators. "
            "Some success had come from bait stations laced with slow-acting toxins carried back to nests by foragers. "
            "Although eradication had proved rare at supercolony scale, localized control had protected parks and farms. "
            "Evolutionary biologists had also asked whether such vast cooperation could collapse from its own success—mutations that had favored selfish cheating had occasionally appeared in lab colonies.</p>"
            "<p>Next time you see a thin ant trail crossing a sidewalk, consider whether those workers had belonged to a hill—or to a continent-spanning "
            + vw("superorganism", "A group of organisms behaving as a coordinated whole, like ants in a colony")
            + " that had rewritten the rules of "
            + vw("territorial", "Defending a defined area against others of the same species")
            + " life. "
            "Although we had built nations with flags and passports, Argentine ants had built one with "
            + vw("pheromone", "A chemical signal released by an animal that affects others of its species")
            + "s alone—and had marched farther than many armies had ever dreamed.</p>"
        ),
        "questions": [
            {"id": "q1", "question": "What makes Argentine ant supercolonies unicolonial?",
             "hint": "Nests accept distant workers as nestmates.",
             "answers": ["no fighting between distant nests", "cooperate across vast areas", "accept workers from miles away", "single colony without borders"],
             "explanation": "Unicolonial Argentine ant networks treat workers from nests hundreds of miles apart as nestmates, cooperating without the territorial wars typical of ant species."},
            {"id": "q2", "question": "How do ants usually recognize nestmates versus intruders?",
             "hint": "Chemical smell signatures.",
             "answers": ["cuticular hydrocarbons", "chemical scent signatures", "pheromone-like smells", "learned colony odors"],
             "explanation": "Ants recognize nestmates by cuticular hydrocarbon scents learned at birth; outsiders with different chemical profiles are typically attacked."},
            {"id": "q3", "question": "Why are supercolony ants considered a superorganism?",
             "hint": "Many individuals act as one coordinated body.",
             "answers": ["coordinated like one organism", "colony behaves as a whole", "shared resources and defense", "individuals act as parts of one unit"],
             "explanation": "Supercolony ants function as a superorganism—millions of individuals sharing brood, food, and defense so the collective behaves like a single coordinated entity."},
            {"id": "q4", "question": "How did Argentine ants spread to new continents?",
             "hint": "Human shipping and potted plants.",
             "answers": ["human shipping", "cargo and potted plants", "accidental transport by people", "introduced via trade"],
             "explanation": "Argentine ants spread invasively to new continents by hitchhiking in cargo, soil, and potted plants transported through global shipping networks."},
            {"id": "q5", "question": "What ecological damage do invasive ant supercolonies cause?",
             "hint": "Native species lose food and habitat.",
             "answers": ["reduce biodiversity", "displace native ants", "harm ground-nesting birds", "outcompete native species"],
             "explanation": "Invasive supercolonies outcompete native ants and insects, reducing biodiversity and disrupting ecosystems including seed dispersal and bird food sources."},
        ],
        "curiosityHooks": [
            "Grandpa, one ant supercolony in Japan has millions of nests—do you think they know they're part of something huge?",
            "Mom, if ants recognize family by smell, could we trick an invader colony with the wrong perfume?",
            "Argentine ants ride in potted plants—should we check our garden store purchases like customs agents?",
        ],
        "shareMessage": (
            "Today's essay was about ant supercolonies! 🐜🌍\n\n"
            "Argentine ants form unicolonial networks where distant nests cooperate without fighting—some span continents! "
            "They recognize nestmates by pheromone-like scent signatures.\n\n"
            "These invasive superorganisms outcompete native species and disrupt ecosystems. "
            "Scientists struggle to control them because treating one nest isn't enough.\n\n"
            "Ask us what unicolonial means and why one ant empire covers Japan!"
        ),
    },
    {
        "id": "essay-016",
        "title": "Palaces Built Inside the Mind",
        "topic": "Memory Palace Technique History",
        "words": [
            {"word": "mnemonic", "definition": "A device such as a pattern of letters or images that aids memory"},
            {"word": "loci", "definition": "Latin for 'places'; in memory techniques, familiar locations where information is stored mentally"},
            {"word": "rhetoric", "definition": "The art of effective or persuasive speaking and writing"},
            {"word": "orator", "definition": "A skilled public speaker, especially one who addresses formal audiences"},
            {"word": "visualization", "definition": "The practice of forming clear mental images to represent ideas or information"},
        ],
        "grammarRules": GRAMMAR,
        "passageHtml": (
            "<p>Before printing presses had existed, a Roman lawyer standing in the Forum had been expected to recite hours of testimony without notes—names, dates, statutes, precedents flowing like water from memory alone. "
            "How had anyone done it? "
            "Cicero, one of Rome's greatest "
            + vw("orator", "A skilled public speaker, especially one who addresses formal audiences")
            + "s, had described a trick still taught to memory champions today: the method of "
            + vw("loci", "Latin for 'places'; in memory techniques, familiar locations where information is stored mentally")
            + ", building a palace inside the mind.</p>"
            "<p>The technique had likely originated with Greek poets who had competed in oral epic performance. "
            "Simonides of Ceos, legend had claimed, had survived a banquet roof collapse and had identified victims by remembering where each guest had sat—discovering that spatial memory had been extraordinarily sticky. "
            "Although words alone had faded quickly, places had lingered. "
            "Students of "
            + vw("rhetoric", "The art of effective or persuasive speaking and writing")
            + " had begun placing images of ideas along familiar routes— the forum's statues, a childhood home's rooms—so recalling a walk had retrieved speeches in order.</p>"
            "<p>A "
            + vw("mnemonic", "A device such as a pattern of letters or images that aids memory")
            + " palace had worked because brains had evolved to navigate geography, not spreadsheets. "
            "You had chosen a building you had known intimately and had assigned vivid, even absurd, images to each corner—a red elephant juggling laws in the hallway, a laughing judge on the stairs. "
            "During delivery, the "
            + vw("orator", "A skilled public speaker, especially one who addresses formal audiences")
            + " had mentally strolled the route, collecting images like packages. "
            "Even though the images had been invented, the "
            + vw("loci", "Latin for 'places'; in memory techniques, familiar locations where information is stored mentally")
            + " had been real enough to anchor them.</p>"
            "<p>Medieval monks had adapted the method to memorize scripture; Renaissance humanists had taught it alongside Latin grammar. "
            "Giordano Bruno had wandered Europe claiming fantastical memory systems tied to astrology—some had admired his "
            + vw("visualization", "The practice of forming clear mental images to represent ideas or information")
            + " skills, others had feared them as sorcery. "
            "Although the Church had eventually burned Bruno for other heresies, his memory treatises had survived to intrigue modern psychologists.</p>"
            "<p>Brain scans in the twenty-first century had shown memory athletes using spatial networks in the hippocampus while memorizing shuffled decks of cards. "
            "They had not been born different—they had trained "
            + vw("mnemonic", "A device such as a pattern of letters or images that aids memory")
            + " palaces for months until recall had looked like magic. "
            "Even though smartphones had outsourced names and numbers, competitive memorizers had proved ancient "
            + vw("rhetoric", "The art of effective or persuasive speaking and writing")
            + " tools had still worked on modern brains.</p>"
            "<p>Students today had applied the method to anatomy, languages, and history timelines—any ordered list that had benefited from a walk through an imagined house. "
            "Teachers had encouraged exaggerated "
            + vw("visualization", "The practice of forming clear mental images to represent ideas or information")
            + " because dull images had slipped away; violent or humorous scenes had stuck. "
            "Although the palace had existed only in mind, its rooms had been as navigable as any street the learner had walked since childhood.</p>"
            "<p>Next time you forget where you put your keys, remember Cicero pacing mental marble halls—each statue a speech, each doorway a chapter. "
            "Although empires had fallen and libraries had burned, the method of "
            + vw("loci", "Latin for 'places'; in memory techniques, familiar locations where information is stored mentally")
            + " had outlasted them all. "
            "The cheapest palace had required no stone—only "
            + vw("visualization", "The practice of forming clear mental images to represent ideas or information")
            + ", patience, and a route you had already known by heart.</p>"
        ),
        "questions": [
            {"id": "q1", "question": "What is the method of loci?",
             "hint": "Memory palace using familiar places.",
             "answers": ["memory palace technique", "storing info in familiar locations", "mental walk through known places", "placing images along a route"],
             "explanation": "The method of loci (memory palace) places vivid mental images along familiar locations so walking the route in imagination retrieves information in order."},
            {"id": "q2", "question": "What story is told about Simonides and the origin of spatial memory techniques?",
             "hint": "Banquet collapse and seating positions.",
             "answers": ["identified bodies by seat location", "banquet roof collapse", "remembered where guests sat", "spatial memory after collapse"],
             "explanation": "Legend says Simonides identified banquet victims by remembering where each guest had sat, revealing how strongly spatial memory anchors recall."},
            {"id": "q3", "question": "Why does the memory palace technique use vivid or absurd images?",
             "hint": "Dull images are forgotten.",
             "answers": ["memorable images stick", "absurd scenes are easier to recall", "vivid images don't fade", "humorous or violent scenes last"],
             "explanation": "Memory palaces use exaggerated, humorous, or bizarre images because vivid scenes are far easier to recall than dull, generic ones."},
            {"id": "q4", "question": "Who was Cicero in the context of this passage?",
             "hint": "Roman orator who described the technique.",
             "answers": ["Roman orator", "famous Roman speaker", "lawyer who used memory palaces", "orator who described method of loci"],
             "explanation": "Cicero was a renowned Roman orator and lawyer who described using the method of loci to memorize long legal speeches without written notes."},
            {"id": "q5", "question": "What did modern brain scans show about memory athletes?",
             "hint": "They use spatial brain networks.",
             "answers": ["hippocampus spatial networks active", "use same loci technique", "trained mnemonic palaces", "spatial memory areas engaged"],
             "explanation": "Brain scans show memory athletes activate spatial navigation networks in the hippocampus when memorizing, confirming they use trained mnemonic palace techniques."},
        ],
        "curiosityHooks": [
            "Grandma, Roman lawyers memorized entire trials by walking through imaginary houses—want us to build a memory palace for your grocery list?",
            "Mom, memory champions memorize decks of cards using rooms in their mind—could you walk through our kitchen and 'see' your speech notes?",
            "They burned Giordano Bruno but kept his memory books—do you think remembering everything is a superpower or a curse?",
        ],
        "shareMessage": (
            "Today's reading was about memory palace history! 🏛️🧠\n\n"
            "Ancient Greek and Roman orators used the method of loci—placing vivid images in familiar mental rooms to memorize hours of speech.\n\n"
            "Legend says Simonides invented it after a banquet collapse. Cicero used it in Roman courts; modern memory athletes still train the same way!\n\n"
            "Ask us what a mnemonic palace is and why absurd images stick better!"
        ),
    },
    {
        "id": "essay-017",
        "title": "When Gravity Bends Starlight",
        "topic": "Black Hole Light Bending",
        "words": [
            {"word": "gravitational", "definition": "Relating to the force of attraction between masses, such as gravity"},
            {"word": "lensing", "definition": "The bending and focusing of light by massive objects' gravity"},
            {"word": "singularity", "definition": "A point where density becomes infinite, as theorized at the center of a black hole"},
            {"word": "relativistic", "definition": "Relating to Einstein's theory describing space, time, and gravity at extreme speeds or masses"},
            {"word": "curvature", "definition": "The degree to which space or a surface is bent or deviates from flatness"},
        ],
        "grammarRules": GRAMMAR,
        "passageHtml": (
            "<p>In May 1919, when astronomer Arthur Eddington had photographed a solar eclipse from the island of Príncipe, he had not been chasing darkness for its own sake. "
            "He had tested a prediction so strange that newspapers had later announced: light itself could weigh. "
            "Stars near the hidden sun had appeared shifted from their expected positions—as if the sun's mass had dented the sky and forced starlight to slide along the dent. "
            "Although Newton's gravity had pulled objects, Einstein's newer theory had described space itself bending.</p>"
            "<p>Einstein's general relativity had proposed that mass and energy had curved spacetime like a mattress under a bowling ball. "
            "Planets had rolled along those curves as if pulled by gravity, but light—despite having no rest mass—had still followed the shortest path through bent geometry. "
            "The effect was called "
            + vw("gravitational", "Relating to the force of attraction between masses, such as gravity")
            + " "
            + vw("lensing", "The bending and focusing of light by massive objects' gravity")
            + ". "
            "Even though starlight had seemed straight for everyday life, a "
            + vw("relativistic", "Relating to Einstein's theory describing space, time, and gravity at extreme speeds or masses")
            + " correction had been required near massive bodies.</p>"
            "<p>Black holes had pushed the idea to extremes. "
            "When a massive star had collapsed at the end of its life, "
            + vw("curvature", "The degree to which space or a surface is bent or deviates from flatness")
            + " near the remnant had grown so steep that not even light could climb out. "
            "The boundary— the event horizon—had marked the point of no return. "
            "Inside, theory had predicted a "
            + vw("singularity", "A point where density becomes infinite, as theorized at the center of a black hole")
            + " where known physics had broken down. "
            "Although no human had visited such a place, mathematics had drawn the portrait in equations.</p>"
            "<p>Telescopes had later seen "
            + vw("gravitational", "Relating to the force of attraction between masses, such as gravity")
            + " "
            + vw("lensing", "The bending and focusing of light by massive objects' gravity")
            + " everywhere. "
            "Galaxy clusters had acted like cosmic magnifying glasses, stretching background galaxies into arcs and rings—Einstein rings when alignment had been perfect. "
            "Astronomers had used these natural telescopes to study galaxies too faint to see otherwise. "
            "Even though the clusters had been invisible in ordinary light, their mass—mostly dark matter—had betrayed them through bent starlight.</p>"
            "<p>In 2019, the Event Horizon Telescope collaboration had released the first image of a black hole's shadow in galaxy M87—a glowing doughnut of gas swirling around darkness. "
            "The ring's size had matched "
            + vw("relativistic", "Relating to Einstein's theory describing space, time, and gravity at extreme speeds or masses")
            + " predictions; the dark center had been where light had fallen inward forever. "
            "Although the image had looked simple, it had confirmed decades of theory born from eclipse plates and chalkboards.</p>"
            "<p>Closer home, GPS satellites had needed relativistic clock corrections—gravity had slowed time slightly in orbit compared to Earth's surface. "
            "Without Einstein's math, your phone's map had drifted by miles daily. "
            "Although black holes had seemed exotic, "
            + vw("curvature", "The degree to which space or a surface is bent or deviates from flatness")
            + " had touched everyday technology.</p>"
            "<p>Next time you see a photo of a black hole's ring, remember Eddington's eclipse—proof that space had been malleable and starlight had obeyed hidden geometry. "
            "Although the "
            + vw("singularity", "A point where density becomes infinite, as theorized at the center of a black hole")
            + " remained a mystery, the bending of light had been real enough to weigh worlds. "
            "Gravity had not merely pulled—it had sculpted the paths photons had traveled since the universe had first turned on its lamps.</p>"
        ),
        "questions": [
            {"id": "q1", "question": "What did Eddington's 1919 eclipse experiment demonstrate?",
             "hint": "Star positions shifted near the sun.",
             "answers": ["light bends around the sun", "gravitational lensing of starlight", "Einstein's prediction confirmed", "star positions shifted by gravity"],
             "explanation": "During the 1919 solar eclipse, Eddington measured star positions near the sun and found light bent due to gravity, confirming Einstein's general relativity prediction."},
            {"id": "q2", "question": "What is gravitational lensing?",
             "hint": "Mass bends light like a lens.",
             "answers": ["gravity bends light", "massive objects focus starlight", "light follows curved spacetime", "bending of light by gravity"],
             "explanation": "Gravitational lensing is the bending and focusing of light when it passes near massive objects whose gravity curves spacetime."},
            {"id": "q3", "question": "What is a singularity in black hole theory?",
             "hint": "Center where physics breaks down.",
             "answers": ["infinite density point", "center of black hole", "where physics breaks down", "theoretical infinite density"],
             "explanation": "A singularity is the theorized point at a black hole's center where density becomes infinite and known physical laws no longer apply."},
            {"id": "q4", "question": "How do galaxy clusters act as natural telescopes?",
             "hint": "They magnify background galaxies.",
             "answers": ["gravitational lensing magnifies", "bend light from distant galaxies", "Einstein rings", "mass magnifies background objects"],
             "explanation": "Massive galaxy clusters gravitationally lens background galaxies, stretching them into arcs and rings that magnify otherwise too-faint objects for study."},
            {"id": "q5", "question": "Why does GPS need relativistic corrections?",
             "hint": "Gravity affects time in orbit.",
             "answers": ["gravity slows clocks differently", "relativistic time differences", "orbital clocks run differently", "Einstein's math needed for accuracy"],
             "explanation": "GPS satellites experience slightly different gravitational time dilation than receivers on Earth; without relativistic corrections, navigation would drift by miles daily."},
        ],
        "curiosityHooks": [
            "Grandpa, starlight bends around the sun like it's sliding on a curved slide—does that mean space is actually dented?",
            "Mom, if black holes eat light, how did we take a picture of one in 2019?",
            "GPS needs Einstein's math or our maps drift miles—should we thank relativity for pizza delivery?",
        ],
        "shareMessage": (
            "Today's essay was about black hole light bending! 🕳️✨\n\n"
            "Eddington's 1919 eclipse proved starlight bends around the sun—confirming Einstein's gravitational lensing. "
            "Black holes curve spacetime so steeply light can't escape!\n\n"
            "Galaxy clusters magnify distant galaxies; the 2019 Event Horizon Telescope imaged a black hole's shadow. "
            "Even GPS needs relativistic corrections.\n\n"
            "Ask us what a singularity is and why light has weight!"
        ),
    },
    {
        "id": "essay-018",
        "title": "The Plant That Counts to Two",
        "topic": "Venus Flytrap Mechanics",
        "words": [
            {"word": "carnivorous", "definition": "Feeding on animal flesh or insects rather than only plants"},
            {"word": "turgor", "definition": "The pressure of fluid inside plant cells that keeps tissue firm and upright"},
            {"word": "predatory", "definition": "Capturing and eating other organisms for food"},
            {"word": "mechanistic", "definition": "Based on predictable physical mechanisms rather than conscious decisions"},
            {"word": "oscillation", "definition": "A repeated back-and-forth movement or fluctuation"},
        ],
        "grammarRules": GRAMMAR,
        "passageHtml": (
            "<p>In the boggy coastal plains of North and South Carolina, a plant with toothy jaws had waited without muscles, without nerves, without anything resembling a brain—yet it had caught more flies than many spiders nearby. "
            "The Venus flytrap, Dionaea muscipula, had fascinated Charles Darwin so deeply that he had called it one of the most wonderful plants in the world. "
            "Although it had looked like a green mouth, its hunting had followed rules as precise as clockwork.</p>"
            "<p>Each trap had been a modified leaf split into two lobes lined with stiff trigger hairs. "
            "When an insect had brushed one hair, nothing had happened—the plant had demanded proof. "
            "A second touch within about twenty seconds had fired the snap. "
            "Although a single false alarm—raindrop or debris—had been ignored, confirmed prey had triggered a "
            + vw("mechanistic", "Based on predictable physical mechanisms rather than conscious decisions")
            + " closure taking roughly a tenth of a second, faster than you could blink.</p>"
            "<p>How had soft leaves moved so fast? "
            "Researchers had discovered a hydraulic trick. "
            "Cells in the outer lobes had been inflated with water—high "
            + vw("turgor", "The pressure of fluid inside plant cells that keeps tissue firm and upright")
            + " pressure keeping them curved outward like a spring. "
            "When triggers had confirmed a meal, ion channels had flashed signals and water had rushed between cells, flipping curvature inward. "
            "The trap had not flexed muscles; it had released stored geometry. "
            "Even though the motion had resembled biting, it had been physics all the way down.</p>"
            "<p>Once closed, the plant had sealed edges with interlocking teeth and had secreted digestive enzymes—true "
            + vw("carnivorous", "Feeding on animal flesh or insects rather than only plants")
            + " behavior in a photosynthesizer. "
            "Nitrogen and phosphorus from bugs had supplemented poor sandy soil. "
            "If the prisoner had been too small and had escaped through gaps, the trap had reopened within a day, wasting little energy. "
            "Although "
            + vw("predatory", "Capturing and eating other organisms for food")
            + " plants had evolved independently several times worldwide, Venus flytraps had narrowed their range to a shrinking ribbon of habitat.</p>"
            "<p>Scientists had also recorded slow "
            + vw("oscillation", "A repeated back-and-forth movement or fluctuation")
            + "s—traps had subtly pulsed between open states, possibly testing thresholds or redistributing water before strikes. "
            "Electrophysiologists had measured action-potential-like spikes in trigger hairs, blurring the line between plant signaling and animal nerves without neurons present. "
            "Even though the flytrap had not counted in words, it had counted in touches—two, then lunch.</p>"
            "<p>Poachers and habitat loss had threatened wild populations; most sold in shops had been cultivated, not dug from bogs. "
            "Gardeners had learned to feed them distilled water—minerals in tap water had burned roots evolved for rain-fresh wetlands. "
            "Although a windowsill flytrap had seemed like a toy, it had embodied millions of years of "
            + vw("predatory", "Capturing and eating other organisms for food")
            + " refinement.</p>"
            "<p>Next time you tickle a trigger hair, remember the plant had been waiting for a second knock like a cautious landlord. "
            "Although it had lacked a mind, its "
            + vw("turgor", "The pressure of fluid inside plant cells that keeps tissue firm and upright")
            + "-powered jaws had solved a problem soil could not—turning flies into fertilizer with "
            + vw("mechanistic", "Based on predictable physical mechanisms rather than conscious decisions")
            + " grace. "
            "The bog's green mouth had counted to two since long before calculators had existed.</p>"
        ),
        "questions": [
            {"id": "q1", "question": "How many trigger hair touches does a Venus flytrap require before snapping shut?",
             "hint": "One touch is not enough.",
             "answers": ["two touches", "two within about twenty seconds", "second touch within 20 seconds", "two trigger hair contacts"],
             "explanation": "A Venus flytrap requires two trigger hair touches within roughly twenty seconds to confirm prey and avoid false alarms from raindrops or debris."},
            {"id": "q2", "question": "What role does turgor pressure play in the trap's snap?",
             "hint": "Water pressure in cells.",
             "answers": ["hydraulic pressure drives closure", "water pressure in cells", "turgor keeps lobes curved then releases", "fluid pressure flips trap shape"],
             "explanation": "High turgor pressure in outer lobe cells keeps traps curved open; when triggered, rapid water movement changes cell pressure, flipping the lobes shut."},
            {"id": "q3", "question": "Why is the Venus flytrap classified as carnivorous?",
             "hint": "It digests insects for nutrients.",
             "answers": ["digests insects", "captures and eats bugs", "secretes enzymes on prey", "gets nitrogen from insects"],
             "explanation": "Venus flytraps capture insects, seal them in modified leaves, and secrete digestive enzymes to absorb nitrogen and phosphorus from prey."},
            {"id": "q4", "question": "What happens if prey is too small for the closed trap?",
             "hint": "Trap reopens quickly.",
             "answers": ["trap reopens within a day", "reopens if prey escapes", "doesn't waste energy digesting", "opens again if meal too small"],
             "explanation": "If captured prey is too small and escapes, the trap reopens within about a day rather than wasting energy on digestion."},
            {"id": "q5", "question": "Why do scientists describe the flytrap's behavior as mechanistic?",
             "hint": "Physical rules, not conscious decisions.",
             "answers": ["follows physical mechanisms", "predictable hydraulic response", "no brain needed", "touch-count triggers physical snap"],
             "explanation": "Flytrap closure follows mechanistic physical processes—trigger hair signals and turgor changes—rather than conscious decision-making."},
        ],
        "curiosityHooks": [
            "Grandma, the Venus flytrap waits for TWO touches before it snaps—do you think it's smarter than our doorbell camera?",
            "Mom, the plant moves by water pressure, not muscles—could we build robots that snap shut the same way?",
            "Darwin called it the most wonderful plant—want to try tickling one trigger hair and waiting for nothing to happen?",
        ],
        "shareMessage": (
            "Today's reading was about Venus flytrap mechanics! 🪴🪰\n\n"
            "Flytraps require TWO trigger hair touches within ~20 seconds before snapping shut in 0.1 seconds—using turgor pressure, not muscles!\n\n"
            "This carnivorous plant digests insects for nutrients poor soil lacks. "
            "Scientists study its mechanistic oscillations and electrical-like signals.\n\n"
            "Ask us why one touch isn't enough and how a plant counts to two!"
        ),
    },
    {
        "id": "essay-019",
        "title": "Paper That Connected Empires",
        "topic": "Silk Road Paper",
        "words": [
            {"word": "papermaking", "definition": "The process of producing paper from plant fibers mixed with water and pressed flat"},
            {"word": "pulp", "definition": "A soft mass of fibers beaten from plants or rags, used to make paper"},
            {"word": "mulberry", "definition": "A tree whose inner bark has long been used as a fiber source for fine paper"},
            {"word": "manuscript", "definition": "A document or book written by hand rather than printed"},
            {"word": "dissemination", "definition": "The spreading of something widely among people or places"},
        ],
        "grammarRules": GRAMMAR,
        "passageHtml": (
            "<p>In a Han dynasty court around 105 CE, official Cai Lun had presented the emperor with sheets unlike anything scribes had used before—not brittle bamboo strips tied with string, not costly silk scrolls, but thin, flexible pages made from plant fibers mashed and dried. "
            "Although legend had credited Cai Lun with inventing paper, archaeologists had later found rougher sheets centuries older in Chinese tombs. "
            "What had mattered was the revolution: knowledge could now travel lighter than bronze and cheaper than silk.</p>"
            "<p>Early "
            + vw("papermaking", "The process of producing paper from plant fibers mixed with water and pressed flat")
            + " had begun by soaking bark, hemp, and rags until fibers had separated into "
            + vw("pulp", "A soft mass of fibers beaten from plants or rags, used to make paper")
            + ". "
            "Workers had beaten the mass flat, poured it onto screens, and pressed water out until sheets had formed. "
            "The craft had remained secret within China for centuries while scribes had copied poetry, tax records, and medical texts onto stacks that had fit in a saddlebag. "
            "Even though stone and clay had preserved words for millennia, paper had made duplication fast.</p>"
            "<p>When papermaking had leaked along the Silk Road—likely after a battle near Samarkand where Chinese papermakers had been captured— the technology had spread west like a quiet wildfire. "
            "By the eighth century, mills in Baghdad had refined formulas; "
            + vw("mulberry", "A tree whose inner bark has long been used as a fiber source for fine paper")
            + " bark had become prized for smooth sheets favored by scholars. "
            "Although merchants had traded spices and gems openly, the "
            + vw("dissemination", "The spreading of something widely among people or places")
            + " of paper had carried ideas farther than any single caravan of goods.</p>"
            "<p>Islamic libraries had bloomed with copied "
            + vw("manuscript", "A document or book written by hand rather than printed")
            + "s—astronomy, algebra, medicine—because paper had been affordable enough for wide circulation. "
            "When the craft had reached medieval Europe through Spain and Sicily, it had collided with parchment made from animal skins. "
            "Paper had won on price; parchment had lingered for luxury charters. "
            "Even though Gutenberg's press had later multiplied paper's power, the Silk Road had planted the seed centuries earlier.</p>"
            "<p>Paper had changed more than books. "
            "Governments had issued paper currency in China long before European banks had tried the experiment. "
            "Ship logs, star charts, and maps had multiplied explorations because navigators had no longer carved every update in wood. "
            "Although fire had remained paper's enemy—libraries had burned—copies had often survived elsewhere, a resilience scrolls had struggled to match when unique.</p>"
            "<p>Modern historians had traced paper trails through fibers and watermarks, identifying when a "
            + vw("manuscript", "A document or book written by hand rather than printed")
            + " had crossed deserts from one script to another. "
            "The Silk Road had not been a single road but a braid of routes; "
            + vw("papermaking", "The process of producing paper from plant fibers mixed with water and pressed flat")
            + " had traveled that braid in workshops built beside caravanserais where traders had rested camels and swapped recipes along with pepper.</p>"
            "<p>Next time you fold a notebook page, remember it had descended from "
            + vw("pulp", "A soft mass of fibers beaten from plants or rags, used to make paper")
            + " beaten in Central Asian vats—technology that had turned the Silk Road into a highway for words. "
            "Although empires had risen on swords, they had endured on "
            + vw("dissemination", "The spreading of something widely among people or places")
            + ": paper sheets lighter than armor, carrying algebra, stories, and laws from Chang'an to Cordoba without ever needing to clink like gold.</p>"
        ),
        "questions": [
            {"id": "q1", "question": "What materials were used in early Chinese papermaking?",
             "hint": "Bark, hemp, and rags.",
             "answers": ["bark hemp and rags", "plant fibers and rags", "mulberry bark and hemp", "soaked plant fibers"],
             "explanation": "Early papermakers soaked and beat bark, hemp, and rags into pulp, then screened and pressed the fibers into thin sheets."},
            {"id": "q2", "question": "How did papermaking spread west along the Silk Road?",
             "hint": "Captured artisans after a battle.",
             "answers": ["captured Chinese papermakers", "spread after Samarkand battle", "artisans taken west", "technology leaked along trade routes"],
             "explanation": "Papermaking likely spread west when Chinese papermakers were captured near Samarkand, then established mills that spread the craft along Silk Road trade routes."},
            {"id": "q3", "question": "Why did paper help Islamic libraries grow?",
             "hint": "Cheaper than parchment or silk.",
             "answers": ["affordable copying", "cheaper than parchment", "paper made wide circulation possible", "lower cost for manuscripts"],
             "explanation": "Paper was affordable enough for extensive copying, enabling Islamic libraries to circulate astronomical, mathematical, and medical manuscripts widely."},
            {"id": "q4", "question": "What is pulp in papermaking?",
             "hint": "Beaten fiber mass.",
             "answers": ["beaten fiber mass", "soft mass of plant fibers", "fibers mashed from bark and rags", "fiber mixture for paper"],
             "explanation": "Pulp is the soft mass of plant or rag fibers beaten and soaked until they separate, then spread on screens to form paper sheets."},
            {"id": "q5", "question": "Besides books, how did paper change economies in China?",
             "hint": "Money made from paper.",
             "answers": ["paper currency", "government issued paper money", "paper banknotes", "currency before Europe"],
             "explanation": "China used paper for government-issued currency long before European banks adopted paper money, changing how economies handled trade and taxation."},
        ],
        "curiosityHooks": [
            "Grandpa, paper spread because soldiers captured Chinese papermakers in a battle—do you think the Silk Road ran on secrets?",
            "Mom, Islamic scholars copied math and medicine because paper was cheap—would history change if they only had animal-skin parchment?",
            "They invented paper money centuries before Europe—would you trust a bill made from mulberry bark?",
        ],
        "shareMessage": (
            "Today's essay was about Silk Road paper! 📜🐫\n\n"
            "Chinese papermaking turned bark, hemp, and rags into pulp sheets—lighter and cheaper than bamboo or silk scrolls!\n\n"
            "The craft spread west when artisans were captured near Samarkand. "
            "Paper fueled Islamic libraries, medieval Europe, and even early Chinese currency.\n\n"
            "Ask us what pulp is and how paper traveled the Silk Road!"
        ),
    },
    {
        "id": "essay-020",
        "title": "The Reef's Single Night of Fire",
        "topic": "Coral Spawning Sync",
        "words": [
            {"word": "gamete", "definition": "A reproductive cell such as a sperm or egg that fuses with another to form a new organism"},
            {"word": "synchrony", "definition": "The state of happening at the same time or operating in unison"},
            {"word": "polyps", "definition": "Small tube-shaped animals that form coral colonies and secrete hard skeletons"},
            {"word": "lunar", "definition": "Relating to the moon or its cycles"},
            {"word": "broadcast", "definition": "To release or send out widely, as coral releasing eggs and sperm into water"},
        ],
        "grammarRules": GRAMMAR,
        "passageHtml": (
            "<p>On one moonlit night each year near the Great Barrier Reef, the ocean had sometimes looked as if it had snowed upside down—billions of pink and orange globules had risen from coral heads, drifting upward until the surface had shimmered like a sunset had dissolved into water. "
            "Divers who had witnessed the event had described silence broken only by bubbles and awe. "
            "Although any single coral polyp had seemed stationary and rock-like, entire reefs had coordinated the greatest group release of "
            + vw("gamete", "A reproductive cell such as a sperm or egg that fuses with another to form a new organism")
            + "s on Earth.</p>"
            "<p>Corals are colonies of tiny "
            + vw("polyps", "Small tube-shaped animals that form coral colonies and secrete hard skeletons")
            + "—animals related to jellyfish that had built limestone apartments over generations. "
            "Most had reproduced sexually by "
            + vw("broadcast", "To release or send out widely, as coral releasing eggs and sperm into water")
            + " spawning: eggs and sperm had been dumped into currents to meet by chance. "
            "That strategy had only worked if neighbors had released at once; otherwise gametes had diluted into useless soup. "
            "Even though individual polyps had lacked eyes, the reef had synchronized like an orchestra without a visible conductor.</p>"
            "<p>Scientists had pinned timing to "
            + vw("lunar", "Relating to the moon or its cycles")
            + " cues—often a full moon in spring or summer depending on species and latitude—combined with water temperature and sunset light. "
            "When conditions had aligned, chemical signals had rippled through colonies and "
            + vw("synchrony", "The state of happening at the same time or operating in unison")
            + " had exploded within hours. "
            "Although researchers had once guessed spawning had been random, night dives had proved otherwise; calendars had now been published predicting peak nights for tour boats and graduate students alike.</p>"
            "<p>The "
            + vw("broadcast", "To release or send out widely, as coral releasing eggs and sperm into water")
            + " cloud had fed plankton and fish while fertilized eggs had developed into larvae that had drifted days or weeks before settling on hard substrate. "
            "One successful night had seeded reefs miles away. "
            "Climate change had threatened the ritual— overheated water had caused bleaching that had weakened polyps and disrupted timing. "
            "Even though some colonies had spawned after partial recovery, mismatched "
            + vw("synchrony", "The state of happening at the same time or operating in unison")
            + " had reduced fertilization when neighbors had died.</p>"
            "<p>Aquarium biologists had replicated "
            + vw("lunar", "Relating to the moon or its cycles")
            + " cycles in tanks to induce spawning for restoration projects, collecting larvae to seed damaged reefs. "
            "Although lab coral had never matched wild spectacle, the technique had offered hope where storms and heat had scraped reefs bare.</p>"
            "<p>Indigenous reef cultures had long noticed seasonal rises of slick spawn slicks on water—signs that fish runs would follow. "
            "Marine parks had restricted anchoring on predicted nights so propellers had not shredded floating "
            + vw("gamete", "A reproductive cell such as a sperm or egg that fuses with another to form a new organism")
            + " clouds. "
            "Although tourists had booked flights to glimpse the snowstorm, the event had remained fundamentally fragile—one warm year could shift everything.</p>"
            "<p>Next time you see a coral photo, imagine what had happened after dark when millions of "
            + vw("polyps", "Small tube-shaped animals that form coral colonies and secrete hard skeletons")
            + " had opened like tiny chimneys and the sea had filled with future reefs. "
            "Although the colony had looked like stone by day, it had "
            + vw("broadcast", "To release or send out widely, as coral releasing eggs and sperm into water")
            + " life by moonlight—proof that the quietest neighborhoods had sometimes thrown the wildest parties on the planet.</p>"
        ),
        "questions": [
            {"id": "q1", "question": "What is coral broadcast spawning?",
             "hint": "Releasing eggs and sperm into water.",
             "answers": ["releasing gametes into water", "eggs and sperm dumped into currents", "mass release into ocean", "broadcasting reproductive cells"],
             "explanation": "Broadcast spawning is when coral polyps simultaneously release eggs and sperm into the water column for external fertilization by chance meeting in currents."},
            {"id": "q2", "question": "Why must corals spawn in synchrony?",
             "hint": "Gametes must meet before diluting.",
             "answers": ["increase fertilization success", "gametes must meet at same time", "prevent dilution in ocean", "neighbors must release together"],
             "explanation": "Synchronized spawning ensures enough gametes are present at once for successful fertilization before they disperse and dilute in ocean currents."},
            {"id": "q3", "question": "What cues trigger synchronized coral spawning?",
             "hint": "Moon, temperature, sunset.",
             "answers": ["lunar cycles and temperature", "full moon and water temperature", "moon phase sunset and warmth", "lunar and seasonal cues"],
             "explanation": "Coral spawning typically aligns with lunar cycles—often full moons—combined with seasonal water temperature and sunset light patterns."},
            {"id": "q4", "question": "What are coral polyps?",
             "hint": "Tiny animals building reefs.",
             "answers": ["small coral animals", "tube-shaped colony builders", "tiny animals that secrete skeletons", "individual coral animals"],
             "explanation": "Polyps are small tube-shaped animals that form coral colonies, secrete hard limestone skeletons, and collectively build reef structures."},
            {"id": "q5", "question": "How does climate change threaten coral spawning?",
             "hint": "Bleaching disrupts timing and health.",
             "answers": ["bleaching weakens polyps", "disrupts synchrony", "heat stress reduces spawning", "warming kills neighbors and timing"],
             "explanation": "Ocean warming causes bleaching that weakens polyps, kills colonies, and disrupts the synchronized timing needed for successful mass spawning."},
        ],
        "curiosityHooks": [
            "Grandma, the whole reef 'snows' eggs one moonlit night a year—would you go diving if it looks like sunset in the water?",
            "Mom, corals sync spawning like a secret calendar—how do you think they agree without phones?",
            "If climate change messes up the sync, baby corals might never meet—what can we do to keep the reef's party on schedule?",
        ],
        "shareMessage": (
            "Today's reading was about coral spawning sync! 🪸🌕\n\n"
            "Coral polyps release gametes together on predicted full-moon nights—broadcast spawning that looks like an underwater snowstorm!\n\n"
            "Synchrony ensures fertilization before gametes drift away. "
            "Scientists track lunar and temperature cues; climate bleaching threatens the timing.\n\n"
            "Ask us what a gamete is and why the whole reef spawns on one night!"
        ),
    },
    {
        "id": "essay-021",
        "title": "When Animals Feel the Earth Shift",
        "topic": "Earthquake Animal Behavior",
        "words": [
            {"word": "seismic", "definition": "Relating to earthquakes or vibrations of the earth"},
            {"word": "precursory", "definition": "Serving as a warning sign that something larger is about to happen"},
            {"word": "anomaly", "definition": "Something that deviates from what is standard, normal, or expected"},
            {"word": "evacuation", "definition": "The organized removal of people or animals from a dangerous place"},
            {"word": "tremor", "definition": "A small earthquake or slight shaking of the ground"},
        ],
        "grammarRules": GRAMMAR,
        "passageHtml": (
            "<p>On February 4, 1975, officials in Haicheng, China, had ordered an "
            + vw("evacuation", "The organized removal of people or animals from a dangerous place")
            + " that had saved tens of thousands of lives hours before a magnitude 7.3 earthquake had struck. "
            "The warning had not come from satellites or smartphone alerts—those had not existed. "
            "Instead, reports had piled up of strange animal behavior: snakes had surfaced from hibernation in freezing weather, cattle had refused to enter barns, rats had run in daylight. "
            "Although skeptics had called it folklore, the city had emptied—and when buildings had collapsed, many people had been elsewhere.</p>"
            "<p>Animals had sensed "
            + vw("seismic", "Relating to earthquakes or vibrations of the earth")
            + " signals humans had missed. "
            "Dogs had barked without cause; fish had jumped in still ponds; birds had flushed from roosts minutes before "
            + vw("tremor", "A small earthquake or slight shaking of the ground")
            + "s humans had finally felt. "
            "Researchers had proposed several mechanisms— animals had detected P-waves, the faster but weaker seismic waves that had arrived seconds before destructive S-waves; they had felt ground tilt or groundwater changes; they had heard infrasound below human hearing. "
            "Even though no single explanation had fit every story, the pattern had appeared often enough to study.</p>"
            "<p>Scientists had searched for "
            + vw("precursory", "Serving as a warning sign that something larger is about to happen")
            + " "
            + vw("anomaly", "Something that deviates from what is standard, normal, or expected")
            + "s in reliable data. "
            "Japan had monitored catfish in tanks; China had maintained observation networks for snakes and rodents near fault lines. "
            "Although Haicheng had seemed like proof, later quakes had hit without animal warnings—false negatives had undermined confidence. "
            "Statisticians had also noted false positives: animals had acted oddly on calm days too.</p>"
            "<p>Modern seismology had focused on instruments—gps creep, strain meters, aftershock patterns—rather than zoo behavior. "
            "Yet pet owners had continued reporting dogs pacing before quakes worldwide. "
            "Some biologists had suggested evolution had favored "
            + vw("seismic", "Relating to earthquakes or vibrations of the earth")
            + " sensitivity in burrowing species because falling tunnels had killed careless ones. "
            "Even though city pigeons had faced fewer cave-ins, nervous systems had sometimes retained ancient alarms.</p>"
            "<p>Technology had merged old and new in limited ways. "
            "Motion sensors on farms had logged cattle clustering hours before Italian "
            + vw("tremor", "A small earthquake or slight shaking of the ground")
            + "s; apps had invited citizens to report pet "
            + vw("anomaly", "Something that deviates from what is standard, normal, or expected")
            + "s alongside instrument readings. "
            "Although prediction had remained imperfect, rapid "
            + vw("evacuation", "The organized removal of people or animals from a dangerous place")
            + " after early shaking had saved lives where building codes had been weak.</p>"
            "<p>Haicheng's success had been unique—foreshocks, odd weather, and animal reports had combined with brave officials willing to act. "
            "Most earthquakes had still arrived without dress rehearsal. "
            "Although we had not built a zoo-based early-warning system, the stories had reminded us that biology had sometimes felt the planet flex before our calendars had noticed.</p>"
            "<p>Next time your dog stares at the wall and whines, you will probably blame squirrels—but remember Haicheng's snakes in snow, a "
            + vw("precursory", "Serving as a warning sign that something larger is about to happen")
            + " whisper from faults deep below. "
            "Although instruments had mapped "
            + vw("seismic", "Relating to earthquakes or vibrations of the earth")
            + " waves with precision, animals had remained Earth's older sensors—imperfect, mysterious, and occasionally right when seconds had mattered most.</p>"
        ),
        "questions": [
            {"id": "q1", "question": "What happened in Haicheng, China in 1975 before the major earthquake?",
             "hint": "Animals acted strangely; city evacuated.",
             "answers": ["mass evacuation", "animal behavior warnings", "snakes and rats acted oddly", "officials evacuated before quake"],
             "explanation": "Before the 1975 Haicheng earthquake, unusual animal behavior reports combined with other signs prompted officials to evacuate, saving tens of thousands of lives."},
            {"id": "q2", "question": "What are P-waves and why might animals detect them before humans?",
             "hint": "Faster, weaker seismic waves arrive first.",
             "answers": ["faster seismic waves first", "P-waves arrive before destructive waves", "weaker tremors animals feel first", "primary waves seconds earlier"],
             "explanation": "P-waves are faster, weaker seismic waves that arrive seconds before destructive S-waves; animals may feel or hear these precursory tremors before humans notice shaking."},
            {"id": "q3", "question": "Why is animal earthquake prediction considered unreliable?",
             "hint": "False positives and missed quakes.",
             "answers": ["false positives and false negatives", "animals act oddly on calm days too", "many quakes have no animal warnings", "not consistent enough"],
             "explanation": "Animal behavior anomalies occur on non-earthquake days too (false positives), and many earthquakes strike without reported animal warnings (false negatives), making prediction unreliable."},
            {"id": "q4", "question": "What does precursory mean in earthquake studies?",
             "hint": "Warning signs before a larger event.",
             "answers": ["warning before main event", "early sign of earthquake", "signal before larger quake", "advance indicator"],
             "explanation": "Precursory signals or behaviors are changes that may appear before a larger earthquake, though they are not consistently reliable for prediction."},
            {"id": "q5", "question": "What evolutionary reason might explain seismic sensitivity in some animals?",
             "hint": "Burrowing animals survive tunnel collapses.",
             "answers": ["burrowing species avoid collapse", "evolution favored seismic sensitivity", "tunnel fallers died", "ancient alarm systems retained"],
             "explanation": "Burrowing animals that sensed seismic vibrations early may have survived collapsing tunnels, so evolution may have favored seismic sensitivity in some species."},
        ],
        "curiosityHooks": [
            "Grandpa, China evacuated a whole city because snakes woke up in winter—would you leave home if our dog acted that weird?",
            "Mom, dogs might feel earthquake P-waves seconds before we do—should we trust Fido more than my phone alert?",
            "Haicheng saved thousands but most quakes have no animal warning—why do you think snakes got it right that one time?",
        ],
        "shareMessage": (
            "Today's essay was about earthquake animal behavior! 🐍🌍\n\n"
            "Before the 1975 Haicheng earthquake, snakes, rats, and cattle acted strangely—and officials evacuated in time to save tens of thousands!\n\n"
            "Animals may detect P-waves, infrasound, or groundwater changes before we feel tremors. "
            "But false alarms make zoo-based prediction unreliable.\n\n"
            "Ask us what a precursory anomaly is and why Haicheng was special!"
        ),
    },
]


def main():
    with open(BANK_PATH, encoding="utf-8") as f:
        existing = json.load(f)
    if len(existing) != 7:
        print(f"Warning: expected 7 existing essays, found {len(existing)}")
    combined = existing + NEW_ESSAYS
    with open(BANK_PATH, "w", encoding="utf-8") as f:
        json.dump(combined, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Wrote {len(combined)} essays to {BANK_PATH}")
    # Validate
    with open(BANK_PATH, encoding="utf-8") as f:
        validated = json.load(f)
    assert len(validated) == 21, f"Expected 21 entries, got {len(validated)}"
    ids = [e["id"] for e in validated]
    assert ids == [f"essay-{i:03d}" for i in range(1, 22)], f"ID mismatch: {ids}"
    print("JSON valid. 21 entries confirmed.")


if __name__ == "__main__":
    main()

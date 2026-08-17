#!/usr/bin/env python3
"""Expand short essay passages (009-021) toward ~600 words."""
import json
import re
from pathlib import Path

BANK = Path(__file__).parent / "essay-bank.json"

# Extra paragraphs inserted before the final "Next time" paragraph
EXPANSIONS = {
    "essay-009": (
        "<p>European robins had become the poster birds for the quantum hypothesis. "
        "When researchers had placed them inside shielded chambers that had blocked normal magnetic cues, "
        "the birds had still oriented correctly—until wavelengths of light that could affect "
        "cryptochrome had been filtered out. Although the evidence had remained debated, "
        "physicists and ornithologists had begun collaborating in ways no textbook had predicted. "
        "Even though a robin's brain had weighed less than a grape, it had possibly been performing "
        "calculations at the edge of what laboratories had measured in chilled crystals.</p>"
        "<p>Homing pigeons had offered another puzzle. "
        "For decades, trainers had released birds hundreds of miles from lofts they had never seen from the air, "
        "yet most had returned by afternoon. "
        "Magnets taped to their heads had confused some; olfactory maps and visual landmarks had explained others. "
        "Although no single sense had accounted for every journey, magnetoreception had remained the ghost "
        "in the compass—always present in the data, never fully captured in a cage.</p>"
    ),
    "essay-010": (
        "<p>Computer scientists had noticed something humbling. "
        "When engineers had compared slime-mold networks to Tokyo rail maps, "
        "the fungus had often matched human designs for efficiency—connecting food sources with minimal total length. "
        "Although the plasmodium had possessed no planning committee, its foraging algorithm had converged on solutions "
        "that had taken human transit planners decades to refine. "
        "Even though the comparison had been partly a thought experiment, "
        "urban designers had cited it when arguing that nature had solved routing problems long before spreadsheets.</p>"
        "<p>Biologists had also watched slime molds learn. "
        "After crossing a bridge laced with irritants, a plasmodium had later avoided that path—even when the bridge "
        "had been cleaned and the irritant had been gone. "
        "Although the organism had lacked neurons, it had stored something like habit in its protoplasmic body. "
        "Researchers had debated whether to call that memory or simply chemical residue; "
        "either way, the maze had not been solved once by accident but twice by choice.</p>"
    ),
    "essay-011": (
        "<p>Inside the thermopolia, counters had displayed round vessels called dolia—large clay jars sunk into masonry "
        "to keep stews warm through the day. "
        "Archaeologists had found ladles, bronze pans, and graffiti advertising the day's special in crude Latin script. "
        "Although Pompeii had been a resort town for the wealthy, "
        "most citizens had eaten out because apartment kitchens had been tiny and fire had been dangerous indoors. "
        "Even though the bread ovens had supplied the city, the hot-food counters had supplied its rhythm—breakfast "
        "for laborers, midday wine for merchants, evening gossip for neighbors who had known each other's faces for generations.</p>"
        "<p>Modern bakers had attempted to recreate Pompeian loaves from carbonized specimens. "
        "They had ground spelt, shaped rings scored with a knife in the traditional eight-section pattern, "
        "and baked in wood-fired ovens until the crust had crackled like the originals. "
        "Although no recipe card had survived Vesuvius, "
        "chemical analysis of ash-trapped crumbs had revealed barley, emmer wheat, and traces of bay leaf. "
        "Tourists visiting the ruins today had often said the recreated bread had tasted dense and honest—"
        "food meant to fill a stomach before a day hauling pumice or mending nets.</p>"
    ),
    "essay-012": (
        "<p>Recording technology had transformed whale research. "
        "Before portable hydrophones, scientists had leaned over boat rails with microphones dipped in kelp-stained water. "
        "Today autonomous buoys had listened continuously, uploading terabytes of song to servers that had never slept. "
        "Although machine-learning tools had begun picking out new phrases faster than human ears, "
        "graduate students had still spent nights wearing headphones, "
        "learning to recognize the sighing introduction that had announced a humpback's theme.</p>"
        "<p>Conservation had depended on those recordings. "
        "When shipping lanes had been moved away from breeding grounds, "
        "researchers had compared song clarity before and after—measuring whether males had sung longer suites "
        "when engines had grown distant. "
        "Even though whales had no vote in harbor planning, "
        "their acoustic repertoire had become evidence in courtrooms arguing for quieter seas. "
        "Although the ocean had never been silent, the baseline humans had chosen for restoration had been the "
        "decade when Payne had first pressed play and listeners had wept at what they had heard.</p>"
    ),
    "essay-013": (
        "<p>Not every glowing cave had belonged to glowworms. "
        "In Puerto Rico's Río Camuy system and Vietnam's Hang Thung, "
        "explorers had documented fungal bioluminescence on rotting wood carried underground by floods. "
        "Although the light had been fainter than Waitomo's constellations, "
        "speleological teams had mapped chambers where entire fallen trees had glowed green like submerged auroras. "
        "Even though the fungi had gained no obvious benefit from shining in total darkness, "
        "insects attracted to light had spread spores along the cave floor—another predatory partnership written in photons.</p>"
        "<p>Indigenous peoples had known some glowing caves long before tourism. "
        "Māori guides in New Zealand had passed stories about starless skies underground, "
        "treating the worms as taonga—treasures to protect rather than commodities to exploit. "
        "Although modern visitor centers had brought economic benefits to rural regions, "
        "elders had reminded managers that the cave had been a living river system, not a theater with a switch. "
        "When water quality had declined, glowworm numbers had dropped within a single season—"
        "proof that the ceiling's stars had depended on hillsides no tourist had ever photographed.</p>"
    ),
    "essay-014": (
        "<p>Axolotl genetics had become a frontier tool. "
        "When CRISPR editors had knocked out specific regeneration genes, "
        "limbs had failed to rebuild—pinpointing molecular switches humans had shared but rarely activated. "
        "Although editing salamander embryos had required patience measured in years, "
        "the data had flowed into databases comparing axolotls to mice, zebrafish, and human cell cultures. "
        "Even though a smiling amphibian had seemed an unlikely medical model, "
        "pharmaceutical labs had invested because scars had been the enemy of function, and axolotls had simply refused to scar.</p>"
        "<p>Local conservationists in Xochimilco had launched chinampa restoration—"
        "floating gardens that had filtered water and sheltered native axolotls from invasive tilapia. "
        "Schoolchildren had released captive-bred animals into canals that had once been the species' heartland. "
        "Although urban sprawl had not reversed overnight, "
        "each clean channel had represented hope that wild populations could recover if the city had shared its water with a creature "
        "that had never learned to walk on land but had learned to rebuild itself from almost nothing.</p>"
    ),
    "essay-015": (
        "<p>Supercolonies had not been limited to Argentine ants. "
        "Invasive yellow crazy ants on Christmas Island had formed high-density swarms that had blinded and killed "
        "millions of red land crabs during their annual migration—disrupting a migration so ancient "
        "that island forests had evolved to depend on crab droppings for fertilizer. "
        "Although the ant species had differed, the pattern had repeated: "
        "uniform scent, reduced territorial fighting, exponential spread once humans had moved soil across oceans.</p>"
        "<p>Ant researchers had also found hope in division. "
        "When supercolonies had grown large enough, subtle scent drift had occasionally split them into warring factions again—"
        "evolution testing whether cooperation without borders could last forever. "
        "Although such splits had rarely reversed invasion, "
        "they had reminded ecologists that even the most unicolonial empire had carried the seeds of its own fracture. "
        "Even though a sidewalk trail had looked harmless, "
        "the workers marching across it might have belonged to a network that had rewritten entire continents beneath our feet.</p>"
    ),
    "essay-016": (
        "<p>Medieval monks had copied manuscripts in scriptoria while memorizing long liturgical passages using similar spatial tricks. "
        "Although parchment had been precious, "
        "oral rehearsal had remained essential because books had been scarce and candles had been rationed. "
        "A novice had walked mentally through the abbey cloister, placing each psalm verse on a column or fountain "
        "until the route had become a library no fire could burn. "
        "Even though the method had predated Rome, Christian monasteries had preserved it through centuries when literacy had been rare.</p>"
        "<p>Modern memory athletes had pushed the palace far beyond speeches. "
        "Competitors had memorized shuffled decks of cards in under twenty seconds by assigning each card "
        "an image in a familiar gymnasium or childhood street. "
        "Although neuroscience had shown such training had thickened connections in spatial memory regions, "
        "schoolteachers had begun adapting simplified versions for vocabulary lists and history timelines. "
        "When a student had complained that facts had slipped away overnight, "
        "coaches had asked where in the mental house the dates had been stored—and whether the images had been vivid enough to steal attention from a phone screen.</p>"
    ),
    "essay-017": (
        "<p>Einstein's general relativity had predicted the bending of starlight decades before astronomers had photographed it. "
        "During a 1919 solar eclipse, "
        "Arthur Eddington's expedition had measured stars near the sun appearing slightly out of place—"
        "their light deflected by the sun's gravitational field. "
        "Although the shift had been tiny, "
        "newspapers had declared that space itself could curve, and a theory born at a desk had passed its first public test.</p>"
        "<p>Modern observatories had turned gravitational lensing into a measuring tool. "
        "When distant galaxies had lined up behind massive clusters, "
        "their images had stretched into arcs and rings—Einstein rings—that had magnified light from objects too faint to see directly. "
        "Although the effect had once been a curiosity, "
        "cosmologists had used it to map dark matter that had never emitted a photon yet had bent light like invisible glass. "
        "Even though black holes had remained the most dramatic lenses, "
        "every massive object had tugged photons off straight lines—reminding stargazers that looking upward had always meant looking through gravity's sculpture.</p>"
    ),
    "essay-018": (
        "<p>Charles Darwin had been fascinated by Dionaea muscipula—the Venus flytrap he had called "
        "\"one of the most wonderful plants in the world.\" "
        "He had timed how long traps had held prey and had fed them raw meat to prove the plant had truly eaten animal tissue. "
        "Although Victorian readers had found carnivorous plants unsettling, "
        "Darwin's experiments had shown they had thrived in nitrogen-poor bogs where roots alone could not supply enough nutrients.</p>"
        "<p>High-speed cameras had later revealed the trap's secret tempo. "
        "Each trigger hair had required two touches within about twenty seconds to fire—"
        "a filter that had ignored raindrops but had snapped shut on struggling insects. "
        "Although the closing motion had looked violent, "
        "the plant had spent more energy digesting than catching; "
        "failed traps that had closed on pebbles or twigs had often died because digestion had cost more than the meal had returned. "
        "Even though the flytrap had evolved in a narrow band of Carolina wetlands, "
        "its mechanistic hunger had become a classroom icon for how plants could act with animal-like speed when soil had refused to feed them.</p>"
    ),
    "essay-019": (
        "<p>Paper had not spread west instantly. "
        "For centuries, parchment from animal skins had remained the prestige medium for European charters and Bibles—"
        "expensive, durable, and smelly when fresh. "
        "Although Arabic scholars in Baghdad had embraced paper for astronomy and medicine by the ninth century, "
        "Latin monasteries had copied manuscripts on calfskin long after merchants had carried cheaper rolls along Silk Road caravans.</p>"
        "<p>When paper mills had finally multiplied in Italy and Spain, "
        "the cost of books had collapsed and literacy had begun its slow climb beyond elites. "
        "Printers in the fifteenth century had combined paper with movable type, "
        "multiplying texts faster than any scribe could copy by hand. "
        "Although the Silk Road's camel routes had faded as sea trade had grown, "
        "the pulp technology they had carried had reshaped universities, law courts, and eventually newspapers. "
        "Even though a sheet looked humble, "
        "it had been the vessel that had turned knowledge from a luxury good into something a merchant's apprentice could afford to stain with ink and argue over by candlelight.</p>"
    ),
    "essay-020": (
        "<p>Divers who had witnessed a mass spawn had described the ocean turning into a blizzard of pink and white—"
        "millions of egg and sperm bundles rising toward the surface in synchronized clouds. "
        "Although individual polyps had looked like static rocks by day, "
        "they had become fountains after dark, releasing gametes within minutes of neighbors both near and far. "
        "Satellite temperature data and lunar calendars had helped scientists predict the night, "
        "but local cues—water chemistry, sunset light—had still mattered enough that predictions had occasionally missed by a day.</p>"
        "<p>Climate stress had threatened the timing. "
        "When seas had warmed too quickly, "
        "some reefs had spawned out of sync, reducing fertilization because eggs and sperm had drifted alone. "
        "Although captive breeding programs had collected gametes in floating nurseries, "
        "restoration had depended on wild reefs still firing together like biological fireworks. "
        "Even though a single polyp had seemed insignificant, "
        "its willingness to release on the same moon as thousands of cousins had been the difference between a reef reborn and a reef remembered only in photographs.</p>"
    ),
    "essay-021": (
        "<p>Historical accounts had mixed folklore with observation. "
        "In 373 BC, Greek writers had recorded rats, snakes, and weasels fleeing Helice days before an earthquake—"
        "stories repeated so often that modern seismologists had treated them cautiously yet had not dismissed them entirely. "
        "Although mass animal movement could have unrelated causes, "
        "repeated reports from China, Japan, and California had suggested some species might detect precursory signals humans had ignored.</p>"
        "<p>Today sensor networks had outpaced anecdote. "
        "Seismologists had deployed accelerometers, gas sniffers, and strain gauges along fault lines, "
        "searching for reliable precursors that animals might feel first. "
        "Although no zookeeper had yet run a perfect earthquake forecast from restless elephants alone, "
        "researchers had documented anomalous behavior—unusual barking, refusals to enter stalls, "
        "restless fish in ponds—minutes to hours before some tremors. "
        "Even though evacuation based solely on animal oddities would have caused chaos, "
        "combining biological anomalies with instrument data had remained an active frontier—"
        "one where the dog scratching at the door might someday contribute to a warning humans could trust before the ground had finished arguing with itself.</p>"
    ),
}


def insert_before_final_paragraph(html: str, extra: str) -> str:
    """Insert extra paragraphs before the last <p>...</p> block."""
    parts = html.rsplit("</p>", 1)
    if len(parts) != 2:
        return html + extra
    return parts[0] + "</p>" + extra + "<p>" + parts[1].lstrip().removeprefix("<p>")


def main():
    data = json.loads(BANK.read_text(encoding="utf-8"))
    by_id = {e["id"]: e for e in data}
    for eid, extra in EXPANSIONS.items():
        if eid in by_id:
            by_id[eid]["passageHtml"] = insert_before_final_paragraph(
                by_id[eid]["passageHtml"], extra
            )
    BANK.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for e in data:
        if e["id"] in EXPANSIONS:
            text = re.sub(r"<[^>]+>", " ", e["passageHtml"])
            print(e["id"], len(text.split()), "words")


if __name__ == "__main__":
    main()

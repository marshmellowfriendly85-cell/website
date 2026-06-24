from __future__ import annotations

import hashlib
import html
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).parent


OFFICIAL = {
    "I": "mi",
    "you": "ta",
    "person": "li",
    "he": "lih",
    "she": "lis",
    "it": "lit",
    "we": "mu",
    "they": "lu",
    "be": "be",
    "have": "su",
    "has": "su",
    "belong": "bel",
    "go": "ko",
    "come": "la",
    "eat": "mo",
    "drink": "dri",
    "read": "re",
    "write": "wri",
    "speak": "ra",
    "say": "say",
    "know": "ni",
    "think": "th",
    "study": "stu",
    "learn": "ler",
    "teach": "te",
    "work": "wer",
    "play": "pla",
    "walk": "bo",
    "wait": "wa",
    "help": "hel",
    "take": "tak",
    "give": "giv",
    "get": "get",
    "make": "mak",
    "do": "do",
    "build": "bu",
    "fix": "fix",
    "open": "open",
    "close": "clos",
    "start": "start",
    "stop": "stop",
    "like": "lik",
    "love": "lov",
    "hate": "hat",
    "want": "want",
    "need": "ned",
    "see": "see",
    "look": "luk",
    "watch": "wat",
    "tell": "tel",
    "ask": "ask",
    "answer": "ans",
    "call": "cal",
    "join": "join",
    "leave": "lev",
    "buy": "buy",
    "sell": "sel",
    "pay": "pay",
    "use": "use",
    "try": "try",
    "find": "find",
    "lose": "los",
    "win": "win",
    "live": "liv",
    "die": "die",
    "can": "kan",
    "must": "mus",
    "should": "shud",
    "may": "may",
    "of": "ov",
    "currently": "du",
    "not": "na",
    "there is": "ex",
    "that": "dat",
    "and": "e",
    "or": "o",
    "but": "bat",
    "therefore": "so",
    "if": "if",
    "because": "bec",
    "then": "den",
    "also": "also",
    "what": "wt",
    "who": "hu",
    "where": "wer",
    "when": "wen",
    "why": "wai",
    "how": "hou",
    "this": "dis",
    "these": "dese",
    "those": "dose",
    "in": "al",
    "on": "on",
    "under": "un",
    "at": "at",
    "to": "tu",
    "from": "fram",
    "near": "ne",
    "with": "wit",
    "without": "no",
    "about": "ab",
    "for": "for",
    "through": "thru",
    "over": "ova",
    "between": "bit",
    "here": "hir",
    "there": "der",
    "somewhere": "som",
    "everywhere": "evr",
    "nowhere": "noh",
    "now": "now",
    "today": "ted",
    "yesterday": "yesd",
    "tomorrow": "tomd",
    "morning": "morn",
    "afternoon": "aft",
    "evening": "eve",
    "night": "nit",
    "early": "ear",
    "later": "lat",
    "before": "bef",
    "after": "afta",
    "during": "dur",
    "until": "unt",
    "since": "sin",
    "again": "agai",
    "already": "alred",
    "still": "stil",
    "zero": "nul",
    "one": "un",
    "two": "du",
    "three": "tri",
    "four": "for",
    "five": "fin",
    "six": "sis",
    "seven": "sev",
    "eight": "et",
    "nine": "nin",
    "ten": "ten",
    "hundred": "hun",
    "thousand": "mil",
    "all": "all",
    "some": "sum",
    "any": "ani",
    "every": "eve",
    "many": "multi",
    "few": "few",
    "more": "mor",
    "less": "les",
    "most": "mos",
    "least": "lest",
    "only": "only",
    "good": "gud",
    "bad": "bad",
    "big": "bi",
    "small": "sm",
    "new": "new",
    "old": "old",
    "hot": "hot",
    "cold": "cold",
    "fast": "fast",
    "slow": "slow",
    "strong": "stron",
    "weak": "weak",
    "important": "imp",
    "same": "same",
    "different": "dif",
    "easy": "easy",
    "hard": "hard",
    "happy": "hap",
    "sad": "sad",
    "really": "real",
    "very": "veri",
    "doctor": "dok",
    "teacher": "teer",
    "learner": "lerer",
    "friend": "fri",
    "man": "man",
    "woman": "wom",
    "guy": "voru",
    "child": "kid",
    "baby": "bab",
    "family": "fam",
    "food": "mek",
    "water": "ven",
    "bread": "bred",
    "rice": "ric",
    "egg": "egg",
    "fish": "fis",
    "meat": "mit",
    "fruit": "frut",
    "vegetable": "veg",
    "apple": "apl",
    "banana": "ban",
    "tea": "tisa",
    "coffee": "kofi",
    "house": "dom",
    "room": "rum",
    "door": "dor",
    "window": "windo",
    "bed": "bed",
    "table": "tab",
    "chair": "chair",
    "lamp": "lamp",
    "key": "key",
    "book": "buk",
    "pen": "pen",
    "paper": "paper",
    "bag": "bag",
    "box": "box",
    "glass": "glas",
    "car": "kar",
    "bus": "bus",
    "train": "train",
    "bicycle": "bike",
    "ship": "ship",
    "airplane": "plane",
    "road": "road",
    "phone": "tel",
    "computer": "kom",
    "internet": "net",
    "video": "vid",
    "game": "gam",
    "sun": "sol",
    "moon": "mun",
    "star": "star",
    "rain": "rain",
    "wind": "wind",
    "tree": "tree",
    "grass": "gras",
    "sea": "sea",
    "river": "riv",
    "mountain": "mount",
    "cat": "kat",
    "dog": "dog",
    "bird": "bird",
    "cow": "cow",
    "horse": "hors",
    "pig": "pig",
    "time": "tim",
    "life": "lif",
    "death": "dea",
    "joy": "joy",
    "happiness": "hapnes",
    "problem": "problem",
    "question": "question",
    "idea": "idea",
    "truth": "truth",
    "hello": "hei",
    "hi": "haj",
    "yes": "ye",
    "no": "nu",
    "okay": "oya",
    "thanks": "tia",
}


OFFICIAL.update({
    "feet": "petoi",
    "men": "mani",
    "women": "womi",
    "children": "kidi",
    "mice": "logani",
    "leaves": "ziroi",
    "halves": "vukoki",
    "knives": "mokosi",
    "lives": "lifi",
    "elves": "elfai",
    "potatoes": "potai",
    "tomatoes": "tomai",
    "people": "li",

    "me": "mia",
    "mine": "mai",

    "off": "ofa",

    "dragon": "draga",
    "wizard": "viza",
    "witch": "wika",
    "vampire": "vampa",
    "werewolf": "wulf-man",
    "zombie": "zomba",
    "demon": "dema",
    "angel": "anja",
    "fairy": "fara",
    "goblin": "gobla",
    "troll": "trola",
    "dwarf": "dwafa",
    "elf": "elfa",
    "mermaid": "mera ma",
    "unicorn": "unika",
    "pegasus": "pega",
    "phoenix": "fenix",
    "monster": "monsta",
    "universe": "univaall",
    "asteroid": "astropa",
    "comet": "koma",
    "meteor": "meteo",
    "black hole": "blakahol",
    "nebula": "nebu",
    "astronaut": "astro",
    "spaceship": "spasaship",
    "orbit": "orba",
    "satellite": "satela",
    "telescope": "teleskop",
    "gravity": "gravita",
    "tsunami": "tsuna",
    "avalanche": "avalan",
    "blizzard": "bliza",
    "thunderstorm": "tundastorm",
    "lightning": "litastrike",
    "rainbow": "rainabow",
    "sunset": "solaset",
    "sunrise": "solarise",
    "eclipse": "eklisa",
    "basketball": "baskabal",
    "baseball": "basabal",
    "tennis": "tena",
    "soccer": "sokabal",
    "volleyball": "volabal",
    "swimming": "swimasport",
    "boxing": "boxa",
    "wrestling": "vresla",
    "cycling": "sikla",
    "running": "runasport",
    "gymnastics": "jima",
    "skating": "skata",
    "skiing": "skia",
    "surfing": "surfa",
    "hiking": "hikasport",
    "fishing": "fishasport",
    "camping": "kampa",
    "microwave": "mikra",
    "refrigerator": "frija",
    "freezer": "friza",
    "toaster": "tosta",
    "blender": "blenda",
    "dishwasher": "dishavash",
    "washing machine": "vashamach",
    "dryer": "driamach",
    "vacuum": "vakua",
    "broom": "bruma",
    "mop": "mopa",
    "bucket": "buketa",
    "hammer": "hama",
    "screwdriver": "skrudriva",
    "wrench": "vrencha",
    "pliers": "plia",
    "axe": "axa",
    "shovel": "shova",
    "rake": "raka",
    "hoe": "hoatol",
    "nails": "nailahard",
    "screws": "skrua",
    "bolts": "bolta",
    "nuts": "nutahard",
    "glue": "glua",

    "penguin": "penga",
    "kangaroo": "kanga",
    "koala": "koal",
    "dolphin": "dolfa",
    "whale": "vala",
    "shark": "sharka",
    "octopus": "okta",
    "jellyfish": "jela",
    "starfish": "starafis",
    "crab": "krab",
    "lobster": "loba",
    "shrimp": "shrim",
    "seahorse": "seahors",
    "seaweed": "seavid",
    "eagle": "igla",
    "hawk": "hoka",
    "falcon": "falko",
    "owl": "ola",
    "pigeon": "pija",
    "dove": "dova",
    "sparrow": "sparo",
    "crow": "kro",
    "raven": "rava",
    "swan": "swana",
    "peacock": "pika",
    "parrot": "paro",
    "flamingo": "flami",
    "ostrich": "ostra",
    "woodpecker": "wodapek",
    "avocado": "avo",
    "coconut": "koko",
    "pineapple": "pina",
    "watermelon": "vatamel",
    "strawberry": "stra",
    "blueberry": "bluber",
    "raspberry": "raspa",
    "blackberry": "blakaber",
    "peach": "picha",
    "plum": "pluma",
    "cherry": "cheri",
    "grape": "grapa",
    "mango": "mango",
    "papaya": "papa",
    "kiwi": "kiwi",
    "lemon": "lema",
    "grapefruit": "grapafrut",
    "pomegranate": "poma",
    "onion": "onia",
    "carrot": "karo",
    "potato": "pota",
    "tomato": "toma",
    "cucumber": "kuku",
    "broccoli": "broko",
    "spinach": "spina",
    "lettuce": "letu",
    "cabbage": "kaba",
    "mushroom": "musha",
    "corn": "korna",
    "peas": "pizaveg",
    "beans": "bina",
    "lentils": "lenta",
    "monitor": "monita",
    "mousepad": "mauspad",
    "headphones": "hedfons",
    "microphone": "mika",
    "speaker": "spika",
    "webcam": "webakam",
    "router": "routa",
    "modem": "moda",
    "charger": "charja",
    "pixel": "pixa",
    "file": "fila",
    "folder": "folda",
    "image": "imaja",
    "audio": "odio",
    "software": "softa",
    "hardware": "hardaware",
    "network": "netavork",
    "website": "webasit",
    "sweater": "sweta",
    "hoodie": "huda",
    "gloves": "glova",
    "mittens": "mita",
    "socks": "sokawear",
    "boots": "butawear",
    "sneakers": "snika",
    "sandals": "sanda",
    "heels": "helawear",
    "slippers": "slipa",
    "necklace": "nekles",
    "bracelet": "brasa",
    "earrings": "iraring",
    "glasses": "glasa",
    "sunglasses": "solglasa",
    "beanie": "binahat",
    "cowardly": "kowada",
    "deceitful": "desita",
    "loyal": "loya",
    "jealous": "jelaemo",
    "envious": "envi",
    "humble": "humba",
    "modest": "modaemo",
    "outgoing": "outgo",
    "hostile": "hosta",
    "stressed": "stresa",
    "hopeful": "hopaful",
    "pharmacist": "farmaist",
    "student": "studa",
    "principal": "prinsa",
    "professor": "profa",
    "scientist": "sienta",
    "engineer": "enjina",
    "mechanic": "mekana",
    "electrician": "elektra",
    "plumber": "plumba",
    "carpenter": "karpa",
    "painter": "painta",
    "artist": "arta",
    "musician": "muzika",
    "writer": "writaist",
    "photographer": "fota",
    "chef": "chefa",
    "baker": "baka",
    "waiter": "waita",
    "university": "univa",
    "library": "libra",
    "museum": "muza",
    "theater": "tiata",
    "cinema": "sinema",
    "stadium": "stadia",
    "restaurant": "resta",
    "cafe": "kafe",
    "post office": "postaofis",
    "police station": "polisasta",
    "fire station": "firasta",
    "church": "churka",
    "whisper": "wispa",
    "shout": "shota",
    "scream": "skrima",
    "frown": "frona",
    "wink": "winka",
    "stare": "stera",
    "peek": "pikaluk",
    "sigh": "saia",
    "yawn": "yona",
    "sneeze": "sniza",
    "hiccup": "hikupa",
    "burp": "burpa",
    "fart": "farta",
    "victory": "vikta",
    "success": "sukesa",
    "magic": "majika",
    "science": "sainsa",
    "art": "artakon",
    "music": "muzikakon",

    "magnificent": "magnifa",
    "breathtaking": "breta",
    "spectacular": "spekta",
    "astounding": "astonda",
    "fascinating": "fasina",
    "captivating": "kaptiva",
    "enchanting": "enchanta",
    "mesmerizing": "mezmera",
    "phenomenal": "fenoma",

    "basically": "bazika",
    "genuinely": "jenula",
    "literally": "litera",
    "seriously": "serioza",
    "obviously": "obvia",
    "clearly": "klaria",
    "supposedly": "suposa",
    "technically": "tekna",
    "specifically": "spesika",
    "essentially": "esenta",
    "ultimately": "ultima",
    "ironically": "irona",
    "surprisingly": "surpa",
    "thankfully": "graka",
    "unfortunately": "inforta",
    "weirdly": "weirda",
    "lowkey": "loka",
    "highkey": "hika",
    "kinda": "kinda",
    "arguably": "argula",
    "admittedly": "admita",
    "purely": "pura",
    "approximately": "aproxma",
    "typically": "tipika",
    "normally": "norma",
    "naturally": "natura",
    "mainly": "maina",
    "slightly": "slita",
    "fairly": "faira",
    "pretty": "prita",
    "super": "supa",
    "extremely": "extrima",
    "incredibly": "inkredla",
    "insanely": "insana",
    "wildly": "wilda",
    "terribly": "terba",
    "horribly": "horba",
    "awfully": "ofla",
    "dreadfully": "dreda",
    "ridiculously": "ridika",
    "unbelievably": "unbelva",

    "reveal": "rivela",
    "ignore": "ignora",
    "rely": "reliva",
    "share": "shara",
    "remove": "rimova",
    "replace": "riplas",
    "solve": "solva",
    "produce": "produka",
    "release": "rilisa",
    "require": "rikwira",
    "suggest": "sugesta",
    "support": "suporta",
    "reduce": "ridusa",
    "prevent": "preventa",
    "prepare": "prepara",
    "perform": "performa",
    "promise": "promisa",
    "prove": "pruva",
    "provide": "provida",
    "publish": "publisha",
    "pull": "pula",
    "push": "pusha",
    "raise": "raiza",
    "reach": "richa",
    "realize": "rializa",
    "recognize": "rekogniza",
    "reflect": "reflekta",
    "refuse": "refuza",
    "relate": "relata",
    "remain": "rimena",
    "remember": "rimembra",
    "repeat": "ripeta",
    "represent": "representa",
    "respect": "respekta",
    "respond": "risponda",
    "result": "rezulta",
    "return": "ritorna",
    "review": "rivyuwa",
    "roll": "rola",
    "rush": "rusha",
    "satisfy": "satisfa",
    "save": "seva",
    "shake": "sheka",
    "shine": "shina",
    "shoot": "shuta",
    "sign": "signa",
    "skip": "skipa",
    "slide": "slida",
    "sort": "sorta",
    "split": "splita",
    "spread": "spreda",
    "steal": "stila",
    "step": "stepa",
    "stick": "stika",
    "stretch": "strecha",
    "strike": "straka",
    "succeed": "suksida",
    "suffer": "sufra",
    "survive": "surviva",
    "test": "testa",
    "throw": "throwa",
    "touch": "tucha",
    "trust": "trusta",
    "turn": "turna",
    "unite": "unita",
    "upload": "uploda",
    "vote": "vota",
    "warn": "worna",
    "waste": "westa",
    "wonder": "wondra",
    "worry": "worya",
    "wrap": "rapa",
    "yell": "yela",
    "yield": "yilda",
    "zoom": "zuma",
    "mistake": "miztaka",
    "trouble": "trabla",
    "power": "powra",
    "culture": "kultura",
    "moment": "momenta",
    "reason": "rizona",
    "chance": "chansa",
    "effort": "efforta",
    "level": "levela",
    "method": "methoda",
    "order": "orda",
    "policy": "polisha",
    "process": "prosesa",
    "project": "projeka",
    "quality": "qualita",
    "resource": "risursa",
    "role": "rola",
    "sense": "sensa",
    "service": "servisa",
    "situation": "situwasha",
    "solution": "solushona",
    "source": "sursa",
    "space": "spasa",
    "structure": "struktura",
    "subject": "subjekta",
    "system": "sistema",
    "theory": "tiorya",

    "as": "asa",
    "dickhead": "pako",
    "piss": "piza",
    "loser": "luzu",

    "implied": "redu",
    "import": "gete",
    "impose": "susu",
    "impossible": "riko",
    "impress": "zoko",
    "impression": "sapa",
    "impressive": "kolu",
    "improve": "topu",
    "improvement": "nito",
    "incident": "piza",
    "include": "bafu",
    "including": "pido",
    "incorporate": "fipi",
    "increase": "nima",
    "increased": "lepo",
    "increasing": "zave",
    "increasingly": "pide",
    "incredible": "ture",
    "indeed": "livi",
    "independence": "tofa",
    "independent": "fina",
    "index": "voso",
    "Indian": "mulo",
    "indicate": "nibo",
    "indication": "rera",
    "individual": "lugi",
    "industrial": "pasu",
    "infant": "kefo",
    "infection": "turu",
    "inflation": "suve",
    "influence": "delo",
    "inform": "rone",
    "ingredient": "suli",
    "initial": "pusu",
    "initially": "pape",
    "initiative": "tozo",
    "injury": "tuvi",
    "inner": "soga",
    "innocent": "roni",
    "inquiry": "kogu",
    "inside": "pugi",
    "insight": "bibi",
    "insist": "bode",
    "inspire": "teve",
    "install": "nero",
    "instance": "pube",
    "institution": "doze",
    "institutional": "bamu",
    "instruction": "tura",
    "instructor": "muni",
    "instrument": "loli",
    "insurance": "soge",
    "intellectual": "rato",
    "intelligence": "dagu",
    "intend": "susa",
    "intense": "selu",
    "intensity": "gobu",
    "intention": "viva",
    "interaction": "deni",
    "interest": "maro",
    "interesting": "bode",
    "internal": "bare",
    "international": "pane",
    "Internet": "mezu",
    "interpret": "vama",
    "interpretation": "roze",
    "intervention": "sobi",
    "interview": "sova",
    "introduce": "nobu",
    "introduction": "rogi",
    "invasion": "zeba",
    "invest": "line",
    "investigate": "fofo",
    "investigation": "ruve",
    "investigator": "kazo",
    "investment": "kire",
    "investor": "nora",
    "invite": "deri",
    "involve": "dabe",
    "involved": "zuka",
    "involvement": "bulu",
    "Iraqi": "bige",
    "Irish": "zota",
    "iron": "ziro",
    "Islamic": "bone",
    "island": "vifa",
    "Israeli": "rolo",
    "issue": "betu",
    "Italian": "rase",
    "item": "zezo",
    "jail": "modo",
    "Japanese": "fare",
    "jet": "nuli",
    "Jew": "foga",
    "Jewish": "pado",
    "job": "pope",
    "joint": "puge",
    "journalist": "kofe",
    "judge": "fefi",
    "judgment": "suse",
    "juice": "sazi",
    "jump": "kipu",
    "junior": "kuda",
    "jury": "vizi",
    "justice": "kako",
    "justify": "kodo",
    "keep": "baru",
    "kick": "mefi",
    "kill": "kage",
    "killer": "dopa",
    "killing": "zusa",
    "king": "livo",
    "kiss": "zaba",
    "kitchen": "rise",
    "knee": "zanu",
    "knock": "sori",
    "knowledge": "dabi",
    "lab": "getu",
    "label": "bafi",
    "labor": "fomu",
    "laboratory": "sebo",
    "lack": "pefi",
    "lady": "dane",
    "land": "pefi",
    "landscape": "gonu",
    "language": "lobe",
    "lap": "geka",
    "largely": "rili",
    "Latin": "raki",
    "latter": "tebu",
    "laugh": "posi",
    "launch": "luke",
    "law": "sopi",
    "lawn": "sofi",
    "lawsuit": "moku",
    "lawyer": "solo",
    "lay": "toze",
    "layer": "fuma",
    "lead": "kope",
    "leader": "muru",
    "leadership": "puno",
    "leading": "pare",
    "lean": "zufi",
    "leather": "pege",
    "left": "kufo",
    "leg": "vefe",
    "legacy": "vuso",
    "legal": "pide",

    "yourself": "koki",
    "myself": "zasa",
    "himself": "ludu",
    "herself": "nomo",
    "itself": "faki",
    "ourselves": "sepu",
    "yourselves": "tila",
    "themselves": "rebi",
    "abuse": "pasa",
    "accommodate": "liki",
    "accumulate": "sezo",
    "acknowledge": "napa",
    "administer": "dalo",
    "advocate": "mami",
    "apologize": "bovi",
    "appear": "kali",
    "apply": "nino",
    "appoint": "napi",
    "appreciate": "fari",
    "approach": "pezu",
    "approve": "fari",
    "argue": "dega",
    "arise": "zivu",
    "arrange": "kazi",
    "arrest": "ruma",
    "arrive": "fini",
    "assess": "mofo",
    "assign": "kafu",
    "assist": "reni",
    "assume": "fenu",
    "assure": "mesa",
    "attach": "siru",
    "attack": "pinu",
    "attempt": "vami",
    "attend": "fape",
    "attract": "puva",
    "avoid": "zadu",
    "bake": "daki",
    "balance": "safi",
    "bang": "vezu",
    "bare": "mami",
    "base": "kodu",
    "bathe": "lafa",
    "beam": "binu",
    "bear": "bemo",
    "beat": "todo",
    "become": "bega",
    "beg": "miso",
    "begin": "suti",
    "behave": "dape",
    "believe": "toko",
    "bend": "geri",
    "benefit": "biko",
    "bet": "gadu",
    "betray": "kasi",
    "bind": "golu",
    "bite": "voku",
    "blame": "laro",
    "bleed": "zeta",
    "blend": "like",
    "bless": "mogi",
    "blink": "luvo",
    "blow": "kuke",
    "boast": "mapo",
    "boil": "divi",
    "bolt": "bogi",
    "bomb": "gadi",
    "boom": "maza",
    "boost": "lipi",
    "border": "pasu",
    "bore": "muli",
    "borrow": "pavu",
    "bother": "kifu",
    "bounce": "luri",
    "bow": "funo",
    "brake": "tevo",
    "branch": "tobo",
    "break": "koda",
    "breathe": "tupa",
    "breed": "zela",
    "bring": "nidu",
    "broadcast": "tula",
    "burn": "riru",
    "burst": "feva",
    "bury": "sova",
    "bust": "dozu",
    "calculate": "leda",
    "camp": "saza",
    "cancel": "tote",
    "capture": "sivu",
    "care": "pezi",
    "carry": "foru",
    "carve": "valo",
    "cast": "mame",
    "catch": "pigu",
    "cause": "safu",
    "celebrate": "nizi",
    "center": "magu",
    "challenge": "nati",
    "change": "muze",
    "characterize": "vati",
    "chase": "suko",
    "chat": "kafu",
    "cheat": "reno",
    "check": "doka",
    "cheer": "bosu",
    "chew": "page",
    "choose": "gemu",
    "chop": "bami",
    "claim": "feno",
    "clarify": "doso",
    "climb": "bafa",
    "cling": "noku",
    "collapse": "vunu",
    "collect": "kubu",
    "combine": "motu",
    "comfort": "depe",
    "command": "pide",
    "comment": "zidi",
    "commit": "zago",
    "communicate": "sogu",
    "compare": "beni",
    "compete": "veta",
    "complain": "vobe",
    "complete": "zosu",
    "complicate": "vesa",
    "compose": "kosi",
    "comprise": "kazo",
    "compromise": "kano",
    "conceal": "gega",
    "concentrate": "tabu",
    "concept": "pova",
    "concern": "fosi",
    "conclude": "zobe",
    "condemn": "limo",
    "conduct": "noga",
    "confess": "gisi",
    "confidence": "reri",
    "confirm": "kava",
    "confront": "vore",
    "confuse": "tabe",
    "connect": "bago",
    "conquer": "bole",
    "consent": "dola",
    "consider": "dona",
    "consist": "mise",
    "construct": "doti",
    "consume": "tafo",
    "contact": "ravu",
    "contain": "miza",
    "contend": "soba",
    "continue": "nesu",
    "contrast": "giru",
    "contribute": "buvu",
    "control": "siri",
    "convert": "gaba",
    "convey": "tore",
    "convince": "faze",
    "cooperate": "gane",
    "coordinate": "doki",
    "cope": "rile",
    "copy": "bopi",
    "corner": "lipu",
    "correct": "nusa",
    "correlate": "rore",
    "counsel": "raru",
    "cover": "zinu",
    "crack": "sonu",
    "crash": "tuzo",
    "crawl": "rosa",
    "credit": "visu",
    "creep": "diru",
    "criticize": "dali",
    "cross": "zopu",
    "crush": "puru",
    "cry": "pago",
    "curl": "savu",
    "curve": "tami",
    "cut": "geti",
    "cycle": "matu",
    "damage": "diso",
    "dare": "pefi",
    "dash": "gigo",
    "decay": "zemi",
    "decide": "budu",
    "declare": "name",
    "decline": "butu",
    "decorate": "mala",
    "decrease": "sole",
    "dedicate": "nura",
    "defeat": "dano",
    "defend": "sope",
    "define": "vopi",
    "delay": "nuzi",
    "delete": "bama",
    "deliver": "pizo",
    "demand": "zopo",
    "demonstrate": "lufu",
    "deny": "dizi",
    "depart": "nafu",
    "depend": "rege",
    "depict": "ponu",
    "depress": "gori",
    "derive": "biti",
    "describe": "pure",
    "deserve": "pose",
    "desire": "fadu",
    "destroy": "zole",
    "detect": "tapo",
    "determine": "vase",
    "develop": "kudu",
    "devise": "vufu",
    "devote": "vufa",
    "dictate": "dumu",
    "differ": "vako",
    "dig": "kone",
    "digest": "goge",
    "diminish": "petu",
    "direct": "nibo",
    "disagree": "nele",
    "disappear": "kaza",
    "disappoint": "mine",
    "disapprove": "lusa",
    "discard": "luse",
    "discharge": "tivo",
    "disclose": "pusu",
    "disconnect": "topo",
    "discover": "mofi",
    "discuss": "sefo",
    "dismiss": "simi",
    "display": "teka",
    "dispose": "solo",
    "dissolve": "mude",
    "distance": "rara",
    "distinguish": "gupo",
    "distort": "bulo",
    "distract": "defe",
    "distribute": "lomu",
    "disturb": "ruze",
    "dive": "setu",
    "divide": "pegi",
    "divorce": "rezo",
    "document": "dumi",
    "dominate": "zipa",
    "donate": "rome",
    "doubt": "raro",
    "draft": "tove",
    "drag": "dumi",
    "drain": "dobe",
    "dream": "bosi",
    "dress": "mume",
    "drift": "mogi",
    "drill": "bama",
    "drip": "modi",
    "drop": "momi",
    "drown": "rudu",
    "dump": "zose",
    "duty": "bafo",
    "earn": "zipu",
    "ease": "tosi",
    "echo": "taga",
    "edit": "more",
    "educate": "dupo",
    "effect": "debi",
    "elect": "riru",
    "eliminate": "pega",
    "embrace": "seso",
    "emerge": "dolu",
    "emphasize": "bisu",
    "employ": "rite",
    "enable": "fena",
    "enclose": "bezo",
    "encounter": "vipa",
    "encourage": "rado",
    "end": "zape",
    "endorse": "miga",
    "endure": "dule",
    "enforce": "fosu",
    "engage": "sovi",
    "enhance": "budo",
    "enjoy": "kebe",
    "enlarge": "mezo",
    "ensure": "tavi",
    "enter": "vuse",
    "entertain": "teto",
    "enthusiasm": "kuki",
    "entitle": "vanu",
    "entrance": "seve",
    "envelope": "poge",
    "environment": "tame",
    "equal": "paki",
    "equip": "mupo",
    "equivalent": "potu",
    "erase": "gisi",
    "escape": "rige",
    "establish": "siza",
    "estimate": "lime",
    "evaluate": "fono",
    "evidence": "sipu",
    "evolve": "rubi",
    "exact": "mila",
    "examine": "vofi",
    "exceed": "kani",
    "exchange": "peno",
    "excite": "kima",
    "exclude": "toto",
    "excuse": "nemu",
    "execute": "pubi",
    "exhaust": "saga",
    "exhibit": "legi",
    "exist": "niti",
    "expand": "bero",
    "expect": "zame",
    "experience": "tibu",
    "experiment": "sito",
    "expert": "topa",
    "explain": "nule",
    "explode": "pifi",
    "explore": "nutu",
    "export": "lase",
    "expose": "kamu",
    "express": "meba",
    "extend": "zune",
    "extra": "ginu",
    "extract": "kigu",
    "extreme": "vusa",
    "eye": "guzi",
    "face": "zavu",
    "facility": "nina",
    "factor": "fovu",
    "fail": "kepa",
    "failure": "sigu",
    "fair": "tudu",
    "faith": "dava",
    "fall": "dodi",
    "familiar": "kuve",
    "famous": "nupi",
    "fan": "duvo",
    "fantasy": "sezo",
    "farmer": "lade",
    "fashion": "vuse",
    "fat": "kevi",
    "fate": "memo",
    "father": "sege",
    "fault": "rilo",
    "favor": "rani",
    "favorite": "manu",
    "fear": "simo",
    "feature": "tiki",
    "fee": "pala",
    "feed": "pima",
    "feel": "tedo",
    "feeling": "dagi",
    "fellow": "raza",
    "female": "pagi",
    "fence": "rufu",
    "fiction": "sigi",
    "fierce": "sidu",
    "figure": "pode",
    "fill": "peka",
    "film": "tida",
    "final": "keso",
    "finance": "nebu",
    "financial": "meti",
    "fine": "foke",
    "finger": "gako",
    "finish": "raba",
    "fit": "safi",
    "flag": "vibo",
    "flash": "tode",
    "flat": "lizo",
    "flavor": "bala",
    "flee": "zako",
    "flesh": "nere",
    "float": "teba",
    "flow": "peku",
    "fly": "guna",
    "focus": "poro",
    "fold": "suti",
    "folk": "palo",
    "follow": "tite",
    "foot": "peto",
    "football": "redi",
    "force": "fasi",
    "foreign": "pota",
    "forever": "nabe",
    "forget": "peko",
    "forgive": "foko",
    "form": "fete",
    "formal": "bode",
    "format": "gudo",
    "former": "nufe",
    "formula": "fusi",
    "fortune": "zumu",
    "forward": "mili",
    "found": "lifu",
    "foundation": "vuka",
    "founder": "depa",
    "frame": "rodu",
    "framework": "buge",
    "freedom": "peku",
    "freeze": "mubi",
    "frequency": "tura",
    "frequent": "lefa",
    "friendly": "nevi",
    "friendship": "vito",
    "frighten": "vode",
    "frog": "gana",
    "front": "maku",
    "frustrate": "popa",
    "fuel": "zezo",
    "fun": "tase",
    "function": "mume",
    "fund": "simu",
    "fundamental": "soza",
    "funding": "gani",
    "funeral": "zake",
    "funny": "bilu",
    "furniture": "togo",
    "further": "gemi",
    "gain": "liri",
    "galaxy": "kani",
    "gallery": "nifi",
    "gang": "moma",
    "gap": "lumi",
    "garage": "furi",
    "garlic": "mupi",
    "gate": "nedo",
    "gather": "zuzu",
    "gay": "roku",
    "gaze": "kori",
    "gear": "sevu",
    "gender": "bama",
    "gene": "vezo",
    "general": "pire",
    "generate": "pefo",
    "generation": "reni",
    "genetic": "vuda",
    "gentleman": "sipe",
    "German": "bano",
    "gesture": "tede",
    "ghost": "mafa",
    "giant": "sofe",
    "gifted": "lido",
    "girl": "nomi",
    "girlfriend": "mudi",
    "given": "teni",
    "glance": "bizu",
    "global": "zuzo",
    "God": "beso",
    "golden": "lipi",
    "golf": "gifa",
    "government": "temu",
    "governor": "kofo",
    "grab": "lilu",
    "grade": "litu",
    "gradually": "rogu",
    "graduate": "luda",
    "grain": "kivo",
    "grand": "mozo",
    "grandfather": "gezi",
    "grandmother": "beso",
    "grant": "ruka",
    "grave": "bobo",
    "greatest": "lepi",
    "ground": "kobo",
    "grow": "gogu",
    "growing": "gote",
    "growth": "muto",
    "guarantee": "rule",
    "guard": "nemo",
    "guess": "kosu",
    "guest": "soza",
    "guide": "dafi",
    "guideline": "sobu",
    "guilty": "sego",
    "gun": "tigi",
    "habit": "mapo",
    "habitat": "peki",
    "hair": "sibu",
    "hall": "tetu",
    "hand": "gino",
    "handful": "vola",
    "handle": "pemo",
    "hang": "lema",
    "happen": "mife",
    "head": "nufi",
    "headline": "pise",
    "headquarters": "nazu",
    "hear": "koro",
    "hearing": "zulu",
    "heart": "nepi",
    "heaven": "suvu",
    "height": "pazu",
    "helicopter": "zabe",
    "helpful": "feta",
    "heritage": "mizu",
    "hero": "gebi",
    "herself": "nale",
    "hide": "dide",
    "highlight": "dake",
    "highly": "ponu",
    "highway": "dofa",
    "him": "bupu",
    "himself": "gako",
    "hire": "luko",
    "historian": "sizu",
    "historic": "zega",
    "historical": "vipa",
    "hit": "kobi",
    "hold": "beta",
    "hole": "zomi",
    "holy": "viro",
    "homeless": "goma",
    "honey": "gupu",
    "honor": "tasa",
    "hope": "gate",
    "horizon": "rebu",
    "horror": "sute",
    "host": "dome",
    "hotel": "vuvo",
    "household": "liso",
    "housing": "fusa",
    "human": "mamo",
    "humor": "tufi",
    "hungry": "turo",
    "hunter": "vesu",
    "hunting": "desu",
    "hurt": "vepi",

    "honestly": "diza",
    "abiding": "sovag",
    "absorbing": "rodaf",
    "absurd": "donam",
    "abundant": "putap",
    "accessible": "sorip",
    "accidental": "pibop",
    "accommodating": "sarez",
    "accomplished": "mesar",
    "aching": "vuzul",
    "acidic": "vizaz",
    "acoustic": "nukuk",
    "adaptable": "suvip",
    "addictive": "muful",
    "adept": "tafok",
    "admirable": "matut",
    "adorable": "sikub",
    "adventurous": "galam",
    "agonizing": "pirub",
    "agreeable": "mosum",
    "alien": "ramef",
    "alluring": "genes",
    "ambitious": "dagaf",
    "amiable": "nodiz",
    "ample": "lagel",
    "amused": "zitor",
    "amusing": "pepam",
    "angelic": "muvas",
    "animated": "gutas",
    "annoying": "mizez",
    "anxious": "vofas",
    "apathetic": "futeg",
    "appealing": "zazik",
    "appetizing": "vured",
    "appreciative": "dovam",
    "appropriate": "tarer",
    "arrogant": "lufez",
    "artistic": "gubuf",
    "ashamed": "megaf",
    "astonishing": "sopen",
    "athletic": "zopeg",
    "attractive": "pegem",
    "authentic": "fidad",
    "automatic": "lodaz",
    "available": "makos",
    "average": "luleg",
    "awake": "vasib",
    "aware": "nikum",
    "awesome": "lobib",
    "awful": "mepiz",
    "awkward": "serep",
    "babyish": "sukel",
    "barren": "fepos",
    "basic": "ganeg",
    "beautiful": "gakit",
    "believable": "fegen",
    "beneficial": "fipeb",
    "bizarre": "fosek",
    "blank": "popuv",
    "blazing": "pasiz",
    "blessed": "tarur",
    "blind": "terez",
    "blissful": "natup",
    "blonde": "debev",
    "bloody": "nigup",
    "boring": "luvel",
    "bossy": "gadon",
    "bouncy": "milad",
    "boundless": "nelet",
    "breezy": "netiv",
    "brief": "divim",
    "brilliant": "fogut",
    "broad": "bateb",
    "broken": "detur",
    "bumpy": "butod",
    "burly": "memud",
    "busy": "pavan",
    "candid": "zetav",
    "capable": "benor",
    "caring": "bases",
    "cautious": "rufuz",
    "ceaseless": "mabek",
    "certain": "bazuk",
    "charming": "tolaz",
    "cheerful": "nerad",
    "chilly": "rolim",
    "chubby": "sodot",
    "civil": "letiv",
    "classic": "togit",
    "clever": "bivel",
    "cloudy": "filuz",
    "clumsy": "polib",

    "properly": "dovav",
    "beautifully": "tafum",
    "perfectly": "dodor",
    "simply": "vufek",
    "merely": "tadaz",
    "just": "gafil",
    "even": "famug",
    "nearly": "pusom",
    "mostly": "ruvan",
    "fully": "nefir",
    "completely": "kesud",
    "entirely": "kazid",
    "totally": "nerom",
    "wholly": "rerag",
    "partially": "kifok",
    "partly": "tubas",
    "hardly": "besid",
    "scarcely": "vorat",
    "barely": "betel",
    "closely": "zukub",
    "roughly": "tidal",
    "smoothly": "gipuk",
    "softly": "mubef",
    "loudly": "darof",
    "quietly": "beliz",
    "silently": "siniv",
    "firmly": "vimun",
    "strongly": "samor",
    "weakly": "vuvam",
    "heavily": "zesiv",
    "lightly": "duzed",
    "deeply": "setil",
    "shallowly": "kutus",
    "widely": "purol",
    "narrowly": "bafog",
    "broadly": "zerug",
    "thickly": "ninit",
    "thinly": "dutif",
    "tightly": "dovof",
    "loosely": "vuvuk",
    "freely": "dumag",
    "strictly": "befit",
    "severely": "domuf",
    "harshly": "simol",
    "mildly": "dizod",
    "gently": "kagur",
    "kindly": "pebos",
    "cruelly": "kegaf",
    "badly": "kegul",
    "poorly": "fabot",
    "well": "mevil",
    "better": "zozug",
    "best": "deluv",
    "worse": "gumod",
    "worst": "zevuv",
    "far": "kafap",
    "high": "birum",
    "low": "gemom",
    "long": "redad",
    "short": "libep",
    "tall": "fatip",
    "large": "nobim",
    "great": "vapuv",
    "huge": "bukud",
    "tiny": "pagit",
    "heavy": "fumos",
    "dirty": "zivez",
    "stale": "fepik",
    "sour": "sozip",
    "bitter": "rofed",
    "salty": "vedaf",
    "spicy": "befok",
    "cool": "gakez",
    "dry": "fupet",
    "wet": "tusen",
    "damp": "robut",
    "humid": "muvez",
    "rough": "mibub",
    "solid": "niber",
    "liquid": "giker",
    "gas": "pofok",
    "empty": "tezag",
    "full": "gadip",
    "closed": "fison",
    "shut": "mutod",
    "locked": "litar",
    "unlocked": "reruf",
    "dangerous": "keruk",
    "secure": "sobas",
    "insecure": "fenas",
    "ill": "fuzen",
    "well": "vimed",
    "mad": "lagov",
    "glad": "kazev",
    "joyful": "nozeg",
    "sorrowful": "pibaz",
    "fearful": "surar",
    "brave": "zemis",
    "bold": "rerad",
    "shy": "vatam",
    "timid": "labap",
    "nervous": "mulak",
    "relaxed": "nopam",
    "tense": "karid",
    "excited": "tavoz",
    "bored": "budam",
    "interested": "venul",
    "curious": "ragad",
    "indifferent": "mukuz",
    "careless": "tudat",
    "thoughtful": "kapas",
    "thoughtless": "dezit",
    "selfish": "lukuz",
    "unselfish": "rorer",
    "generous": "somub",
    "greedy": "vepog",
    "stingy": "tadam",
    "dishonest": "lirad",
    "false": "duzib",
    "fake": "zazim",
    "genuine": "fagov",
    "artificial": "nuvig",
    "natural": "zovof",
    "unnatural": "pinav",
    "normal": "mosev",
    "abnormal": "derig",
    "strange": "zadak",
    "weird": "sifum",
    "odd": "susip",
    "unusual": "talel",
    "usual": "fafod",
    "common": "tiviv",
    "rare": "kotot",
    "unique": "nokeb",
    "single": "tulug",
    "multiple": "litez",
    "double": "fokes",
    "triple": "bafem",
    "half": "vukok",
    "whole": "pobol",
    "part": "buvib",
    "piece": "lolid",
    "slice": "darob",
    "chunk": "gapol",
    "block": "pireb",
    "pile": "rudom",
    "stack": "soder",
    "bunch": "navar",
    "crowd": "gafob",
    "mob": "tazup",
    "flock": "nakag",
    "herd": "zupuz",
    "pack": "danaz",
    "swarm": "kuget",
    "class": "pinil",
    "club": "tazem",
    "society": "fasot",
    "association": "dogol",
    "mill": "movom",
    "mine": "pabom",
    "ranch": "bezir",
    "garden": "burav",
    "park": "nirug",
    "jungle": "gimed",
    "desert": "kiran",
    "plain": "bugig",
    "field": "nuzel",
    "meadow": "netup",
    "pasture": "dosif",
    "cliff": "luzil",
    "soil": "rulir",
    "clay": "panan",
    "flame": "getik",
    "spark": "kevam",
    "heat": "nobef",
    "warmth": "roluv",
    "chill": "dunub",
    "frost": "dotod",
    "vapor": "zenap",
    "fog": "muson",
    "mist": "kimus",
    "dew": "mevil",
    "breeze": "misud",
    "hurricane": "sibas",
    "tornado": "kupep",
    "earthquake": "birak",
    "volcano": "vobek",
    "flood": "rofes",
    "drought": "zakun",
    "famine": "pubup",
    "tablet": "vetal",
    "capsule": "dirof",
    "injection": "tisar",
    "shot": "nizak",
    "vaccine": "seguf",
    "therapy": "ligaf",
    "surgery": "pitiv",
    "operation": "pubip",
    "dentist": "migup",
    "surgeon": "lavob",

    "abandoned": "zalu",
    "absorb": "vati",

    "abandon": "banir",
    "ability": "fovet",
    "able": "vole",
    "absent": "sopeb",
    "absolute": "bonom",
    "abstract": "kires",
    "academic": "biniv",
    "accept": "fakig",
    "acceptable": "razod",
    "access": "zubip",
    "accident": "zirin",
    "accompany": "selel",
    "accomplish": "lemub",
    "according": "valob",
    "accurate": "vegof",
    "accuse": "zimur",
    "achieve": "koret",
    "acquire": "sedas",
    "act": "fido",
    "action": "safud",
    "active": "petef",
    "activity": "kugul",
    "actor": "dosa",
    "actual": "komok",
    "adapt": "tudo",
    "add": "zoso",
    "addition": "fifek",
    "additional": "vesob",
    "address": "fekev",
    "adequate": "pokek",
    "adjust": "pited",
    "administration": "relov",
    "administrator": "lubod",
    "admire": "tumuz",
    "admit": "pupa",
    "adopt": "dova",
    "adult": "vove",
    "advance": "tidun",
    "advanced": "bituf",
    "advantage": "radiv",
    "adventure": "porez",
    "advertising": "tagit",
    "advice": "vumur",
    "advise": "valol",
    "affair": "gikat",
    "affect": "vibuk",
    "afford": "dimip",
    "afraid": "borub",
    "age": "pedu",
    "agency": "nonek",
    "agent": "kesu",
    "aggressive": "felog",
    "ago": "gefu",
    "agree": "fimo",
    "ahead": "bori",
    "aid": "doni",
    "aim": "ranu",
    "air": "dufo",
    "aircraft": "melan",
    "airline": "leses",
    "album": "piku",
    "alcohol": "depef",
    "alive": "nami",
    "allow": "gaki",
    "ally": "vava",
    "alone": "sula",
    "along": "soro",
    "alter": "befa",
    "alternative": "dusov",
    "AM": "nilu",
    "amazing": "medur",
    "American": "dokez",
    "amount": "zosit",
    "analysis": "gipum",
    "analyst": "furar",
    "analyze": "tebiz",
    "ancient": "bebop",
    "anger": "difi",
    "angle": "bume",
    "angry": "tedu",
    "anniversary": "bimaz",
    "announce": "doriz",
    "annual": "rokor",
    "another": "fafor",
    "anticipate": "gogen",
    "anxiety": "laziv",
    "anybody": "bunad",
    "apartment": "badav",
    "apparent": "vupev",
    "apparently": "liret",
    "appeal": "zudel",

    "anymore": "keval",
    "others": "pokaz",
    "something": "zorur",
    "everything": "tezeb",
    "nothing": "bagem",
    "anything": "zovit",
    "someone": "vazev",
    "anyone": "finop",
    "no one": "ruvat",
    "anywhere": "bukov",
    "somehow": "mazef",
    "anyhow": "goziv",
    "someday": "gosog",
    "anyway": "lofig",
    "besides": "nerig",
    "instead": "zoken",
    "however": "nolof",
    "although": "libaf",
    "though": "nivaf",
    "unless": "rogak",
    "while": "zapun",
    "above": "fevut",
    "below": "talor",
    "among": "kirel",
    "across": "guror",
    "against": "lebov",
    "within": "ziran",
    "behind": "tunob",
    "beyond": "gotop",
    "beside": "lasev",
    "beneath": "midag",
    "upon": "bevu",
    "into": "dizi",
    "onto": "mose",
    "toward": "topiv",
    "towards": "damef",
    "around": "sasen",
    "almost": "kuteb",
    "together": "mekod",
    "apart": "dezam",
    "away": "teso",
    "back": "vusu",
    "forth": "feled",
    "which": "disen",
    "whom": "kebu",
    "whose": "linid",
    "such": "kiza",
    "much": "bido",
    "little": "sovub",
    "several": "dutit",
    "enough": "miges",
    "too": "kosi",
    "quite": "pamap",
    "rather": "fuveb",
    "somewhat": "ruriv",
    "truly": "tizek",
    "actually": "defep",
    "exactly": "kalug",
    "absolutely": "fagez",
    "certainly": "darep",
    "definitely": "fevak",
    "probably": "dovar",
    "possibly": "bifep",
    "maybe": "rorap",
    "perhaps": "bidit",
    "suddenly": "bazap",
    "quickly": "pagop",
    "slowly": "levek",
    "carefully": "marof",
    "easily": "repaz",
    "finally": "remol",
    "especially": "furos",
    "generally": "dadep",
    "seldom": "tored",
    "frequently": "nazuv",
    "recently": "nemor",
    "lately": "retef",
    "tonight": "kumez",
    "monday": "desob",
    "tuesday": "fugil",
    "wednesday": "rifol",
    "thursday": "toden",
    "friday": "pedap",
    "saturday": "pazel",
    "sunday": "danom",
    "january": "pamek",
    "february": "nifiz",
    "march": "toduz",
    "april": "gupop",
    "june": "poki",
    "july": "pine",
    "august": "nokig",
    "september": "dirit",
    "october": "ruzat",
    "november": "napaf",
    "december": "femok",
    "spring": "vagop",
    "summer": "dofof",
    "autumn": "foter",
    "winter": "pusis",
    "season": "zenum",
    "millennium": "dedud",
    "history": "niliz",
    "future": "nitel",
    "past": "zami",
    "present": "varek",
    "diary": "demom",
    "journal": "lezut",
    "schedule": "nazav",
    "meeting": "bavev",
    "event": "govil",
    "party": "mevim",
    "celebration": "gipov",
    "holiday": "bopev",
    "vacation": "nipaz",
    "trip": "tipa",
    "journey": "fadon",
    "tour": "dosi",
    "flight": "zogon",
    "passport": "lanaf",
    "visa": "motu",
    "luggage": "befal",
    "baggage": "zesig",
    "suitcase": "gosiz",
    "backpack": "serek",
    "purse": "nanov",
    "cash": "lepa",
    "coin": "degu",
    "card": "guki",
    "bank": "beso",
    "account": "zozig",
    "cost": "gobe",
    "value": "roped",
    "tax": "redu",
    "bill": "rolu",
    "invoice": "pukem",
    "payment": "lufat",
    "salary": "gagis",
    "wage": "fitu",
    "income": "gikod",
    "profit": "kotit",
    "loss": "dupa",
    "debt": "zuku",
    "loan": "meri",
    "mortgage": "moreb",
    "rent": "mone",
    "lease": "navad",
    "contract": "mumud",
    "agreement": "saper",
    "deal": "noma",
    "offer": "tutuf",
    "discount": "fogud",
    "sale": "kiro",
    "store": "sunif",
    "mall": "vebu",
    "supermarket": "malin",
    "grocery": "falen",
    "bakery": "zuzod",
    "butcher": "nuzuv",
    "hospital": "lebel",
    "nurse": "madet",
    "patient": "zakod",
    "pill": "fifo",
    "drug": "vumi",
    "prescription": "busuk",
    "treatment": "zigog",
    "cure": "zebi",
    "disease": "nerop",
    "illness": "zubot",
    "sickness": "bibok",
    "fitness": "sagod",
    "exercise": "kubaz",
    "workout": "kuzez",
    "gym": "guma",
    "sport": "vumip",
    "match": "zokeg",
    "team": "bura",
    "player": "kigal",
    "coach": "tuluf",
    "referee": "rukak",
    "umpire": "kimov",
    "score": "kinap",
    "point": "turib",
    "draw": "lufa",
    "champion": "tezuv",
    "tournament": "tinub",
    "league": "titog",
    "medal": "binos",
    "trophy": "duzib",
    "prize": "zuzar",
    "award": "bugad",
    "reward": "zuloz",
    "gift": "togi",
    "surprise": "gegog",
    "secret": "tofum",
    "mystery": "refag",
    "puzzle": "rulut",
    "riddle": "bikat",
    "joke": "pili",
    "tale": "litu",
    "fable": "gonug",
    "myth": "ligo",
    "legend": "ronip",
    "news": "mefe",
    "information": "vigiz",
    "data": "samo",
    "fact": "vonu",
    "lie": "mosi",
    "rumor": "vepan",
    "gossip": "silip",
    "conversation": "sorep",
    "discussion": "tupel",
    "debate": "linuv",
    "argument": "ranas",
    "dispute": "mupek",
    "conflict": "gefip",
    "fight": "gozur",
    "battle": "nolop",
    "war": "fapo",
    "peace": "sesan",
    "treaty": "muton",
    "alliance": "serip",
    "union": "renas",
    "organization": "momek",
    "company": "ganor",
    "business": "rudor",
    "corporation": "vufiz",
    "firm": "koso",
    "industry": "natat",
    "factory": "mosez",
    "machine": "bapuf",

    "everybody": "evali",
    "everyone": "evali",
    "did": "doraa",
    "animal": "rifut",
    "cake": "dize",
    "floor": "naseb",
    "wall": "divo",
    "ceiling": "gasol",
    "roof": "zomo",
    "street": "semum",
    "town": "karu",
    "village": "namis",
    "country": "sugek",
    "planet": "galug",
    "cloud": "fedik",
    "snow": "puni",
    "storm": "kopeg",
    "flower": "sulad",
    "leaf": "ziro",
    "plant": "revep",
    "forest": "zarug",
    "lake": "vure",
    "ocean": "masun",
    "hill": "tuda",
    "valley": "vadik",
    "rock": "zonu",
    "stone": "lakiz",
    "sand": "kunu",
    "dirt": "sume",
    "dust": "zupo",
    "mud": "rima",
    "ice": "mofa",
    "steam": "podan",
    "smoke": "tukum",
    "ash": "bafe",
    "metal": "sorum",
    "wood": "nelo",
    "plastic": "mubup",
    "pencil": "bozib",
    "notebook": "lubok",
    "desk": "susu",
    "screen": "bizav",
    "keyboard": "vekuk",
    "mouse": "logan",
    "cable": "kurib",
    "battery": "malom",
    "bulb": "dolo",
    "switch": "guzob",
    "plug": "piro",
    "socket": "gatob",
    "wire": "desa",
    "boat": "beve",
    "wheel": "vokit",
    "engine": "runon",
    "motor": "kubup",
    "ticket": "bupug",
    "station": "kesos",
    "airport": "pigor",
    "port": "zigi",
    "bridge": "fopap",
    "tunnel": "kikug",
    "path": "nedo",
    "track": "mokor",
    "map": "kaka",
    "compass": "zanir",
    "basket": "fibus",
    "bottle": "nopit",
    "cup": "mano",
    "plate": "terad",
    "bowl": "lado",
    "fork": "papo",
    "knife": "mokos",
    "spoon": "fasiv",
    "pan": "paso",
    "pot": "mego",
    "oven": "tuvi",
    "stove": "tesiv",
    "fridge": "rarok",
    "sink": "pane",
    "soap": "fane",
    "towel": "semib",
    "brush": "mekud",
    "comb": "kodi",
    "razor": "mitur",
    "scissors": "gifok",
    "needle": "zukam",
    "thread": "difop",
    "cloth": "fidik",
    "clothes": "todaz",
    "shirt": "guber",
    "pants": "rodud",
    "shoe": "kova",
    "sock": "tufi",
    "coat": "bedo",
    "jacket": "bokaz",
    "glove": "fifom",
    "scarf": "renif",
    "belt": "tiru",
    "tie": "mebu",
    "ring": "mutu",
    "clock": "zubab",
    "calendar": "pelag",
    "second": "zeden",
    "minute": "zufiz",
    "hour": "riso",
    "day": "zaba",
    "week": "tovo",
    "month": "nomuv",
    "year": "kefa",
    "decade": "vupad",
    "century": "gipev",
    "noon": "zibi",
    "midnight": "lutib",
    "soon": "fomi",
    "late": "gitu",
    "always": "ravit",
    "never": "palut",
    "sometimes": "lotez",
    "often": "zigup",
    "rarely": "ganof",
    "usually": "gunos",
    "yet": "kune",
    "once": "nola",
    "twice": "ravas",
    "first": "silez",
    "third": "ritum",
    "last": "novo",
    "next": "tezi",
    "previous": "morim",
    "number": "voped",
    "count": "kunug",
    "math": "dala",

    "belong": "bela",
    "say": "sai",
    "study": "suma",
    "learn": "luma",
    "teach": "tava",
    "work": "vora",
    "play": "pali",
    "take": "naka",
    "get": "gava",
    "make": "maka",
    "do": "dora",
    "build": "buna",
    "fix": "fira",
    "open": "opa",
    "close": "kloa",
    "start": "sira",
    "stop": "soto",
    "like": "liri",
    "love": "loma",
    "hate": "hata",
    "want": "wena",
    "need": "neda",
    "look": "luka",
    "watch": "wata",
    "tell": "tela",
    "let": "jova",
    "ask": "asu",
    "answer": "anisa",
    "call": "kala",
    "join": "jona",
    "leave": "leva",
    "sell": "sela",
    "pay": "paya",
    "use": "uza",
    "try": "tira",
    "find": "fina",
    "so": "soa",
    "other": "odra",
    "lose": "losa",
    "win": "wina",
    "live": "liva",
    "die": "dai",
    "must": "musu",
    "should": "shuda",
    "may": "meya",
    "therefore": "sona",
    "if": "iva",
    "because": "beka",
    "then": "dana",
    "also": "alsa",
    "on": "ona",
    "at": "ata",
    "for": "fora",
    "through": "thura",
    "over": "ovra",
    "now": "nau",
    "after": "afra",
    "hundred": "huna",
    "all": "ala",
    "every": "eva",
    "only": "ono",
    "good": "guda",
    "bad": "bada",
    "new": "niva",
    "old": "oda",
    "hot": "hota",
    "cold": "koda",
    "fast": "fasa",
    "slow": "sloa",
    "same": "sama",
    "easy": "eza",
    "hard": "hara",
    "happy": "hapi",
    "sad": "sada",
    "doctor": "doka",
    "teacher": "taver",
    "learner": "lumer",
    "friend": "fali",
    "man": "mava",
    "woman": "woma",
    "child": "kidi",
    "family": "fama",
    "bread": "breda",
    "egg": "ega",
    "meat": "mita",
    "apple": "apa",
    "banana": "bana",
    "coffee": "kafa",
    "room": "ruma",
    "door": "dora n",
    "window": "wina n",
    "table": "taba",
    "chair": "chara",
    "lamp": "lampa",
    "book": "buka",
    "paper": "papa",
    "glass": "gala",
    "train": "tiren",
    "airplane": "avion",
    "road": "roda",
    "computer": "koma",
    "internet": "neta",
    "video": "vida",
    "game": "gama",
    "moon": "luna",
    "star": "sila",
    "rain": "raina",
    "wind": "vayu",
    "tree": "tira n",
    "grass": "gresa",
    "river": "riva",
    "mountain": "monda",
    "horse": "hosa",
    "time": "tima",
    "life": "lifa",
    "death": "deta",
    "joy": "joa",
    "happiness": "hapnes",
    "problem": "noro",
    "question": "kesa",
    "idea": "ida",
    "truth": "trua",
    "to be": "be",
    "my": "mai",
    "your": "tai",
    "his": "lihi",
    "her": "lisi",
    "its": "liti",
    "our": "mui",
    "their": "lui",
    "soft": "siva",
    "market": "mara",
    "price": "prisa",
    "smile": "simi",
    "city": "siti",
    "quiet": "quira",
    "story": "stori",
    "word": "wora",
    "meaning": "mina",
    "clear": "kira",
    "sentence": "seni",
    "board": "boda",
    "voice": "voa",
    "world": "wolda",
    "color": "kolo",
    "black": "naru",
    "white": "vela",
    "red": "ruba",
    "blue": "sanu",
    "green": "mira",
    "yellow": "yela",
    "orange": "oran",
    "purple": "pura",
    "pink": "pina",
    "brown": "brona",
    "gray": "gora",
    "gold": "zola",
    "silver": "sivamet",
    "violet": "viola",
    "cyan": "sian",
    "teal": "tila",
    "turquoise": "turka",
    "magenta": "magena",
    "maroon": "maru",
    "navy": "navi",
    "beige": "beja",
    "cream": "krema",
    "tan": "tana",
    "olive": "oliva",
    "lime": "lima",
    "indigo": "inda",
    "lavender": "lavena",
    "coral": "kora",
    "bronze": "bronza",
    "copper": "kopra",
    "charcoal": "charko",
    "ivory": "ivora",
    "crimson": "krima",
    "scarlet": "skara",
    "amber": "amba",
    "aqua": "akwa",
    "forehead": "forha",
    "eyebrow": "browa",
    "eyelash": "lasha",
    "eyelid": "lida",
    "pupil": "pupila",
    "iris": "irisa",
    "nostril": "nosra",
    "jaw": "jawa",
    "beard": "berda",
    "mustache": "musta",
    "wrist": "rista",
    "forearm": "foram",
    "upper arm": "upam",
    "armpit": "ampita",
    "rib": "riba",
    "spine": "spina",
    "hip": "hipa",
    "thigh": "thaia",
    "calf": "kalfa",
    "heel": "hela",
    "sole": "solafoot",
    "toenail": "tonela",
    "fingernail": "fingela",
    "knuckle": "nukla",
    "vein": "vena",
    "nerve": "nerva",
    "organ": "orga",
    "liver": "livera",
    "kidney": "kidna",
    "medicine": "medina",
    "fever": "fevra",
    "cough": "kofa",
    "cold illness": "kodasik",
    "allergy": "alerga",
    "bandage": "banda",
    "clinic": "klinika",
    "pharmacy": "farma",
    "toilet": "toila",
    "toothbrush": "tuthbrus",
    "toothpaste": "tuthpas",
    "shampoo": "shampa",
    "deodorant": "deoda",
    "mirror": "miragla",
    "wallet": "wala",
    "receipt": "resita",
    "appointment": "aponta",
    "medicine pill": "medinapil",
    "please": "pli",
    "sorry": "sori",
    "excuse me": "emi",
    "goodbye": "bai",
    "welcome": "weli",
    "you are welcome": "ta weli",
    "thank you": "tia",
    "good morning": "guda morn",
    "good night": "guda nit",
    "see you": "sena ta",
    "I do not know": "mi na ni",
    "for real": "fre",
    "in my opinion": "imo n",
    "to be honest": "tbo",
    "laugh out loud": "lal",
    "idk": "nin",
    "lol": "lal",
    "omg": "oma",
    "np": "nop",
    "bro": "brg",
    "dude": "vori",
    "guy": "voru",
    "fuck": "fk",
    "shit": "zako",
    "damn": "bren",
    "hell": "norg",
    "ass": "aza",
    "crap": "kopo",
    "idiot": "bafu",
    "stupid": "dulo",
    "crazy": "zani",
    "nigger": "negr",
    "insane": "mado",
    "sick": "zika",
    "fire": "falo",
    "lit": "laza",
    "goat": "beso",
    "vibe": "vibu",
    "cap": "fala",
    "flex": "sho",
    "clout": "klautu",
    "easy": "eza",
    "bag": "bago",
    "bed": "beda",
    "bird": "vori",
    "box": "boko",
    "buy": "baya",
    "few": "fewa",
    "key": "kiva",
    "pen": "penu",
    "see": "sena",
    "ship": "shiva",
    "weak": "weka",
})


SECTIONS = {
    "Core Grammar": """
above across act action activity add address adult afraid age agree air almost alone along already always amount animal another area argue around arrive art ask avoid away back base basic beautiful become bed before begin behind believe below best better body both bring business busy by care carry case center chance change city class clean clear close common company compare complete condition continue control cook cost could country course cover create current cut daily dance dark data date day deal decide deep describe design detail develop die different difficult direct discover discuss distance divide dog draw dream drive drop each early earth east easy edge education effect effort either else end energy enjoy enough enter even event ever exact example expect explain face fact fall family famous far farm fast father feel feeling field fight figure file fill final finally finance find fine finish fire firm first fish floor focus follow food foot force form free friend front full future game garden general get girl give glass go goal good government great green ground group grow guess half hand happen happy hard have head health hear heart heavy help here high history hit hold home hope hospital hot hotel hour house human hundred husband idea if image important include increase indeed industry information inside instead interest into issue item job join just keep kid kind kitchen know land language large last late later laugh law lead learn leave left leg less letter level lie life light like likely line list listen little live local long look lose lot love low machine main make man manage many market matter may maybe me mean measure meet member memory mention message middle might mind minute miss model modern moment money month more morning mother mountain move movie much music must name nation natural near need network never new next nice night north note nothing notice number office often oil old once one only open order other outside over own page pain paper parent part particular pass past pay peace people per perfect perhaps person phone pick picture piece place plan plant play point police policy position possible power practice prepare present president price private probably problem process produce product program project property protect prove provide public pull purpose push put quality question quickly quite race radio raise range rate rather reach read ready real reason receive recent record red reduce remain remember report represent require research rest result return rich right rise risk road room rule run safe same save say school science sea season seat second section see seem sell send sense serve service set several share she short should show side sign similar simple since sing single sister sit site situation skill small social society some someone something sometimes son song soon sort sound source south space speak special specific speech spend spring stand standard star start state stay step still stop story strategy street strong student study subject success such suffer suggest summer support sure system table take talk task teach teacher team technology tell term test than thank that the their them then theory there these they thing think this those though thought thousand threat three through time today together total town trade travel treat tree trip true try turn two understand unit until up upon us use usually value various very view visit voice wait walk want war watch water way we week weight well west what whatever when where whether which while white who whole whom whose why wide wife will win wind window wish with within without woman wonder word work world worry would write wrong year yes yet you young your
""",
    "People and Society": """
account actor actress adviser agent ally artist assistant athlete author aunt barber boss boy bride brother captain cashier citizen coach colleague community cousin crowd customer daughter dentist director driver elder employee enemy engineer expert fan farmer father guest hero husband judge king lawyer leader manager mayor member mother neighbor nurse officer owner parent partner passenger patient player poet president prince princess professor queen relative reporter resident scientist singer sister soldier stranger student surgeon teen uncle visitor volunteer worker writer
""",
    "Home and Daily Life": """
apartment attic balcony basement bathroom bedroom blanket bowl broom cabinet candle carpet ceiling closet couch counter curtain desk dish drawer elevator entrance fence floor fork garage gate hall hammer handle heater home kitchen ladder lock mirror napkin needle oven pan pillow plate pot roof shelf shower sink soap spoon stairs stove towel wall wardrobe yard toilet toothbrush toothpaste shampoo deodorant remote outlet plug charger trash laundry basket detergent sponge bucket mop freezer refrigerator microwave
""",
    "Food and Drink": """
almond beef beer berry biscuit breakfast butter cake candy carrot cheese chicken chocolate cinnamon cookie corn cream dinner flour grape honey juice lemon lunch mango meal milk noodle nut oil onion orange pasta pepper pie pizza potato salt sandwich sauce soup spice sugar tomato wine yogurt cereal toast salad bean pea cucumber lettuce garlic mushroom pork turkey shrimp snack dessert
""",
    "Body and Health": """
ankle arm back blood bone brain breath cheek chest chin ear elbow eye face finger hair hand headache heart knee leg lip lung mouth muscle neck nose pain palm shoulder skin stomach throat thumb toe tooth tongue waist wound forehead eyebrow eyelash eyelid pupil iris nostril jaw beard mustache wrist forearm armpit rib spine hip thigh calf heel sole toenail fingernail knuckle vein nerve organ liver kidney medicine fever cough allergy bandage clinic pharmacy pill
""",
    "Nature and Weather": """
beach branch breeze cloud coast desert dust field fire flower fog forest hill island lake leaf lightning mud ocean path planet rock root sand sky snow soil stone storm stream valley wave weather wood
""",
    "Movement and Travel": """
airport arrive boat brake bridge camp carry climb cross depart direction drive engine flight harbor hotel journey map mile move park passport path port ride route station ticket traffic travel truck tunnel vehicle wheel
""",
    "Work and School": """
assignment board calendar campus certificate chart classroom client college contract deadline department document essay exam grade homework invoice lesson library meeting note office project report schedule school skill software task tool training university
""",
    "Technology and Media": """
app audio battery browser camera channel charger chat code database download email file folder image keyboard laptop link login media message microphone mouse network password photo podcast printer profile screen search server tablet text upload website refresh host blank github tab option setting menu button form input output error bug update save load reload publish deploy repository branch page cache browser history local storage custom sync
""",
    "Money and Shopping": """
bank bill budget cash coin cost credit debt discount dollar fee gift income market price purchase rent sale saving shop store tax trade wallet receipt refund coupon checkout aisle cart basket appointment
""",
    "Requested Words": """
scary others swear curse promise vow creepy spooky ghost monster fear terrifying
""",
    "Time and Calendar": """
April August December February Friday January July June March Monday November October Saturday September Sunday Thursday Tuesday Wednesday century decade holiday minute moment month noon season second spring summer sunrise sunset week weekend winter year
""",
    "Feelings and Qualities": """
able angry awake calm careful clever comfortable confident cool curious cute dangerous dead dear dry empty fair false familiar fresh funny gentle glad healthy honest ill jealous kind lazy lonely loud lucky nervous normal open patient poor proud quiet rare rich serious sharp sick soft sweet tired useful warm wet wild wise wrong boring smooth effective efficient random repeated blank custom advanced basic
""",
    "Actions": """
accept achieve add admit affect allow apply argue bake become begin borrow break breathe bring brush burn catch change choose clean collect compare complain cook count cover cry cut dance deliver draw dress drop earn enter erase escape explain fail feed feel finish fold grow hide hit hold hope hurt improve invite jump kick kill kiss lift mark marry mix notice offer pass prefer press pull push repair repeat replace save share shine shout sign sleep smile spend stand stay steal throw touch train turn understand visit wash wear
""",
    "Abstract and Civic": """
ability accident advice agreement attention balance behavior belief benefit cause choice culture danger decision difference duty economy education election emotion evidence freedom future habit history honor influence knowledge law meaning method nature order permission power reason relationship responsibility right safety secret society success value
""",
    "Directions and Shapes": """
angle back bottom circle corner east edge front inside left line middle north outside point rectangle right round side south square straight top triangle west
""",
    "Colors": """
black white red blue green yellow orange purple pink brown gray gold silver violet cyan teal turquoise magenta maroon navy beige cream tan olive lime indigo lavender coral bronze copper charcoal ivory crimson scarlet amber aqua color dark light bright pale
""",
    "Everyday Expanded": """
adapter agenda alarm album alphabet ambulance anchor announcement apron aquarium architect archive argument armor arrow article backpack badge bakery balloon banner bargain basket bathrobe battery blanket blender bookmark booth bracelet brake brand brush calculator campground capsule cardboard carton checkout clipboard collar comb complaint container coupon coworker crate cushion diary envelope eraser extension faucet flashlight freezer glue hallway headline helmet hoodie identity instruction jacket journal kettle label landmark leaflet locker luggage magnet mailbox manual marker mattress menu microscope napkin necklace notebook outlet package parcel parking perfume poster receipt recycling remote ribbon scale scissors screwdriver shampoo shortcut signature suitcase sunscreen survey sweater switch tape thermometer timer toothbrush toothpaste towel umbrella uniform vacuum wallet warranty whistle zipper
""",
    "Common Actions Expanded": """
apologize arrange balance bend blink boil breathe cancel celebrate chase chew clap copy crawl decorate delay delete deliver describe dial dig dip drag edit enter fold fry gather grab greet hang heat imagine improve inspect introduce knock measure mention nod pack peel pour promise recycle remind remove rent rinse roll rub scan scratch select separate shake sign skip squeeze stir stretch tap taste tie toss unlock unpack wipe wrap yawn
""",
    "Common Qualities Expanded": """
accurate bitter bland brave brief broken central cheap clean cloudy crowded deep distant dusty electric equal fancy flexible gentle giant grateful hollow huge hungry noisy polite powerful rainy regular shiny silent sour spicy sticky tiny useful visible weekly wooden
""",
    "Clothing and Personal Items": """
belt blouse boot bracelet button cap coat dress glove hat hoodie jacket jeans necklace pajamas pocket ring scarf shirt shorts skirt sneaker sock suit sweater swimsuit tie uniform zipper
""",
    "City and Places": """
bank bakery bridge cafe cinema clinic courthouse factory gallery gym harbor intersection museum neighborhood pharmacy playground restaurant sidewalk stadium subway supermarket theater tower village warehouse
""",
    "Communication": """
accent advice announcement apology argument comment conversation debate explanation gossip grammar instruction invitation joke language meaning opinion promise reply request rumor translation warning whisper
""",
    "Hobbies and Culture": """
band camera concert craft drawing festival guitar hobby instrument museum painting piano poem recipe sport theater ticket violin
""",
    "Common Life Additions": """
absence access achievement advertisement agreement airline allowance alternative analysis anniversary anxiety appearance appliance application approval arrival assignment assistant background backup behavior boundary breakfast cabinet candidate ceremony charity childhood circumstance collection combination competition concentration conclusion conference confidence confusion connection consequence construction contribution cooperation criticism database definition delivery departure description device difficulty direction disaster discovery discussion distribution drawer editor efficiency emergency employee employer entrance environment equipment estimate event evidence expression failure feature feedback friendship grocery guidance headache household imagination improvement independence information ingredient inspection instance insurance interview introduction invitation judgment leadership maintenance manager membership memory message negotiation obligation operation opportunity organization partnership payment performance personality possession preference preparation presentation priority procedure profession protection recommendation reference relationship replacement requirement reservation resource responsibility restaurant satisfaction selection signature situation solution statement storage subscription suggestion temperature tradition transaction transportation treatment variation version weakness website
""",
    "Everyday Verbs Additions": """
achieve advise afford announce approve attach belong borrow bother calculate complain confirm connect consider continue convince damage depend deserve disagree disappear encourage forgive ignore inform install interrupt manage organize permit postpone prefer prevent recommend recover refuse register relax remind reply reserve retire review solve subscribe succeed suppose surprise translate trust upgrade
""",
    "Objects Additions": """
backpack badge bookmark cable candle charger coaster controller curtain envelope folder frame headphones keyboard ladder microphone monitor notebook pillow plug poster receipt router speaker suitcase tablet toolbox tripod wallet
""",
    "Food Additions": """
avocado bacon bean broccoli burger cabbage cereal cucumber garlic lettuce mushroom oatmeal pancake peach pear pickle salad sausage shrimp spinach steak toast tuna vanilla waffle
""",
    "Body Additions": """
appetite bladder eyebrow eyelash eyelid forehead hormone intestine joint knuckle ligament nostril pulse skull tendon toenail vein wrist
""",
}


COLOR_WORDS = {
    "black", "white", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "gray",
    "gold", "silver", "violet", "cyan", "teal", "turquoise", "magenta", "maroon", "navy", "beige",
    "cream", "tan", "olive", "lime", "indigo", "lavender", "coral", "bronze", "copper", "charcoal",
    "ivory", "crimson", "scarlet", "amber", "aqua", "color",
}

BODY_WORDS = {
    "forehead", "eyebrow", "eyelash", "eyelid", "pupil", "iris", "nostril", "jaw", "beard",
    "mustache", "wrist", "forearm", "upper arm", "armpit", "rib", "spine", "hip", "thigh",
    "calf", "heel", "sole", "toenail", "fingernail", "knuckle", "vein", "nerve", "organ",
    "liver", "kidney", "medicine", "fever", "cough", "cold illness", "allergy", "bandage",
    "clinic", "pharmacy", "medicine pill",
}

ACTION_WORDS = {
    "say", "study", "learn", "teach", "work", "play", "take", "get", "make", "do", "build",
    "fix", "open", "close", "start", "stop", "like", "love", "hate", "want", "need", "look",
    "watch", "tell", "ask", "answer", "call", "join", "leave", "sell", "pay", "use", "try",
    "find", "lose", "win", "live", "die", "see", "buy",
}

HOME_WORDS = {
    "toilet", "toothbrush", "toothpaste", "shampoo", "deodorant", "mirror", "wallet", "receipt",
    "appointment",
}

SLANG_WORDS = {
    "bro", "dude", "guy",
    "fuck", "shit", "damn", "hell", "ass", "crap", "dickhead", "piss", "loser",
    "idiot", "stupid", "crazy", "insane",
    "sick", "fire", "lit", "goat", "cap", "flex",
    "lol", "omg", "np", "idk",
    "laugh out loud", "for real", "in my opinion", "to be honest",
    "good morning", "good night", "see you", "I do not know",
    "easy", "nigger"
}

def official_category(english: str) -> str:
    key = english.lower()
    if key in SLANG_WORDS:
        return "Slang and Swear Words"
    if key in COLOR_WORDS:
        return "Colors"
    if key in BODY_WORDS:
        return "Body and Health"
    if key in ACTION_WORDS:
        return "Common Verbs"
    if key in HOME_WORDS:
        return "Home and Daily Life"
    if key in {"my", "your", "his", "her", "its", "our", "their"}:
        return "Possessives"
    if key in {"to be"}:
        return "Grammar Aliases"
    return "Official Core"


DERIVED_VERBS = {
    "teach",
    "learn",
    "work",
    "play",
    "write",
    "read",
    "drive",
    "cook",
    "build",
    "help",
    "clean",
    "paint",
    "sing",
    "dance",
    "run",
    "swim",
    "study",
    "manage",
    "create",
    "design",
    "research",
    "farm",
    "shop",
    "search",
    "print",
    "charge",
    "travel",
    "protect",
    "serve",
    "record",
    "report",
}


DERIVED_ADJECTIVES = {
    "happy",
    "sad",
    "kind",
    "careful",
    "useful",
    "safe",
    "dark",
    "light",
    "warm",
    "cold",
    "strong",
    "weak",
    "honest",
    "quiet",
    "loud",
    "bright",
    "fresh",
    "sweet",
    "sharp",
    "soft",
    "free",
    "clear",
    "calm",
    "proud",
    "healthy",
    "lucky",
}


COMPOUNDS = {
    "rain jacket": ("rainjak", "clothing"),
    "sun glasses": ("solgala", "clothing"),
    "video call": ("vidakala", "technology"),
    "online book": ("netabuka", "technology"),
    "phone charger": ("telzuma", "technology"),
    "school bag": ("skulbag", "school"),
    "coffee cup": ("kafakup", "food"),
    "water bottle": ("venbotel", "food"),
    "work day": ("voraday", "time"),
    "home town": ("domtown", "place"),
    "story book": ("stori buka", "media"),
    "night sky": ("nit sky", "nature"),
    "sea wind": ("sea wind", "nature"),
    "city road": ("siti road", "travel"),
    "market price": ("maraprisa", "money"),
    "family name": ("famnam", "people"),
    "heart beat": ("hartbit", "body"),
    "first aid": ("firsted", "health"),
    "ice cream": ("aisukrem", "food"),
    "busstation": ("busstation", "travel"),
}


GRAMMAR = """==================================================
NARI v1.2
POLISHED OFFICIAL GRAMMAR

STATUS

This grammar keeps the core structure stable.
The main update is cleaner wording, fewer word collisions,
a less English-looking vocabulary, and a simple translator.

Golden Rule:

If the meaning is clear,
the sentence is correct.

==================================================
0. DESIGN PHILOSOPHY

Nari exists for:

* fast communication
* easy learning
* easy speaking
* easy typing
* minimal grammar
* global usability

Prefer short, direct sentences.

==================================================
1. ALPHABET

Core vowels:

a e i o u

Core consonants:

b d f g h j k l m n p r s t v w y z

Common clusters:

br dr sl th sh ch

Rules:

* no silent letters
* one sound = one spelling where possible
* write words as spoken
* capital letters are optional

==================================================
2. SENTENCE ORDER

Standard order:

subject + verb + object

mi mo mek.

I eat food.

ta re buka.

You read a book.

lu pla gam.

They play games.

==================================================
3. PRONOUNS

mi = I
ta = you
li = person
lih = he
lis = she
lit = it
mu = we
lu = they

Examples:

lih be dok.

He is a doctor.

lis be taver.

She is a teacher.

lit be kar.

It is a car.

==================================================
4. POSSESSION

ov = of

buka ov mi

my book

dom ov mu

our house

Short possessive pronouns:

mai = my
tai = your
lihi = his
lisi = her
liti = its
mui = our
lui = their

mai buka

my book

mui dom

our house

Possession verb:

su = have

mi su tel.

I have a phone.

Ownership:

bel = belong

tel bel mi.

The phone belongs to me.

==================================================
5. VERBS

Verbs never change for person or number.

be = to be / am / is / are

mi be al dom.

I am at home.

ko = go

mi ko
ta ko
lih ko
lu ko

There is no conjugation.

==================================================
6. TENSES

Present:

verb

Past:

verb + a

Future:

verb + u

Examples:

mi ko dom.

I go home.

mi koa dom.

I went home.

mi kou dom.

I will go home.

==================================================
7. CONTINUOUS ACTION

du = currently

mi du mo.

I am eating.

lis du re.

She is reading.

Past:

mi du moa.

I was eating.

Future:

mi du mou.

I will be eating.

==================================================
8. NEGATION

na comes before the verb.

mi na ko.

I do not go.

ta na ni.

You do not know.

==================================================
9. QUESTIONS

Keep normal sentence order and add ?.

ta su tel?

Do you have a phone?

lih ko dom?

Is he going home?

==================================================
10. QUESTION WORDS

wt = what
hu = who
wer = where
wen = when
wai = why
hou = how

wt ta mo?

What are you eating?

wer lis be?

Where is she?

==================================================
11. MODALS

kan = can
mus = must
shud = should
may = may

mi kan ko.

I can go.

ta musu suma.

You must study.

==================================================
12. SERIAL VERBS

Multiple verbs can stand together.
The first action usually happens before the second.

mi ko mo.

I go eat.

mi la hel ta.

I come help you.

lu ko buna dom.

They go build a house.

==================================================
13. EXISTENCE

ex = there is / there are

ex ven.

There is water.

ex tri kat.

There are three cats.

na ex mek.

There is no food.

==================================================
14. DEMONSTRATIVES

dis = this
dat = that
dese = these
dose = those

dis buka

this book

dat kar

that car

==================================================
15. ADJECTIVES

Adjectives come before nouns.

guda fali

good friend

bi dom

big house

==================================================
16. MODIFIER ORDER

quantity + adjective + noun

tri bi kat

three big cats

all guda fali

all good friends

sum niva buka

some new books

==================================================
17. COMPARISON

mor = more
les = less
mos = most
lest = least

dis kar mor fasa.

This car is faster.

dat dom mos bi.

That house is biggest.

==================================================
18. RELATION WORDS

al = in
on = on
un = under
at = at
tu = to
fram = from
ne = near
wit = with
no = without
ab = about
for = for
thru = through
ova = over
bit = between

==================================================
19. LOCATION WORDS

hir = here
der = there
som = somewhere
evr = everywhere
noh = nowhere

==================================================
20. TIME WORDS

ted = today
yesd = yesterday
tomd = tomorrow
now = now
morn = morning
aft = afternoon
eve = evening
nit = night
ear = early
lat = later

==================================================
21. TIME RELATIONS

bef = before
afta = after
dur = during
unt = until
sin = since

mi mo bef vora.

I eat before work.

mi bo afta mek.

I walk after food.

==================================================
22. CONNECTORS

e = and
o = or
bat = but
so = therefore
if = if
bec = because
wen = when
den = then

==================================================
23. CLAUSES

dat = that

mi ni dat lih be guda.

I know that he is good.

lis th dat ta kou la.

She thinks that you will come.

==================================================
24. RELATIVE CLAUSES

dat can also mean who, which, or that.

man dat ra

the man who speaks

buka dat mi re

the book that I read

==================================================
25. NUMBERS

0 nul
1 un
2 du
3 tri
4 for
5 fin
6 sis
7 sev
8 et
9 nin
10 ten

11 ten-un
12 ten-du
20 du-ten
30 tri-ten
100 hun
1000 mil

==================================================
26. QUANTIFIERS

ala = all
sum = some
ani = any
eve = every
multi = many
few = few

==================================================
27. PLURALS

Plural marking is optional.
Numbers and context usually make quantity clear.

tri kat

three cats

multi buka

many books

==================================================
28. COMMANDS

Use the verb alone.

ko!

Go!

la!

Come!

wa!

Wait!

==================================================
29. AGREEMENT

Nothing agrees.

Verbs, adjectives, and nouns do not change for number,
gender, or person.

==================================================
30. ARTICLES

There are no articles.

kat can mean:

cat
a cat
the cat

Context decides.

==================================================
31. WORD CREATION

Official derivation:

-er = person
-in = tool/object
-nes = state/quality
-ing = action/concept
-ful = full of
-les = without

How to read this:

Start with a root.
Add one ending.
Do not change the root.

Examples:

tava = teach
taver = teacher
luma = learn
lumer = learner
hap = happy
hapnes = happiness
homles = homeless

Use compounds when an ending would feel unclear.

==================================================
32. COMPOUND WORDS

Compounds are preferred for practical vocabulary.

sol + gala = solgala

sunglasses

rain + jak = rainjak

rain jacket

vida + kala = vidakala

video call

==================================================
33. INFORMAL SPEECH

hei = hello
ye = yes
nu = no
oya = okay
tia = thanks
pli = please
sori = sorry
emi = excuse me
bai = goodbye
weli = welcome

==================================================
34. INTERNET SLANG

oma = oh my god
oga = on god
fre = for real
nin = I do not know
tbo = to be honest
imo-n = in my opinion
gug = good game
eza = easy
nop = no problem
lal = laugh out loud
bru = disbelief
ripa = unfortunate
brg = bro
fk = fuck

==================================================
35. PUNCTUATION

. statement
? question
! emphasis

==================================================
36. AMBIGUITY RULE

Simple form is preferred.
If detail matters, add detail.

li be taver.

The teacher is there.

lih be taver.

The male teacher is there.

lis be taver.

The female teacher is there.

==================================================
37. OFFICIAL STYLE

Preferred sentences are short, clear, and direct.

mi na ni.

I do not know.

mi kou la tomd.

I will come tomorrow.

Avoid unnecessary complexity.

==================================================
38. EXTRA USAGE NOTES

Names:

Names do not need translation.

mi be Sara.

I am Sara.

Emphasis:

Use veri before an adjective.

dis mek be veri guda.

This food is very good.

Polite requests:

Use shuda or may for softer speech.

ta shuda hel mi?

Could you help me?

Lists:

Use e between the final two items.

mi su ven, breda, e kafa.

I have water, bread, and coffee.

Unknown words:

If a word is missing, make a compound first.
If the compound is unclear, use the English name temporarily.

==================================================
39. FINAL RULE

Grammar is stable.
Vocabulary grows.
Simple beats complicated.
If communication succeeds, Nari succeeds.

==================================================
END OF NARI v1.2
"""


STORIES = [
    {
        "title": "Morn al Dom",
        "translation": "Morning at Home",
        "nari": [
            "Morn be siva e ven be hota.",
            "Mi opa wina n e sena sol ovra tira n.",
            "Lis maka kafa e mi maka breda.",
            "Mu mo al sm taba, dana mu ko vora.",
        ],
        "english": [
            "The morning is soft and the water is hot.",
            "I open the window and see the sun over the trees.",
            "She makes coffee and I make bread.",
            "We eat at the small table, then we go to work.",
        ],
    },
    {
        "title": "Fri al Market",
        "translation": "Friends at the Market",
        "nari": [
            "Ta e mi ko mara afra vora.",
            "Ex multi frut, breda, tisa, e kafa.",
            "Ta asa prisa ov apa.",
            "Sela-er simi e giv du apa tu ta.",
        ],
        "english": [
            "You and I go to the market after work.",
            "There are many fruits, bread, tea, and coffee.",
            "You ask the price of apples.",
            "The seller smiles and gives two apples to you.",
        ],
    },
    {
        "title": "Nit Sky",
        "translation": "Night Sky",
        "nari": [
            "Nit la e siti be quira.",
            "Mu bo ne riva e luka ata luna.",
            "Lu ra ab oda stori ov sea.",
            "Mi th dat wolda be bi, bat dom be hir.",
        ],
        "english": [
            "Night comes and the city is quiet.",
            "We walk near the river and look at the moon.",
            "They speak about old stories of the sea.",
            "I think the world is big, but home is here.",
        ],
    },
    {
        "title": "New Ler-er",
        "translation": "The New Learner",
        "nari": [
            "Kidi wena luma Nari beka wora be eza.",
            "Taver wri tri seni ona boda.",
            "Kidi re, ra, e anisa wit guda voa.",
            "Taver sai, \"iva mina be kira, seni be guda.\"",
        ],
        "english": [
            "The child wants to learn Nari because the words are easy.",
            "The teacher writes three sentences on the board.",
            "The child reads, speaks, and answers with a good voice.",
            "The teacher says, \"if the meaning is clear, the sentence is good.\"",
        ],
    },
    {
        "title": "Kano e Kato",
        "translation": "The Dog and the Cat",
        "nari": [
            "Kano be bi e kato be sm.",
            "Kano pala vi kato.",
            "Lisi mo mek e si ven.",
            "Lisi be guda fri.",
        ],
        "english": [
            "The dog is big and the cat is small.",
            "The dog plays with the cat.",
            "They eat food and drink water.",
            "They are good friends.",
        ],
    },
    {
        "title": "Skula Day",
        "translation": "School Day",
        "nari": [
            "Kidi ko al skula.",
            "Taver re buka.",
            "Kidi wri wora.",
            "Lis be guda day.",
        ],
        "english": [
            "The child goes to school.",
            "The teacher reads a book.",
            "The child writes words.",
            "It is a good day.",
        ],
    },
    {
        "title": "Rain",
        "translation": "Rain",
        "nari": [
            "Skai be dara.",
            "Rain fla ona dom.",
            "Mi be insa dom.",
            "Mi wena rain.",
        ],
        "english": [
            "The sky is dark.",
            "Rain falls on the house.",
            "I am inside the house.",
            "I like the rain.",
        ],
    },
]


LESSONS = [
    {
        "title": "Basics",
        "goal": "Build simple subject + verb + object sentences.",
        "rules": [
            "Use subject + verb + object.",
            "Nari verbs do not change for I, you, he, she, we, or they.",
            "Questions keep the same order and add a question mark.",
        ],
        "examples": [
            ["mi mo mek.", "I eat food."],
            ["ta re buka?", "Do you read a book?"],
            ["lu pala gama.", "They play a game."],
        ],
        "drills": [
            {"prompt": "Translate: I eat food", "answer": "mi mo mek"},
            {"prompt": "Translate: you read a book", "answer": "ta re buka"},
            {"prompt": "Translate: they play a game", "answer": "lu pala gama"},
        ],
    },
    {
        "title": "To Be",
        "goal": "Use be for am, is, are, and to be.",
        "rules": [
            "be means to be, am, is, or are.",
            "Past uses bea. Future uses beu.",
            "Use al dom for at home.",
        ],
        "examples": [
            ["mi be al dom.", "I am at home."],
            ["lis be taver.", "She is a teacher."],
            ["lu bea hir.", "They were here."],
        ],
        "drills": [
            {"prompt": "Translate: I am at home", "answer": "mi be al dom"},
            {"prompt": "Translate: she is a teacher", "answer": "lis be taver"},
            {"prompt": "Translate: they were here", "answer": "lu bea hir"},
        ],
    },
    {
        "title": "Possession",
        "goal": "Choose fast possessive pronouns or clear ov phrases.",
        "rules": [
            "Use mai, tai, mui, and lui before nouns for my, your, our, and their.",
            "Use ov when you want the literal meaning of of.",
            "Use su for have, not for my or your.",
        ],
        "examples": [
            ["mai buka", "my book"],
            ["tai dom", "your house"],
            ["buka ov mi", "book of me"],
        ],
        "drills": [
            {"prompt": "Translate: my book", "answer": "mai buka"},
            {"prompt": "Translate: your house", "answer": "tai dom"},
            {"prompt": "Translate: book of me", "answer": "buka ov mi"},
        ],
    },
    {
        "title": "Body",
        "goal": "Practice common body and health words.",
        "rules": [
            "Body words work like normal nouns.",
            "Pain can follow the body part.",
            "Use su for have symptoms.",
        ],
        "examples": [
            ["mi su dramlon.", "I have a headache."],
            ["mi su pain al rista.", "I have pain in my wrist."],
            ["lis su fevra.", "She has a fever."],
        ],
        "drills": [
            {"prompt": "Translate to Nari: wrist", "answer": "rista"},
            {"prompt": "Translate to Nari: eyebrow", "answer": "browa"},
            {"prompt": "Translate: I have a fever", "answer": "mi su fevra"},
        ],
    },
    {
        "title": "Colors",
        "goal": "Describe things with common color words.",
        "rules": [
            "Adjectives come before nouns.",
            "Color words act like adjectives.",
            "The noun does not change.",
        ],
        "examples": [
            ["sanu buka", "blue book"],
            ["ruba kar", "red car"],
            ["turka dor", "turquoise door"],
        ],
        "drills": [
            {"prompt": "Translate to Nari: blue", "answer": "sanu"},
            {"prompt": "Translate: red car", "answer": "ruba kar"},
            {"prompt": "Translate: turquoise door", "answer": "turka dor"},
        ],
    },
]


ADVANCED_TEXTS = [
    {
        "title": "Siti afta Rain",
        "lines": [
            "Rain stopa, bat road stil wet e sanu lait shine ona glas ov shop.",
            "Multi li la fram station, su bago, tel, e sm plan for nit.",
            "Mi bo slow thru siti bec air be koda e fresh.",
            "At kora ov road, oda mava ra dat tomd kou be mor guda.",
            "Mi na ni if lih be right, bat mi liri hou siti liva afta storm.",
        ],
    },
    {
        "title": "Klinika Morn",
        "lines": [
            "Taver ov health asa mi ab pain al rista e dramlon.",
            "Mi say dat pain starta yesd dur vora.",
            "Lis giv banda e medina-pil, den wri nota ona papa.",
            "Mi musu rest unt nit e dri multi ven.",
            "Afta dat, mi kou la bak if fevra na stop.",
        ],
    },
    {
        "title": "Lesson ov Sea",
        "lines": [
            "Oda teer ra ab sea, vayu, e star dat help ship fina road.",
            "Kid lis na ask quick kesa; lis wri word first e th long.",
            "Den lis say dat language be olsem map: sm sign, bi meaning.",
            "Mu re stori no transal, bec mind musu wer wit Nari direct.",
            "Afta lesson, all fri ra sm, bat ra be clear.",
        ],
    },
    {
        "title": "Oda Siti Wal",
        "lines": [
            "Ston ov oda siti wal tela log histo.",
            "Multi li bila lisi ovra han yer.",
            "Toda, kidi pala ne gata.",
            "Pasa e futa liva toge hir.",
        ],
    },
    {
        "title": "Trva Ovra Monta",
        "lines": [
            "Monta be hi e air be tin.",
            "Trava-li musu be sro e kera heva bago.",
            "Ven lisi rica top, vue be beuta.",
            "Lisi foga lisii pain ven lisi si vala.",
        ],
    },
    {
        "title": "Luma Niva Lan",
        "lines": [
            "Luma niva lan opa dor to niva wolda.",
            "At firs, wora be stra e difa.",
            "Bat vi tim e paca, unda grou.",
            "Sun, ta kan ra vi niva fri.",
        ],
    },
]


MID_STORIES = [
    {
        "title": "Mara Day",
        "lines": [
            "Mi e ta ko mara afra morn.",
            "Mu baya apa, breda, e kafa.",
            "Sel-er simi bec mu ra Nari.",
            "Afta mara, mu bo al dom e mo mek.",
        ],
    },
    {
        "title": "New Buka",
        "lines": [
            "Lis su niva buka ona taba.",
            "Buka be sm, bat stori be guda.",
            "Lis re ona nit e wri tri nota.",
            "Tomd lis kou ra ab buka wit fri.",
        ],
    },
    {
        "title": "Pain al Rista",
        "lines": [
            "Mi du vora multi e rista starta pain.",
            "Taver ov health say mi musu rest.",
            "Mi su banda e medinapil.",
            "Afta du day, rista be mor guda.",
        ],
    },
    {
        "title": "Losa Buka",
        "lines": [
            "Mi na kan fina mai buka.",
            "Mi luka unra taba.",
            "Mai fri si buka ona cera.",
            "Mi be hapa to re.",
        ],
    },
    {
        "title": "Maka Mek",
        "lines": [
            "Mu maka mek for mui fri.",
            "Mu kuta vege e mita.",
            "Mek be hota e guda.",
            "Mu mo toge.",
        ],
    },
    {
        "title": "Log Bo",
        "lines": [
            "Road be log e sol be hota.",
            "Lisi bo ne riva to giva ven.",
            "Lisi sita unra tira to rest.",
            "Evna be koda.",
        ],
    },
]


def simplify_word(english: str) -> str:
    raw = english.lower().strip()
    if raw in {k.lower(): v for k, v in OFFICIAL.items()}:
        lookup = {k.lower(): v for k, v in OFFICIAL.items()}
        return lookup[raw]
    word = raw.replace("&", " and ")
    word = re.sub(r"[^a-z0-9 ]+", " ", word)
    parts = [simplify_single(part) for part in word.split() if part]
    return "-".join(parts)


def simplify_single(word: str) -> str:
    clean = re.sub(r"[^a-z0-9]", "", word.lower())
    if not clean:
        return "na"

    onsets = ["", "b", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "z", "br", "dr", "sl", "th"]
    vowels = ["a", "e", "i", "o", "u"]
    codas = ["", "", "", "l", "m", "n", "r", "s"]
    digest = hashlib.sha1(clean.encode("utf-8")).digest()
    syllable_count = 2 if len(clean) <= 6 else 3
    syllables = []
    for index in range(syllable_count):
        a = digest[index * 3]
        b = digest[index * 3 + 1]
        c = digest[index * 3 + 2]
        syllables.append(onsets[a % len(onsets)] + vowels[b % len(vowels)] + codas[c % len(codas)])
    out = "".join(syllables)
    if out[0] not in "aeiou" and len(out) > 7:
        out = out[:7]
    return out


def add_entry(
    entries: dict[str, dict[str, str]],
    english: str,
    category: str,
    nari: str | None = None,
    allow_duplicate_nari: bool = False,
) -> None:
    english = " ".join(english.strip().split())
    if not english:
        return
    key = english.lower()
    if key in entries:
        return
    base = nari or simplify_word(english)
    base = base.replace("-", "")
    candidate = base
    used = {entry["nari"] for entry in entries.values()}
    if candidate in used and not allow_duplicate_nari:
        stem = re.sub(r"[^a-z0-9]", "", category.lower())[:3] or "x"
        index = 2
        candidate = f"{base}{stem}"
        while candidate in used:
            index += 1
            candidate = f"{base}{stem}{index}"
    entries[key] = {"english": english, "nari": candidate, "category": category}


def build_entries() -> list[dict[str, str]]:
    entries: dict[str, dict[str, str]] = {}
    for english, nari in OFFICIAL.items():
        add_entry(entries, english, official_category(english), nari, allow_duplicate_nari=english in {"to be"})
    for category, words in SECTIONS.items():
        for word in words.split():
            add_entry(entries, word, category)
    for english, (nari, category) in COMPOUNDS.items():
        add_entry(entries, english, category.title(), nari)
    for verb in DERIVED_VERBS:
        root = simplify_word(verb)
        add_entry(entries, f"{verb} person", "Derived People", f"{root}er")
        add_entry(entries, f"{verb} tool", "Derived Tools", f"{root}in")
        add_entry(entries, f"{verb} action", "Derived Actions", f"{root}ing")
    for adj in DERIVED_ADJECTIVES:
        root = simplify_word(adj)
        add_entry(entries, f"{adj} state", "Derived Qualities", f"{root}nes")
        add_entry(entries, f"{adj} full", "Derived Qualities", f"{root}ful")
        add_entry(entries, f"{adj} without", "Derived Qualities", f"{root}les")
    sorted_entries = sorted(entries.values(), key=lambda row: (row["category"], row["english"]))
    return sorted_entries


def write_vocabulary(entries: list[dict[str, str]]) -> None:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for entry in entries:
        grouped[entry["category"]].append(entry)
    lines = [
        "NARI EXPANDED VOCABULARY",
        "",
        f"Total entries: {len(entries)}",
        "",
        "Format: Nari = English",
        "",
        "Notes:",
        "* v1.2 keeps the grammar simple and makes vocabulary less English-looking.",
        "* tea the drink is tisa, and teacher is taver.",
        "* sun the star is sol, and morning is morn.",
        "",
    ]
    for category in sorted(grouped):
        lines.append(f"=== {category.upper()} ===")
        lines.append("")
        for entry in sorted(grouped[category], key=lambda row: row["english"]):
            lines.append(f"{entry['nari']} = {entry['english']}")
        lines.append("")
    (ROOT / "vocabulary.txt").write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def write_grammar() -> None:
    (ROOT / "grammar.txt").write_text(GRAMMAR, encoding="utf-8")



def write_data(entries: list[dict[str, str]]) -> None:
    payload = {
        "entryCount": len(entries),
        "entries": entries,
        "stories": STORIES,
        "midStories": MID_STORIES,
        "lessons": LESSONS,
        "advancedTexts": ADVANCED_TEXTS,
            }
    js = "window.NARI_DATA = " + json.dumps(payload, indent=2, ensure_ascii=True) + ";\n"
    (ROOT / "nari-data.js").write_text(js, encoding="utf-8")


def write_html() -> None:
    html_doc = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Nari Language</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <video class="backdrop-video" src="background.mp4" autoplay muted loop playsinline></video>
  <div class="backdrop-tint"></div>

  <header class="shell site-header">
    <a class="brand" href="#top" aria-label="Nari home">
      <span class="brand-mark">N</span>
      <span>Nari</span>
    </a>
    <nav class="nav-links" aria-label="Primary navigation">
      <a href="#home" data-tab-link="home">Home</a>
      <a href="#translator" data-tab-link="translator">Translator</a>
      <a href="#practice" data-tab-link="practice">Practice</a>
      <a href="#stories" data-tab-link="stories">Stories</a>
      <a href="#grammar" data-tab-link="grammar">Rules</a>
      <a href="#vocabulary" data-tab-link="vocabulary">Vocabulary</a>
    </nav>
  </header>

  <main id="top">

    <section id="home" class="section tab-panel">

      <!-- HERO -->
      <div class="hp-hero">
        <div class="hp-hero-glow"></div>
        <div class="hp-hero-inner shell">
          <p class="eyebrow">Constructed language</p>
          <h1 class="hp-title">Nari</h1>
          <p class="hp-lede">A minimal, logical language built for speed.&nbsp;Learn it in an afternoon &mdash; speak it forever.</p>
          <div class="hp-cta-row">
            <button class="button primary hp-btn" type="button" onclick="goTab('translator')">Start Translating</button>
            <button class="button secondary hp-btn" type="button" onclick="goTab('grammar')">Grammar Guide</button>
          </div>
          <div class="hp-stats-inline">
            <div class="hp-stat-inline">
              <strong id="wordCount">3188</strong>
              <span>words</span>
            </div>
            <div class="hp-stat-divider"></div>
            <div class="hp-stat-inline">
              <strong>13</strong>
              <span>grammar cards</span>
            </div>
            <div class="hp-stat-divider"></div>
            <div class="hp-stat-inline">
              <strong>3</strong>
              <span>tenses</span>
            </div>
          </div>
        </div>
      </div>

      <!-- QUICK TRANSLATE -->
      <div class="hp-section">
        <div class="shell">
          <div class="hp-block glass-panel">
            <div class="hp-block-header">
              <div>
                <p class="eyebrow">Try it now</p>
                <h2 class="hp-block-title">Quick translate</h2>
              </div>
              <button class="button secondary" type="button" onclick="goTab('translator')">Full translator &rarr;</button>
            </div>
            <div class="hp-translate-row">
              <div class="hp-translate-side">
                <label class="hp-translate-label">English</label>
                <input id="homeTranslateInput" class="hp-translate-input" type="text" placeholder="e.g. I go home tomorrow" autocomplete="off" oninput="homeTranslate(this.value)">
              </div>
              <div class="hp-translate-arrow-col">&#8594;</div>
              <div class="hp-translate-side">
                <label class="hp-translate-label">Nari</label>
                <div id="homeTranslateOutput" class="hp-translate-output">Translation appears here</div>
              </div>
            </div>
            <div class="hp-translate-hint">Unknown words are skipped. Regular plurals (dogs, cats) work automatically.</div>
          </div>
        </div>
      </div>

      <!-- GRAMMAR SNEAK PEEK -->
      <div class="hp-section">
        <div class="shell">
          <div class="hp-section-head">
            <div>
              <p class="eyebrow">Grammar at a glance</p>
              <h2 class="hp-section-title">Core patterns</h2>
            </div>
            <button class="button secondary" type="button" onclick="goTab('grammar')">See all rules &rarr;</button>
          </div>
          <div class="hp-grammar-grid">
            <div class="glass-panel hp-grammar-card">
              <div class="hp-grammar-pill">Sentence order</div>
              <div class="hp-grammar-example"><span class="nari">mi mo mek.</span></div>
              <div class="hp-grammar-gloss">I eat food &mdash; subject + verb + object</div>
            </div>
            <div class="glass-panel hp-grammar-card">
              <div class="hp-grammar-pill">Past tense</div>
              <div class="hp-grammar-example"><span class="nari">mi koa.</span></div>
              <div class="hp-grammar-gloss">I went &mdash; add <strong>a</strong> to verb</div>
            </div>
            <div class="glass-panel hp-grammar-card">
              <div class="hp-grammar-pill">Future tense</div>
              <div class="hp-grammar-example"><span class="nari">mi kou.</span></div>
              <div class="hp-grammar-gloss">I will go &mdash; add <strong>u</strong> to verb</div>
            </div>
            <div class="glass-panel hp-grammar-card">
              <div class="hp-grammar-pill">Negation</div>
              <div class="hp-grammar-example"><span class="nari">mi na ni.</span></div>
              <div class="hp-grammar-gloss">I don&apos;t know &mdash; <strong>na</strong> before verb</div>
            </div>
            <div class="glass-panel hp-grammar-card">
              <div class="hp-grammar-pill">Question</div>
              <div class="hp-grammar-example"><span class="nari">ta ko?</span></div>
              <div class="hp-grammar-gloss">Are you going? &mdash; same order, add ?</div>
            </div>
            <div class="glass-panel hp-grammar-card">
              <div class="hp-grammar-pill">Possession</div>
              <div class="hp-grammar-example"><span class="nari">mai buka.</span></div>
              <div class="hp-grammar-gloss">My book &mdash; possessive before noun</div>
            </div>
          </div>
        </div>
      </div>

      <!-- FEATURE CARDS -->
      <div class="hp-section hp-section-dark">
        <div class="shell">
          <div class="hp-section-head">
            <div>
              <p class="eyebrow">Explore</p>
              <h2 class="hp-section-title">Everything in one place</h2>
            </div>
          </div>
          <div class="hp-features">
            <article class="hp-feature-card" onclick="goTab('vocabulary')">
              <div class="hp-feature-top">
                <span class="hp-feature-icon">&#128218;</span>
                <span class="hp-feature-arrow">&rarr;</span>
              </div>
              <h3>Vocabulary</h3>
              <p>Browse 3000+ words across dozens of categories. Search, filter, and explore.</p>
            </article>
            <article class="hp-feature-card" onclick="goTab('practice')">
              <div class="hp-feature-top">
                <span class="hp-feature-icon">&#127919;</span>
                <span class="hp-feature-arrow">&rarr;</span>
              </div>
              <h3>Practice</h3>
              <p>Flashcards, translation drills, and word match games to sharpen your skills.</p>
            </article>
            <article class="hp-feature-card" onclick="goTab('stories')">
              <div class="hp-feature-top">
                <span class="hp-feature-icon">&#128214;</span>
                <span class="hp-feature-arrow">&rarr;</span>
              </div>
              <h3>Stories</h3>
              <p>Read short stories at easy, mid, and hard difficulty levels.</p>
            </article>
            <article class="hp-feature-card" onclick="goTab('translator')">
              <div class="hp-feature-top">
                <span class="hp-feature-icon">&#9889;</span>
                <span class="hp-feature-arrow">&rarr;</span>
              </div>
              <h3>Translator</h3>
              <p>Full English &#8596; Nari translator with tense, plural and grammar detection.</p>
            </article>
          </div>
        </div>
      </div>

    </section>

    <section id="translator" class="section shell tab-panel">
      <div class="section-heading">
        <div>
          <p class="eyebrow">Translator</p>
          <h2>Move between English and Nari</h2>
        </div>
        <div class="direction-toggle glass-panel" role="group" aria-label="Translation direction">
          <button class="direction-button is-active" type="button" data-direction="en-nari">English to Nari</button>
          <button class="direction-button" type="button" data-direction="nari-en">Nari to English</button>
        </div>
      </div>
      <div class="translator-grid">
        <label class="translator-box glass-panel">
          <span id="sourceLabel">English</span>
          <textarea id="translatorInput" rows="8" placeholder="Type a sentence like: I want coffee after work."></textarea>
        </label>
        <div class="translator-output glass-panel" aria-live="polite">
          <span id="targetLabel">Nari</span>
          <p id="translatorOutput">mi wena kafa afra vora.</p>
          <p id="translatorHint">The translator uses the vocabulary list and leaves unknown words marked with a dot.</p>
        </div>
      </div>
    </section>

    <section id="practice" class="section shell tab-panel">
      <div class="section-heading">
        <div>
          <p class="eyebrow">Practice</p>
          <h2>Train Nari</h2>
        </div>
        <div class="practice-mode-tabs glass-panel" role="group" aria-label="Practice mode">
          <button class="practice-mode-tab is-active" type="button" data-practice-tab="drill">Translation</button>
          <button class="practice-mode-tab" type="button" data-practice-tab="cloze">Cloze</button>
          <button class="practice-mode-tab" type="button" data-practice-tab="choice">Multiple Choice</button>
          <button class="practice-mode-tab" type="button" data-practice-tab="match">Word Match</button>
          <button class="practice-mode-tab" type="button" data-practice-tab="build">Builder</button>
        </div>
      </div>

      <div id="drillPanel" class="practice-mode-panel is-active">
        <div class="practice-layout">
          <article class="practice-card glass-panel">
            <p id="drillMode" class="eyebrow">Translation drill</p>
            <h3 id="drillPrompt">Translate: my book</h3>
            <label class="practice-answer">
              <span>Your answer</span>
              <input id="drillAnswer" type="text" autocomplete="off" placeholder="Type your answer">
            </label>
            <div class="practice-actions">
              <button id="checkDrill" class="button primary" type="button">Check</button>
              <button id="nextDrill" class="button secondary" type="button">Skip</button>
              <p id="drillFeedback">Use the trainer to practice grammar and vocabulary.</p>
            </div>
          </article>
          <aside class="practice-card glass-panel">
            <p class="eyebrow">Drill Types</p>
            <ul class="practice-list">
              <li>English → Nari translation</li>
              <li>Nari → English translation</li>
              <li>Grammar &amp; tense drills</li>
              <li>Vocabulary recall by category</li>
            </ul>
          </aside>
        </div>
      </div>

      <div id="clozePanel" class="practice-mode-panel">
        <div class="cloze-card glass-panel">
          <p class="eyebrow">Cloze Recall</p>
          <h3 id="clozePrompt">mi ___ al dom.</h3>
          <p id="clozeEnglish" class="cloze-english">I am at home.</p>
          <p class="cloze-instruction">Fill in the missing Nari word.</p>
          <label class="practice-answer">
            <span>Missing word</span>
            <input id="clozeAnswer" type="text" autocomplete="off" placeholder="Type one word">
          </label>
          <div class="practice-actions">
            <button id="checkCloze" class="button primary" type="button">Check</button>
            <button id="nextCloze" class="button secondary" type="button">Skip</button>
            <p id="clozeFeedback">Active recall beats rereading.</p>
          </div>
        </div>
      </div>

      <div id="choicePanel" class="practice-mode-panel">
        <div class="choice-card glass-panel">
          <p class="eyebrow">Multiple Choice</p>
          <div class="choice-direction-toggle">
            <button id="choiceDirEnNari" class="chip is-active" type="button">English → Nari</button>
            <button id="choiceDirNariEn" class="chip" type="button">Nari → English</button>
          </div>
          <h3 id="choicePrompt">Choose the Nari word</h3>
          <p id="choiceFeedback">Fast recognition practice.</p>
          <div id="choiceOptions" class="choice-options"></div>
        </div>
      </div>

      <div id="matchPanel" class="practice-mode-panel">
        <div class="match-card glass-panel">
          <div class="match-header">
            <p class="eyebrow">Word Match</p>
            <span id="matchScore" class="srs-badge">0 matched</span>
          </div>
          <p id="matchFeedback">Tap a Nari word, then tap its English meaning.</p>
          <div id="matchGrid" class="match-grid"></div>
          <button id="newMatch" class="button secondary" type="button">New Round</button>
        </div>
      </div>

      <div id="buildPanel" class="practice-mode-panel">
        <div class="build-card glass-panel">
          <p class="eyebrow">Sentence Builder</p>
          <h3 id="buildPrompt">Translate this sentence</h3>
          <div id="buildDropzone" class="build-dropzone"></div>
          <div id="buildWordBank" class="build-wordbank"></div>
          <p id="buildFeedback" class="build-feedback"></p>
          <div class="build-actions">
            <button id="checkBuildBtn" class="button primary" type="button">Check</button>
            <button id="nextBuildBtn" class="button secondary" type="button" style="display:none;">Next</button>
          </div>
        </div>
      </div>
    </section>

    <section id="stories" class="section shell tab-panel">
      <div class="section-heading">
        <div>
          <p class="eyebrow">Reading practice</p>
          <h2>Stories in Nari</h2>
        </div>
        <div class="story-tabs glass-panel" role="group" aria-label="Story difficulty">
          <button class="story-tab is-active" type="button" data-story-level="easy">Easy</button>
          <button class="story-tab" type="button" data-story-level="mid">Mid</button>
          <button class="story-tab" type="button" data-story-level="hard">Hard</button>
                  </div>
      </div>
      <div id="easyStoryGrid" class="story-grid story-level-panel is-active"></div>
      <div id="midStoryGrid" class="story-grid story-level-panel"></div>
      <div id="hardStoryGrid" class="story-grid story-level-panel"></div>
      
            <div class="story-note glass-panel">
        <strong>Easy</strong> includes translations. <strong>Mid</strong> and <strong>Hard</strong> are Nari-only.
      </div>
    </section>

    <section id="grammar" class="section shell tab-panel">
      <div class="section-heading">
        <p class="eyebrow">Rules</p>
        <h2>Core Rules</h2>
      </div>
      <h3 class="rule-group-title">Core patterns</h3>
      <div class="grammar-layout">
        <article class="glass-panel grammar-card">
          <h3>Core sentence</h3>
          <p><strong>subject + verb + object</strong></p>
          <p><span class="nari">mi mo mek.</span> I eat food.</p>
          <p><span class="nari">ta re buka?</span> Do you read a book?</p>
        </article>
        <article class="glass-panel grammar-card">
          <h3>To be</h3>
          <p>Nari uses one word for am, is, are, was, and were forms.</p>
          <p><span class="nari">be</span> means to be, am, is, or are.</p>
          <p><span class="nari">mi be al dom.</span> I am at home.</p>
        </article>
        <article class="glass-panel grammar-card">
          <h3>Tense</h3>
          <p>Present uses the verb alone. Past adds <strong>-a</strong>. Future adds <strong>-u</strong>.</p>
          <p><span class="nari">mi ko.</span> I go.</p>
          <p><span class="nari">mi koa.</span> I went.</p>
          <p><span class="nari">mi kou.</span> I will go.</p>
        </article>
        <article class="glass-panel grammar-card">
          <h3>Negation and questions</h3>
          <p>Put <strong>na</strong> before the verb. Questions keep normal order and add a question mark.</p>
          <p><span class="nari">mi na ni.</span> I do not know.</p>
          <p><span class="nari">wer lis be?</span> Where is she?</p>
        </article>
        <article class="glass-panel grammar-card">
          <h3>Word creation</h3>
          <p>Take one root and add one ending. The root stays the same.</p>
          <p><span class="nari">tava</span> means teach. <span class="nari">taver</span> means teacher.</p>
          <p><strong>-er</strong> person, <strong>-in</strong> tool, <strong>-nes</strong> quality, <strong>-ing</strong> action.</p>
        </article>
        <article class="glass-panel grammar-card">
          <h3>Pronouns</h3>
          <p>Pronouns are short and never change form.</p>
          <p><span class="nari">mi</span> I, <span class="nari">ta</span> you, <span class="nari">mu</span> we, <span class="nari">lu</span> they.</p>
          <p><span class="nari">li</span> can mean a person when gender or identity does not matter.</p>
        </article>
        <article class="glass-panel grammar-card">
          <h3>Possession</h3>
          <p>Fast form: use possessive pronouns before the noun.</p>
          <p><span class="nari">mai buka</span> my book. <span class="nari">tai dom</span> your house.</p>
          <p>Clear form: use <strong>ov</strong>. <span class="nari">buka ov mi</span> book of me.</p>
          <p>Use <strong>su</strong> only for have: <span class="nari">ta su tel.</span></p>
        </article>
      </div>

      <h3 class="rule-group-title">Usage patterns</h3>
      <div class="grammar-layout">
        <article class="glass-panel grammar-card">
          <h3>Continuous action</h3>
          <p>Put <strong>du</strong> before a verb for an action happening right now.</p>
          <p><span class="nari">lis du re.</span> She is reading.</p>
          <p><span class="nari">mu du vora.</span> We are working.</p>
        </article>
        <article class="glass-panel grammar-card">
          <h3>Modals</h3>
          <p>Modal words come before the main verb.</p>
          <p><span class="nari">mi kan ko.</span> I can go.</p>
          <p><span class="nari">ta musu suma.</span> You must study.</p>
        </article>
        <article class="glass-panel grammar-card">
          <h3>Clauses</h3>
          <p><strong>dat</strong> links ideas and also works like who, which, or that.</p>
          <p><span class="nari">mi ni dat lih be guda.</span> I know that he is good.</p>
          <p><span class="nari">mava dat ra</span> the man who speaks.</p>
        </article>
        <article class="glass-panel grammar-card">
          <h3>Comparison</h3>
          <p>Use <strong>mor</strong>, <strong>les</strong>, <strong>mos</strong>, and <strong>lest</strong>.</p>
          <p><span class="nari">dis kar mor fasa.</span> This car is faster.</p>
          <p><span class="nari">dat dom mos bi.</span> That house is biggest.</p>
        </article>
        <article class="glass-panel grammar-card">
          <h3>Compounds</h3>
          <p>Join short words when a new idea is easier than a new root.</p>
          <p><span class="nari">vidakala</span> video call.</p>
          <p><span class="nari">solgala</span> sunglasses.</p>
        </article>
        <article class="glass-panel grammar-card">
          <h3>Style</h3>
          <p>Prefer the shortest sentence that still carries the meaning.</p>
          <p><span class="nari">mi na ni.</span> I do not know.</p>
          <p><span class="nari">mi kou la tomd.</span> I will come tomorrow.</p>
        </article>
      </div>
    </section>

    <section id="vocabulary" class="section shell tab-panel">
      <div class="section-heading vocab-heading">
        <div>
          <p class="eyebrow">Vocabulary</p>
          <h2>Everyday word bank</h2>
        </div>
        <label class="search glass-panel">
          <span>Search</span>
          <input id="vocabSearch" type="search" placeholder="Try food, friend, weather..." autocomplete="off">
        </label>
      </div>
      <div id="categoryChips" class="chips" aria-label="Vocabulary categories"></div>
      <div class="vocab-tools">
        <p id="vocabMeta"></p>
        <button id="showMore" class="button secondary" type="button">Show more</button>
      </div>
      <div class="glass-panel table-wrap">
        <table>
          <thead>
            <tr>
              <th>Nari</th>
              <th>English</th>
              <th>Category</th>
            </tr>
          </thead>
          <tbody id="vocabRows"></tbody>
        </table>
      </div>
    </section>
  </main>

  <footer class="shell footer">
    <p>Nari v1.2. Grammar stays light; vocabulary keeps growing.</p>
  </footer>

  <script src="nari-data.js"></script>
  <script src="script.js"></script>
</body>
</html>
"""
    (ROOT / "index.html").write_text(html_doc, encoding="utf-8")


def write_css() -> None:
    css = r""":root {
  color-scheme: dark;
  --text: #f8fbff;
  --muted: rgba(248, 251, 255, 0.72);
  --soft: rgba(248, 251, 255, 0.12);
  --line: rgba(255, 255, 255, 0.18);
  --glass: rgba(12, 18, 24, 0.46);
  --glass-strong: rgba(12, 18, 24, 0.62);
  --accent: #79e1d3;
  --accent-2: #ffd166;
  --ink: #081017;
  font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  min-width: 320px;
  margin: 0;
  color: var(--text);
  background: #081017;
}

@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(18px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes softGlow {
  0%, 100% {
    box-shadow: 0 22px 70px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.12);
  }
  50% {
    box-shadow: 0 26px 78px rgba(121, 225, 211, 0.12), inset 0 1px 0 rgba(255, 255, 255, 0.16);
  }
}

.backdrop-video,
.backdrop-tint {
  position: fixed;
  inset: 0;
  width: 100%;
  height: 100%;
}

.backdrop-video {
  object-fit: cover;
  z-index: -3;
  filter: saturate(0.95) contrast(1.04);
}

.backdrop-tint {
  z-index: -2;
  background:
    linear-gradient(180deg, rgba(5, 9, 14, 0.38), rgba(5, 9, 14, 0.82)),
    radial-gradient(circle at 72% 8%, rgba(121, 225, 211, 0.2), transparent 28%),
    linear-gradient(90deg, rgba(8, 16, 23, 0.75), rgba(8, 16, 23, 0.28));
}

a {
  color: inherit;
  text-decoration: none;
}

.shell {
  width: min(1160px, calc(100% - 32px));
  margin: 0 auto;
}

.site-header {
  position: sticky;
  top: 16px;
  z-index: 5;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 64px;
  padding: 10px 14px;
  margin-top: 16px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: rgba(8, 16, 23, 0.42);
  box-shadow: 0 16px 50px rgba(0, 0, 0, 0.22);
  backdrop-filter: blur(18px);
}

.brand,
.nav-links,
.hero-actions,
.chips,
.vocab-tools {
  display: flex;
  align-items: center;
}

.brand {
  gap: 10px;
  font-weight: 800;
}

.brand-mark {
  display: grid;
  width: 36px;
  height: 36px;
  place-items: center;
  border-radius: 8px;
  color: var(--ink);
  background: linear-gradient(135deg, var(--accent), var(--accent-2));
}

.nav-links {
  gap: 8px;
  flex-wrap: wrap;
}

.nav-links a,
.button,
.chip {
  min-height: 40px;
  border-radius: 8px;
  border: 1px solid var(--line);
  font-weight: 700;
}

.nav-links a {
  padding: 10px 14px;
  color: var(--muted);
}

.nav-links a:hover {
  color: var(--text);
  background: var(--soft);
}

.hero {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 280px;
  gap: 20px;
  align-items: end;
  min-height: calc(100vh - 96px);
  padding: 84px 0 48px;
}

.glass-panel {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--glass);
  box-shadow: 0 22px 70px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(22px) saturate(1.18);
  animation: fadeUp 650ms ease both;
  transition: transform 220ms ease, border-color 220ms ease, background 220ms ease, box-shadow 220ms ease;
}

.glass-panel:hover {
  transform: translateY(-2px);
  border-color: rgba(121, 225, 211, 0.32);
}

.hero-copy {
  max-width: 760px;
  padding: clamp(28px, 5vw, 56px);
}

.eyebrow {
  margin: 0 0 12px;
  color: var(--accent);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0;
  text-transform: uppercase;
}

h1,
h2,
h3,
p {
  overflow-wrap: anywhere;
}

h1 {
  margin: 0;
  font-size: clamp(4rem, 12vw, 9.5rem);
  line-height: 0.82;
  letter-spacing: 0;
}

h2 {
  margin: 0;
  font-size: clamp(2rem, 5vw, 4.5rem);
  line-height: 0.95;
  letter-spacing: 0;
}

h3 {
  margin: 0 0 14px;
  font-size: 1.1rem;
}

.lede {
  max-width: 650px;
  margin: 28px 0 0;
  color: var(--muted);
  font-size: clamp(1.05rem, 2vw, 1.35rem);
  line-height: 1.55;
}

.hero-actions {
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 30px;
}

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 11px 16px;
  cursor: pointer;
  transition: transform 180ms ease, background 180ms ease, border-color 180ms ease;
}

.button:hover,
.direction-button:hover,
.chip:hover {
  transform: translateY(-1px);
}

.button.primary {
  border-color: transparent;
  color: var(--ink);
  background: var(--accent);
}

.button.secondary {
  color: var(--text);
  background: rgba(255, 255, 255, 0.08);
}

.stats {
  display: grid;
  gap: 8px;
  padding: 18px;
}

.stats div {
  padding: 16px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.08);
}

.stats strong,
.stats span {
  display: block;
}

.stats strong {
  font-size: 1.7rem;
}

.stats span {
  color: var(--muted);
}

.section {
  padding: 84px 0;
}

.intro-panel {
  display: none;
}

.tab-panel {
  display: none;
  opacity: 0;
  transform: translateY(10px);
}

.tab-panel.is-active {
  display: block;
  animation: tabIn 260ms ease both;
}

.nav-links a.is-active {
  color: var(--ink);
  border-color: transparent;
  background: var(--accent);
}

@keyframes tabIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.section-heading {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 24px;
  margin-bottom: 24px;
}

.story-grid,
.grammar-layout,
.translator-grid,
.practice-layout {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
}

.story-tabs {
  display: flex;
  gap: 8px;
  padding: 8px;
}

.story-tab {
  min-height: 40px;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 10px 14px;
  color: var(--muted);
  background: rgba(255, 255, 255, 0.08);
  font: inherit;
  font-weight: 800;
  cursor: pointer;
  transition: transform 180ms ease, background 180ms ease, color 180ms ease;
}

.story-tab:hover {
  transform: translateY(-1px);
}

.story-tab.is-active {
  color: var(--ink);
  border-color: transparent;
  background: var(--accent-2);
}

.story-level-panel {
  display: none;
}

.story-level-panel.is-active {
  display: grid;
  animation: tabIn 240ms ease both;
}

/* ── Practice Mode Tabs (same style as story tabs) ── */
.practice-mode-tabs {
  display: flex;
  gap: 0.25rem;
  padding: 0.35rem;
  border-radius: 12px;
}
.practice-mode-tab {
  background: transparent;
  border: 1px solid transparent;
  color: var(--muted);
  cursor: pointer;
  font-family: inherit;
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  padding: 0.45rem 1rem;
  border-radius: 8px;
  transition: background 0.18s, color 0.18s;
}
.practice-mode-tab:hover {
  color: var(--text);
  background: rgba(255,255,255,0.05);
}
.practice-mode-tab.is-active {
  color: var(--ink);
  border-color: transparent;
  background: var(--accent-2);
}
.practice-mode-panel {
  display: none;
}
.practice-mode-panel.is-active {
  display: block;
  animation: tabIn 240ms ease both;
}

/* ── Flash Card ── */
.flash-card {
  max-width: 600px;
  margin: 0 auto;
  padding: 2.5rem 2rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.flash-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.flash-setup {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.flash-select {
  padding: 0.5rem;
  border-radius: 8px;
  background: rgba(255,255,255,0.1);
  color: var(--text);
  border: 1px solid rgba(255,255,255,0.2);
  font-family: inherit;
}
.flash-select option {
  background: var(--surface);
  color: var(--text);
}

/* ── Cloze Card ── */
.cloze-card {
  max-width: 600px;
  margin: 0 auto;
  padding: 2.5rem 2rem;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}
.cloze-english {
  color: var(--muted);
  font-size: 1.1rem;
  font-weight: 500;
  margin-top: -0.5rem;
  border-left: 2px solid var(--accent);
  padding-left: 0.8rem;
}
.cloze-instruction {
  color: var(--muted);
  font-size: 0.9rem;
  opacity: 0.7;
}

/* ── Choice Card ── */
.choice-card {
  max-width: 640px;
  margin: 0 auto;
  padding: 2.5rem 2rem;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}
.choice-direction-toggle { display: flex; gap: 0.5rem; margin-bottom: 0.5rem; }

/* ── Word Match ── */
.match-card {
  max-width: 680px;
  margin: 0 auto;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.match-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.match-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
}
.match-tile {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 10px;
  color: var(--text);
  cursor: pointer;
  font-family: inherit;
  font-size: 0.95rem;
  padding: 0.9rem 1rem;
  text-align: center;
  transition: background 0.15s, border-color 0.15s, transform 0.1s;
}
.match-tile:hover { background: rgba(255,255,255,0.08); transform: translateY(-1px); }
.match-tile.is-selected { border-color: var(--accent); background: rgba(99,102,241,0.15); }
.match-tile.is-correct { border-color: #27ae60; background: rgba(39,174,96,0.15); pointer-events: none; }
.match-tile.is-wrong { border-color: #c0392b; background: rgba(192,57,43,0.12); animation: shake 0.3s ease; }

/* Builder CSS */
.build-card {
  max-width: 680px;
  margin: 0 auto;
  padding: 2rem;
  display: flex;
  flex-direction: column;
}
#buildPrompt { margin-bottom: 1.5rem; }
.build-dropzone {
  min-height: 4rem;
  padding: 1.25rem;
  background: rgba(255,255,255,0.02);
  border: 1px dashed rgba(255,255,255,0.15);
  border-radius: 12px;
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin-bottom: 1.25rem;
  align-items: center;
}
.build-wordbank {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin-bottom: 1.5rem;
  min-height: 3.5rem;
}
.build-chip {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 18px;
  padding: 0.5rem 1rem;
  color: var(--text);
  cursor: pointer;
  font-family: inherit;
  font-size: 1rem;
  line-height: 1.3;
  transition: transform 0.15s, background 0.15s;
}
.build-chip:hover {
  background: rgba(255,255,255,0.1);
  transform: translateY(-1px);
}
.build-actions {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}
.build-feedback {
  min-height: 1.5rem;
  font-size: 0.9rem;
  color: var(--muted);
}
.build-dropzone.is-correct {
  border-color: #27ae60;
  background: rgba(39,174,96,0.05);
}
.build-dropzone.is-wrong {
  border-color: #c0392b;
  background: rgba(192,57,43,0.05);
  animation: shake 0.3s ease;
}
@keyframes shake {
  0%,100% { transform: translateX(0); }
  25% { transform: translateX(-6px); }
  75% { transform: translateX(6px); }
}

.story-note {
  margin-top: 16px;
  padding: 14px 16px;
  color: var(--muted);
  line-height: 1.5;
}

.rule-group-title {
  margin: 28px 0 14px;
  color: var(--accent-2);
  font-size: 1rem;
  text-transform: uppercase;
}

.direction-toggle {
  display: flex;
  gap: 8px;
  padding: 8px;
}

.direction-button {
  min-height: 40px;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 10px 12px;
  color: var(--muted);
  background: rgba(255, 255, 255, 0.08);
  font: inherit;
  font-weight: 800;
  cursor: pointer;
}

.direction-button.is-active {
  color: var(--ink);
  border-color: transparent;
  background: var(--accent);
}

.translator-box,
.translator-output {
  display: grid;
  gap: 12px;
  min-height: 280px;
  padding: 18px;
}

.translator-box span,
.translator-output span {
  color: var(--accent);
  font-size: 0.78rem;
  font-weight: 800;
  text-transform: uppercase;
}

.translator-box textarea {
  width: 100%;
  min-height: 210px;
  resize: vertical;
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 8px;
  outline: 0;
  padding: 16px;
  color: var(--text);
  background: rgba(0, 0, 0, 0.18);
  font: inherit;
  line-height: 1.55;
}

.translator-output {
  align-content: start;
  background: var(--glass-strong);
}

.translator-output p {
  margin: 0;
}

#translatorOutput {
  color: var(--accent-2);
  font-size: clamp(1.4rem, 3vw, 2.35rem);
  font-weight: 800;
  line-height: 1.2;
}

#translatorHint {
  color: var(--muted);
  line-height: 1.5;
}

.practice-card {
  padding: 24px;
}

.flashcard-panel {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  margin-top: 16px;
  padding: 24px;
}

.cloze-panel {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(220px, 0.5fr);
  gap: 18px;
  align-items: end;
  margin-top: 16px;
  padding: 24px;
}

.cloze-panel h3 {
  margin-bottom: 8px;
  color: var(--accent-2);
  font-size: clamp(1.5rem, 3vw, 2.5rem);
}

.cloze-panel p {
  margin: 0;
  color: var(--muted);
}

.choice-panel {
  display: grid;
  gap: 18px;
  margin-top: 16px;
  padding: 24px;
}

.choice-panel h3 {
  margin-bottom: 8px;
  font-size: clamp(1.4rem, 3vw, 2.25rem);
}

.choice-panel p {
  margin: 0;
  color: var(--muted);
}

.choice-options {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 10px;
}

.choice-option {
  min-height: 48px;
  border: 1px solid var(--line);
  border-radius: 8px;
  color: var(--text);
  background: rgba(255, 255, 255, 0.08);
  font: inherit;
  font-weight: 800;
  cursor: pointer;
}

.choice-option.is-correct {
  color: var(--ink);
  border-color: transparent;
  background: var(--accent);
}

.choice-option.is-wrong {
  border-color: rgba(255, 209, 102, 0.7);
  color: var(--accent-2);
}

.flashcard-panel h3 {
  margin-bottom: 8px;
  font-size: clamp(1.6rem, 4vw, 3rem);
}

.flashcard-panel p {
  margin: 0;
  color: var(--muted);
}

#flashAnswer {
  color: var(--accent-2);
  font-size: 1.2rem;
  font-weight: 800;
}

.practice-card h3 {
  font-size: clamp(1.45rem, 3vw, 2.4rem);
  line-height: 1.1;
}

.practice-answer {
  display: grid;
  gap: 8px;
  margin-top: 22px;
}

.practice-answer span {
  color: var(--accent);
  font-size: 0.78rem;
  font-weight: 800;
  text-transform: uppercase;
}

.practice-answer input {
  min-height: 52px;
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 8px;
  outline: 0;
  padding: 0 14px;
  color: var(--text);
  background: rgba(0, 0, 0, 0.18);
  font: inherit;
  transition: border-color 180ms ease, box-shadow 180ms ease;
}

.practice-answer input:focus,
.translator-box textarea:focus,
.search input:focus {
  border-color: rgba(121, 225, 211, 0.65);
  box-shadow: 0 0 0 3px rgba(121, 225, 211, 0.12);
}

.practice-actions {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
  margin-top: 18px;
}

.practice-actions p,
.practice-list {
  color: var(--muted);
  line-height: 1.55;
}

.practice-actions p.is-correct {
  color: var(--accent);
  font-weight: 800;
}

.practice-actions p.is-warn {
  color: var(--accent-2);
  font-weight: 800;
}

.practice-list {
  display: grid;
  gap: 12px;
  padding-left: 20px;
  margin: 0;
}

.story-card,
.grammar-card {
  padding: 24px;
}

.story-title {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 18px;
}

.story-title span {
  color: var(--muted);
  font-size: 0.9rem;
}

.story-lines {
  display: grid;
  gap: 14px;
}

.story-lines p {
  margin: 0;
}

.nari {
  color: var(--accent-2);
  font-weight: 800;
}

.english {
  color: var(--muted);
}

.grammar-card p {
  color: var(--muted);
  line-height: 1.55;
}

.grammar-card strong {
  color: var(--text);
}

.vocab-heading {
  align-items: center;
}

.search {
  display: grid;
  gap: 8px;
  min-width: min(360px, 100%);
  padding: 12px;
}

.search span {
  color: var(--muted);
  font-size: 0.78rem;
  font-weight: 800;
  text-transform: uppercase;
}

.search input {
  width: 100%;
  border: 0;
  outline: 0;
  color: var(--text);
  background: transparent;
  font: inherit;
}

.chips {
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 16px;
}

.chip {
  padding: 8px 11px;
  color: var(--muted);
  background: rgba(255, 255, 255, 0.08);
  cursor: pointer;
}

.chip.is-active {
  color: var(--ink);
  border-color: transparent;
  background: var(--accent-2);
}

.vocab-tools {
  justify-content: space-between;
  gap: 16px;
  margin: 18px 0;
}

.vocab-tools p {
  margin: 0;
  color: var(--muted);
}

.custom-word-form {
  display: grid;
  gap: 14px;
  margin: 16px 0;
  padding: 16px;
}

.custom-word-form > div {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
}

.custom-word-form label {
  display: grid;
  gap: 8px;
}

.custom-word-form span {
  color: var(--accent);
  font-size: 0.78rem;
  font-weight: 800;
  text-transform: uppercase;
}

.custom-word-form input {
  min-height: 44px;
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 8px;
  outline: 0;
  padding: 0 12px;
  color: var(--text);
  background: rgba(0, 0, 0, 0.18);
  font: inherit;
}

.custom-word-form p {
  margin: 0;
  color: var(--muted);
}

.table-wrap {
  overflow: hidden;
}

table {
  width: 100%;
  border-collapse: collapse;
  background: var(--glass-strong);
}

th,
td {
  padding: 14px 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  text-align: left;
  vertical-align: top;
}

th {
  color: var(--muted);
  font-size: 0.78rem;
  text-transform: uppercase;
}

td:first-child {
  color: var(--accent-2);
  font-weight: 800;
}

.remove-word {
  min-height: 34px;
  border: 1px solid rgba(255, 209, 102, 0.38);
  border-radius: 8px;
  padding: 6px 10px;
  color: var(--accent-2);
  background: rgba(255, 209, 102, 0.08);
  font: inherit;
  font-weight: 800;
  cursor: pointer;
}

.remove-word:hover {
  background: rgba(255, 209, 102, 0.16);
}

.empty-cell {
  padding: 28px 16px;
  color: var(--muted);
  text-align: center;
}

.footer {
  padding: 24px 0 56px;
  color: var(--muted);
}

@media (max-width: 780px) {
  .site-header,
  .section-heading,
  .vocab-tools {
    align-items: stretch;
    flex-direction: column;
  }

  .nav-links {
    width: 100%;
    justify-content: space-between;
  }

  .nav-links a {
    flex: 1;
    padding-inline: 8px;
    text-align: center;
  }

  .hero,
  .story-grid,
  .grammar-layout,
  .translator-grid,
  .practice-layout {
    grid-template-columns: 1fr;
  }

  .direction-toggle {
    flex-direction: column;
  }

  .flashcard-panel {
    align-items: stretch;
    flex-direction: column;
  }

  .cloze-panel {
    grid-template-columns: 1fr;
  }

  .choice-options {
    grid-template-columns: 1fr;
  }

  .custom-word-form > div {
    grid-template-columns: 1fr;
  }

  .hero {
    min-height: auto;
    padding-top: 60px;
  }

  .stats {
    grid-template-columns: repeat(3, minmax(0, 1fr));
    padding: 10px;
  }

  .stats div {
    padding: 10px;
  }

  .stats strong {
    font-size: 1.2rem;
  }

  .stats span {
    font-size: 0.78rem;
  }

  th:nth-child(3),
  td:nth-child(3) {
    display: none;
  }
}


/* ===== HOME PAGE ===== */
.hp-hero {
  position: relative;
  overflow: hidden;
  padding: 7rem 0 5rem;
  text-align: center;
  border-bottom: 1px solid var(--line);
}
.hp-hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 70% 80% at 50% -10%, rgba(121,225,211,0.18) 0%, transparent 65%),
    radial-gradient(ellipse 40% 40% at 80% 50%, rgba(255,209,102,0.06) 0%, transparent 60%);
  pointer-events: none;
}
.hp-hero-glow { display: none; }
.hp-hero-inner {
  position: relative;
  z-index: 1;
}
.hp-title {
  font-size: clamp(6rem, 18vw, 13rem);
  font-weight: 900;
  line-height: 0.85;
  letter-spacing: -0.04em;
  background: linear-gradient(160deg, #ffffff 20%, #b2f0e8 60%, var(--accent) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 0.3em 0 0.25em;
}
.hp-lede {
  max-width: 520px;
  margin: 0 auto 2.5rem;
  color: var(--muted);
  font-size: clamp(1rem, 2vw, 1.18rem);
  line-height: 1.7;
}
.hp-cta-row {
  display: flex;
  gap: 0.85rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 3.5rem;
}
.hp-btn {
  padding: 0.8rem 2.2rem;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: 0.01em;
}
.hp-stats-inline {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--glass);
  backdrop-filter: blur(16px);
  width: fit-content;
  margin: 0 auto;
  overflow: hidden;
}
.hp-stat-inline {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.15rem;
  padding: 1rem 2.5rem;
}
.hp-stat-inline strong {
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--accent);
  line-height: 1;
}
.hp-stat-inline span {
  font-size: 0.72rem;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  white-space: nowrap;
}
.hp-stat-divider {
  width: 1px;
  height: 2.5rem;
  background: var(--line);
  flex-shrink: 0;
}

/* sections */
.hp-section {
  padding: 5rem 0;
}
.hp-section-dark {
  background: rgba(255,255,255,0.02);
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}
.hp-section-head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 1.5rem;
  margin-bottom: 2.5rem;
  flex-wrap: wrap;
}
.hp-section-title {
  font-size: clamp(1.8rem, 3.5vw, 2.6rem);
  font-weight: 800;
  margin: 0.3rem 0 0;
  line-height: 1.05;
  letter-spacing: -0.02em;
}

/* quick translate */
.hp-block {
  padding: 3rem 3rem;
}
.hp-block-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}
.hp-block-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0.25rem 0 0;
  line-height: 1.1;
}
.hp-translate-row {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 1.2rem;
  align-items: center;
}
.hp-translate-side {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}
.hp-translate-label {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
}
.hp-translate-arrow-col {
  font-size: 1.5rem;
  color: var(--accent);
  text-align: center;
  padding-top: 1.5rem;
}
.hp-translate-input {
  background: rgba(255,255,255,0.05);
  border: 1px solid var(--line);
  border-radius: 10px;
  color: var(--text);
  font-size: 1.1rem;
  font-family: inherit;
  padding: 1.1rem 1.3rem;
  outline: none;
  transition: border-color 0.2s, background 0.2s;
  min-height: 70px;
}
.hp-translate-input::placeholder { color: rgba(248,251,255,0.3); }
.hp-translate-input:focus {
  border-color: var(--accent);
  background: rgba(255,255,255,0.08);
}
.hp-translate-output {
  background: rgba(121,225,211,0.05);
  border: 1px solid rgba(121,225,211,0.2);
  border-radius: 10px;
  padding: 1.1rem 1.3rem;
  font-size: 1.1rem;
  color: var(--muted);
  font-style: italic;
  min-height: 70px;
  display: flex;
  align-items: center;
  word-break: break-word;
  transition: color 0.2s;
}
.hp-translate-output.hp-has-result {
  color: var(--accent);
  font-style: normal;
  font-weight: 600;
  font-size: 1.3rem;
}
.hp-translate-hint {
  margin-top: 1rem;
  font-size: 0.8rem;
  color: var(--muted);
  opacity: 0.6;
}

/* grammar cards */
.hp-grammar-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.2rem;
}
.hp-grammar-card {
  padding: 1.8rem 2rem;
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}
.hp-grammar-pill {
  display: inline-block;
  background: rgba(121,225,211,0.13);
  color: var(--accent);
  border-radius: 99px;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  padding: 0.28rem 0.9rem;
  width: fit-content;
}
.hp-grammar-example {
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: -0.01em;
}
.hp-grammar-gloss {
  font-size: 0.85rem;
  color: var(--muted);
  line-height: 1.6;
}

/* feature cards */
.hp-features {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.2rem;
  margin-top: 0;
}
.hp-feature-card {
  cursor: pointer;
  background: var(--glass);
  border: 1px solid var(--line);
  border-radius: 8px;
  backdrop-filter: blur(22px) saturate(1.18);
  box-shadow: 0 22px 70px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.12);
  padding: 2.2rem 2rem;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  position: relative;
  transition: transform 0.22s ease, border-color 0.22s ease, box-shadow 0.22s ease;
}
.hp-feature-card:hover {
  transform: translateY(-5px);
  border-color: rgba(121,225,211,0.5);
  box-shadow: 0 24px 60px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.16);
}
.hp-feature-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 0.6rem;
}
.hp-feature-icon {
  font-size: 2.2rem;
  line-height: 1;
}
.hp-feature-arrow {
  color: var(--accent);
  font-size: 1.3rem;
  font-weight: 700;
  opacity: 0;
  transform: translate(-6px, 6px);
  transition: opacity 0.22s, transform 0.22s;
}
.hp-feature-card:hover .hp-feature-arrow {
  opacity: 1;
  transform: translate(0, 0);
}
.hp-feature-card h3 {
  margin: 0;
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: -0.01em;
}
.hp-feature-card p {
  margin: 0;
  font-size: 0.88rem;
  color: var(--muted);
  line-height: 1.6;
}

@media (max-width: 900px) {
  .hp-grammar-grid { grid-template-columns: repeat(2, 1fr); }
  .hp-features { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
  .hp-stats-inline { flex-direction: column; width: 100%; }
  .hp-stat-divider { width: 80%; height: 1px; }
  .hp-translate-row { grid-template-columns: 1fr; }
  .hp-translate-arrow-col { display: none; }
  .hp-grammar-grid { grid-template-columns: 1fr; }
  .hp-features { grid-template-columns: 1fr; }
  .hp-block { padding: 2rem 1.5rem; }
  .hp-section-head { flex-direction: column; align-items: flex-start; }
}

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    scroll-behavior: auto !important;
    animation-duration: 1ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 1ms !important;
  }
}
"""
    (ROOT / "styles.css").write_text(css, encoding="utf-8")


def write_script() -> None:
    js = r"""const data = window.NARI_DATA;
const rows = [...data.entries];
const tabIds = ["home", "translator", "practice", "stories", "grammar", "vocabulary"];
const state = {
  search: "",
  category: "All",
  limit: 120,
};

const easyStoryGrid = document.querySelector("#easyStoryGrid");
const midStoryGrid = document.querySelector("#midStoryGrid");
const hardStoryGrid = document.querySelector("#hardStoryGrid");
const storyTabs = document.querySelectorAll("[data-story-level]");
const storyPanels = document.querySelectorAll(".story-level-panel");
const wordCount = document.querySelector("#wordCount");
const tabLinks = document.querySelectorAll("[data-tab-link]");
const tabPanels = document.querySelectorAll(".tab-panel");
const categoryChips = document.querySelector("#categoryChips");
const vocabRows = document.querySelector("#vocabRows");
const vocabMeta = document.querySelector("#vocabMeta");
const vocabSearch = document.querySelector("#vocabSearch");
const showMore = document.querySelector("#showMore");
const translatorInput = document.querySelector("#translatorInput");
const translatorOutput = document.querySelector("#translatorOutput");
const translatorHint = document.querySelector("#translatorHint");
const sourceLabel = document.querySelector("#sourceLabel");
const targetLabel = document.querySelector("#targetLabel");
const directionButtons = document.querySelectorAll(".direction-button");
const drillMode = document.querySelector("#drillMode");
const drillPrompt = document.querySelector("#drillPrompt");
const drillAnswer = document.querySelector("#drillAnswer");
const drillFeedback = document.querySelector("#drillFeedback");
const checkDrill = document.querySelector("#checkDrill");
const nextDrill = document.querySelector("#nextDrill");
const matchGrid = document.querySelector("#matchGrid");
const matchScore = document.querySelector("#matchScore");
const matchFeedback = document.querySelector("#matchFeedback");
const newMatchBtn = document.querySelector("#newMatch");
const buildPrompt = document.querySelector("#buildPrompt");
const buildDropzone = document.querySelector("#buildDropzone");
const buildWordBank = document.querySelector("#buildWordBank");
const checkBuildBtn = document.querySelector("#checkBuildBtn");
const nextBuildBtn = document.querySelector("#nextBuildBtn");
const buildFeedback = document.querySelector("#buildFeedback");
const choiceDirEnNari = document.querySelector("#choiceDirEnNari");
const choiceDirNariEn = document.querySelector("#choiceDirNariEn");
const clozePrompt = document.querySelector("#clozePrompt");
const clozeEnglish = document.querySelector("#clozeEnglish");
const clozeAnswer = document.querySelector("#clozeAnswer");
const checkCloze = document.querySelector("#checkCloze");
const nextCloze = document.querySelector("#nextCloze");
const clozeFeedback = document.querySelector("#clozeFeedback");
const choicePrompt = document.querySelector("#choicePrompt");
const choiceOptions = document.querySelector("#choiceOptions");
const choiceFeedback = document.querySelector("#choiceFeedback");

let englishToNari = new Map(rows.map((row) => [row.english.toLowerCase(), row.nari]));
let nariToEnglish = new Map(rows.map((row) => [row.nari.toLowerCase(), row.english.toLowerCase()]));
const englishAliases = new Map([
  ["am", "be"],
  ["is", "be"],
  ["are", "be"],
  ["was", "bea"],
  ["were", "bea"],
  ["being", "du be"],
  ["been", "bea"],
  ["home", "dom"],
]);
const irregularVerbs = {
  "got": "get", "went": "go", "saw": "see", "came": "come", "said": "say", "made": "make",
  "took": "take", "thought": "think", "knew": "know", "found": "find", "told": "tell",
  "gave": "give", "left": "leave", "felt": "feel", "put": "put", "brought": "bring",
  "began": "begin", "kept": "keep", "held": "hold", "wrote": "write", "stood": "stand",
  "heard": "hear", "let": "let", "meant": "mean", "set": "set", "met": "meet",
  "ran": "run", "paid": "pay", "sat": "sit", "spoke": "speak", "led": "lead", "read": "read",
  "grew": "grow", "lost": "lose", "fell": "fall", "sent": "send", "built": "build",
  "understood": "understand", "drew": "draw", "broke": "break", "spent": "spend", "bought": "buy",
  "taught": "teach", "won": "win", "slept": "sleep", "caught": "catch", "ate": "eat",
  "drank": "drink", "drove": "drive", "hid": "hide", "rode": "ride", "sang": "sing", "swam": "swim"
};
for (let [past, base] of Object.entries(irregularVerbs)) {
  if (englishToNari.has(base)) {
    englishAliases.set(past, englishToNari.get(base) + "a");
  }
}
const gerundAliases = new Map([
  ["working", "vora"],
  ["playing", "pali"],
  ["studying", "suma"],
  ["learning", "luma"],
  ["teaching", "tava"],
  ["reading", "re"],
  ["writing", "wri"],
  ["eating", "mo"],
  ["drinking", "dri"],
  ["walking", "bo"],
  ["looking", "luka"],
  ["watching", "wata"],
  ["going", "ko"],
  ["coming", "la"],
  ["speaking", "ra"],
  ["helping", "hel"],
]);
const punctuation = new Set([".", ",", "!", "?", ";", ":"]);
let translationDirection = "en-nari";
let currentDrill = null;
let currentFlash = null;


let currentCloze = null;
let currentChoice = null;

const grammarDrills = [
  { mode: "Possessive pronouns", prompt: "Translate: my book", answer: "mai buka" },
  { mode: "Possessive pronouns", prompt: "Translate: your house", answer: "tai dom" },
  { mode: "Possessive pronouns", prompt: "Translate: our phone", answer: "mui tel" },
  { mode: "Possessive pronouns", prompt: "Translate: his car", answer: "lis kar" },
  { mode: "Possessive pronouns", prompt: "Translate: their food", answer: "lisi mek" },
  { mode: "To be", prompt: "Translate: I am at home", answer: "mi be al dom" },
  { mode: "To be", prompt: "Translate: you are a teacher", answer: "ta be taver" },
  { mode: "To be", prompt: "Translate: she is happy", answer: "lis be hapi" },
  { mode: "Possession with ov", prompt: "Translate: book of me", answer: "buka ov mi" },
  { mode: "Possession with ov", prompt: "Translate: friend of mine", answer: "ami ov mi" },
  { mode: "Tense", prompt: "Translate: I went home", answer: "mi koa dom" },
  { mode: "Tense", prompt: "Translate: I will go tomorrow", answer: "mi kou la tomd" },
  { mode: "Tense", prompt: "Translate: she ate food", answer: "lis moa mek" },
  { mode: "Tense", prompt: "Translate: we will study", answer: "mu sumau" },
  { mode: "Tense", prompt: "What is the past tense suffix?", answer: "a" },
  { mode: "Tense", prompt: "What is the future tense suffix?", answer: "u" },
  { mode: "Negation", prompt: "Translate: I do not know", answer: "mi na ni" },
  { mode: "Negation", prompt: "Translate: she does not eat", answer: "lis na mo" },
  { mode: "Negation", prompt: "Translate: we do not sleep", answer: "mu na sleepa" },
  { mode: "Word order", prompt: "Translate: she reads a book", answer: "lis re buka" },
  { mode: "Word order", prompt: "Translate: he drinks water", answer: "li dri ven" },
  { mode: "Word order", prompt: "Translate: I love you", answer: "mi lova ta" },
  { mode: "Modals", prompt: "Translate: you must study", answer: "ta musu suma" },
  { mode: "Modals", prompt: "Translate: I can go", answer: "mi pova ko" },
  { mode: "Modals", prompt: "Translate: she should rest", answer: "lis shuda resta" },
  { mode: "Continuous action", prompt: "Translate: we are working", answer: "mu du vora" },
  { mode: "Continuous action", prompt: "Translate: I am eating", answer: "mi du mo" },
  { mode: "Continuous action", prompt: "Translate: they are studying", answer: "lisi du suma" },
  { mode: "Colors", prompt: "Translate to Nari: blue", answer: "sanu" },
  { mode: "Colors", prompt: "Translate to Nari: turquoise", answer: "turka" },
  { mode: "Colors", prompt: "Translate to Nari: red", answer: "ruba" },
  { mode: "Colors", prompt: "Translate to Nari: green", answer: "grina" },
  { mode: "Colors", prompt: "Translate to Nari: black", answer: "noka" },
  { mode: "Body", prompt: "Translate to Nari: shoulder", answer: "brelnel" },
  { mode: "Body", prompt: "Translate to Nari: wrist", answer: "rista" },
  { mode: "Body", prompt: "Translate: I have a headache", answer: "mi su dramlon" },
  { mode: "Body", prompt: "Translate to Nari: heart", answer: "kora" },
  { mode: "Body", prompt: "Translate to Nari: eye", answer: "oka" },
  { mode: "Everyday", prompt: "Translate: I want water", answer: "mi wena ven" },
  { mode: "Everyday", prompt: "Translate: open the door", answer: "opa dora n" },
  { mode: "Everyday", prompt: "Translate: I am hungry", answer: "mi be hungra" },
  { mode: "Everyday", prompt: "Translate: good morning", answer: "guda morn" },
  { mode: "Everyday", prompt: "Translate: thank you", answer: "gracia" },
  { mode: "Question", prompt: "Translate: where are you", answer: "wer ta be" },
  { mode: "Question", prompt: "Translate: what do you want", answer: "wt ta wena" },
  { mode: "Question", prompt: "Translate: who is she", answer: "hu be lis" },
  { mode: "Question", prompt: "Translate: when do we go", answer: "wen mu ko" },
  { mode: "Future", prompt: "Translate: we will come tomorrow", answer: "mu kou la tomd" },
  { mode: "Future", prompt: "Translate: I will eat soon", answer: "mi mou sona" },
  { mode: "Slang", prompt: "Translate: what the fuck", answer: "wt fk" },
  { mode: "Slang", prompt: "Translate: that is crazy", answer: "dat be zani" },
  { mode: "Slang", prompt: "Translate: no cap", answer: "na fala" },
  { mode: "Pronouns", prompt: "Translate: I", answer: "mi" },
  { mode: "Pronouns", prompt: "Translate: you", answer: "ta" },
  { mode: "Pronouns", prompt: "Translate: she / he", answer: "lis / li" },
  { mode: "Pronouns", prompt: "Translate: we", answer: "mu" },
  { mode: "Pronouns", prompt: "Translate: they", answer: "lisi" },
  { mode: "Derivation", prompt: "How do you say 'worker' in Nari?", answer: "voraer" },
  { mode: "Derivation", prompt: "How do you say 'teacher' in Nari?", answer: "taver" },
  { mode: "Derivation", prompt: "What does the suffix -er mean?", answer: "person who does" },
  { mode: "Derivation", prompt: "What does the suffix -i mean on a noun?", answer: "plural" },
  { mode: "Derivation", prompt: "What does the suffix -nes mean?", answer: "quality or state" },
];

const clozeDrills = [
  { sentence: "mi ___ al dom.", answer: "be", hint: "I am at home." },
  { sentence: "mu ___ vora.", answer: "du", hint: "We are working." },
  { sentence: "___ buka", answer: "mai", hint: "my book" },
  { sentence: "ta ___ suma.", answer: "musu", hint: "You must study." },
  { sentence: "lis ___ taver.", answer: "be", hint: "She is a teacher." },
  { sentence: "mi ___ ni.", answer: "na", hint: "I do not know." },
  { sentence: "ruba ___", answer: "kar", hint: "red car" },
  { sentence: "mi su pain al ___.", answer: "rista", hint: "I have pain in my wrist." },
  { sentence: "mi ___ al dom.", answer: "koa", hint: "I went to the house." },
  { sentence: "ta ___ mek?", answer: "mo", hint: "Are you eating food?" },
  { sentence: "lis ___ ta.", answer: "siu", hint: "She will see you." },
  { sentence: "mu ___ al dom.", answer: "kou", hint: "We will go home." },
  { sentence: "ta su ___?", answer: "kato", hint: "Do you have a cat?" },
  { sentence: "lisi ___ vora.", answer: "na", hint: "They do not work." },
  { sentence: "mi si ___ kanoi.", answer: "tu", hint: "I see two dogs." },
  { sentence: "___ dom be ruba.", answer: "lisai", hint: "Her house is red." },
  { sentence: "mu vora ___ ta.", answer: "vi", hint: "We work with you." },
  { sentence: "ta mo ___ mek?", answer: "tai", hint: "Are you eating your food?" },
  { sentence: "mi ___ buka.", answer: "sia", hint: "I saw the book." },
  { sentence: "lis su ___ katoi.", answer: "tri", hint: "He has three cats." },
  { sentence: "mu ___ ni.", answer: "na", hint: "We do not know." },
  { sentence: "ta ___ al dom?", answer: "beu", hint: "Will you be at home?" },
  { sentence: "lisi ___ mek.", answer: "mou", hint: "They will eat food." },
  { sentence: "mi vora ___ dom.", answer: "al", hint: "I work at the house." },
  { sentence: "___ buka be ruba.", answer: "mai", hint: "My book is red." },
  { sentence: "ta ___ vora.", answer: "na", hint: "You do not work." },
  { sentence: "lis si ___ kanoi.", answer: "mai", hint: "She sees my dogs." },
  { sentence: "mu ___ katoi.", answer: "su", hint: "We have cats." },
  { sentence: "mi si ___ kano.", answer: "tai", hint: "I see your dog." },
  { sentence: "lisi ___ al vora.", answer: "koa", hint: "They went to work." }
];

wordCount.textContent = rows.length.toLocaleString();

tabLinks.forEach((link) => {
  link.addEventListener("click", (event) => {
    event.preventDefault();
    const tabId = link.dataset.tabLink;
    showTab(tabId);
    history.pushState(null, "", `#${tabId}`);
  });
});

window.addEventListener("popstate", () => {
  showTab(getRequestedTab());
});

storyTabs.forEach((button) => {
  button.addEventListener("click", () => {
    showStoryLevel(button.dataset.storyLevel);
  });
});

easyStoryGrid.innerHTML = data.stories.map((story) => {
  const lines = story.nari.map((line, index) => `
    <div>
      <p class="nari">${escapeHtml(line)}</p>
      <p class="english">${escapeHtml(story.english[index])}</p>
    </div>
  `).join("");
  return `
    <article class="story-card glass-panel">
      <div class="story-title">
        <h3>${escapeHtml(story.title)}</h3>
        <span>${escapeHtml(story.translation)}</span>
      </div>
      <div class="story-lines">${lines}</div>
    </article>
  `;
}).join("");

midStoryGrid.innerHTML = data.midStories.map((text) => `
  <article class="story-card glass-panel advanced-card">
    <div class="story-title">
      <h3>${escapeHtml(text.title)}</h3>
      <span>Mid</span>
    </div>
    <div class="story-lines">
      ${text.lines.map((line) => `<p class="nari">${escapeHtml(line)}</p>`).join("")}
    </div>
  </article>
`).join("");

hardStoryGrid.innerHTML = data.advancedTexts.map((text) => `
  <article class="story-card glass-panel advanced-card">
    <div class="story-title">
      <h3>${escapeHtml(text.title)}</h3>
      <span>Hard</span>
    </div>
    <div class="story-lines">
      ${text.lines.map((line) => `<p class="nari">${escapeHtml(line)}</p>`).join("")}
    </div>
  </article>
`).join("");

renderCategoryChips();

categoryChips.addEventListener("click", (event) => {
  const button = event.target.closest("button");
  if (!button) return;
  state.category = button.dataset.category;
  state.limit = 120;
  document.querySelectorAll(".chip").forEach((chip) => chip.classList.toggle("is-active", chip === button));
  renderVocabulary();
});

vocabSearch.addEventListener("input", (event) => {
  state.search = event.target.value.trim().toLowerCase();
  state.limit = 120;
  renderVocabulary();
});

showMore.addEventListener("click", () => {
  state.limit += 160;
  renderVocabulary();
});


nextDrill.addEventListener("click", loadDrill);
checkDrill.addEventListener("click", checkCurrentDrill);
drillAnswer.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    checkCurrentDrill();
  }
});
newMatchBtn.addEventListener("click", loadMatch);

const practiceModeTabButtons = document.querySelectorAll(".practice-mode-tab");
const practiceModePanels = document.querySelectorAll(".practice-mode-panel");
function showPracticeMode(target) {
  practiceModeTabButtons.forEach((b) => b.classList.toggle("is-active", b.dataset.practiceTab === target));
  practiceModePanels.forEach((p) => p.classList.toggle("is-active", p.id === target + "Panel"));
  localStorage.setItem("nari_practice_tab", target);
  if (target === "match") loadMatch();
  if (target === "build") loadBuilder();
}

practiceModeTabButtons.forEach((btn) => {
  btn.addEventListener("click", () => showPracticeMode(btn.dataset.practiceTab));
});

choiceDirEnNari.addEventListener("click", () => {
  choiceDirection = "en-nari";
  choiceDirEnNari.classList.add("is-active");
  choiceDirNariEn.classList.remove("is-active");
  loadChoice();
});
choiceDirNariEn.addEventListener("click", () => {
  choiceDirection = "nari-en";
  choiceDirNariEn.classList.add("is-active");
  choiceDirEnNari.classList.remove("is-active");
  loadChoice();
});
nextCloze.addEventListener("click", loadCloze);
checkCloze.addEventListener("click", checkClozeAnswer);
clozeAnswer.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    checkClozeAnswer();
  }
});


directionButtons.forEach((button) => {
  button.addEventListener("click", () => {
    translationDirection = button.dataset.direction;
    directionButtons.forEach((item) => item.classList.toggle("is-active", item === button));
    sourceLabel.textContent = translationDirection === "en-nari" ? "English" : "Nari";
    targetLabel.textContent = translationDirection === "en-nari" ? "Nari" : "English";
    translatorInput.placeholder = translationDirection === "en-nari"
      ? "Type a sentence like: I want coffee after work."
      : "Type a sentence like: mi wena kafa afra vora.";
    translateText();
  });
});

translatorInput.addEventListener("input", translateText);

function getFilteredRows() {
  return rows.filter((row) => {
    const matchesCategory = state.category === "All" || row.category === state.category;
    const haystack = `${row.nari} ${row.english} ${row.category}`.toLowerCase();
    return matchesCategory && haystack.includes(state.search);
  });
}

function renderCategoryChips() {
  const categories = ["All", ...Array.from(new Set(rows.map((row) => row.category))).sort()];
  if (!categories.includes(state.category)) state.category = "All";
  categoryChips.innerHTML = categories.map((category) => `
    <button class="chip${category === state.category ? " is-active" : ""}" type="button" data-category="${escapeHtml(category)}">
      ${escapeHtml(category)}
    </button>
  `).join("");
}

function renderVocabulary() {
  const filtered = getFilteredRows();
  const visible = filtered.slice(0, state.limit);
  vocabRows.innerHTML = visible.length ? visible.map((row) => `
    <tr>
      <td>${escapeHtml(row.nari)}</td>
      <td>${escapeHtml(row.english)}</td>
      <td>${escapeHtml(row.category)}</td>
      <td>${row.custom ? `<button class="remove-word" type="button" data-remove-word="${escapeHtml(row.english)}">Remove</button>` : ""}</td>
    </tr>
  `).join("") : `
    <tr>
      <td colspan="4" class="empty-cell">No matching words yet. Try a broader search or another category.</td>
    </tr>
  `;
  vocabMeta.textContent = filtered.length
    ? `Showing ${visible.length.toLocaleString()} of ${filtered.length.toLocaleString()} matching entries.`
    : "No entries match the current filters.";
  showMore.hidden = visible.length >= filtered.length;
}

function translateText() {
  const input = translatorInput.value.trim();
  const sample = translationDirection === "en-nari" ? "I want coffee after work." : "mi wena kafa afra vora.";
  const source = input || sample;
  const translated = translationDirection === "en-nari"
    ? translateEnglishToNari(source)
    : translateNariToEnglish(source);
  translatorOutput.textContent = translated;
  translatorHint.textContent = translated.includes("·")
    ? "Words marked with a dot are not in the vocabulary yet."
    : "Word-by-word translation from the current vocabulary.";
}

function translateEnglishToNari(text) {
  const compact = text.toLowerCase().trim();
  if (compact === "to be") return "be";
  const tokens = tokenize(text);
  const output = [];
  for (let index = 0; index < tokens.length; index += 1) {
    const token = tokens[index];
    if (punctuation.has(token)) {
      output.push(token);
      continue;
    }
    const lower = token.toLowerCase();
    const next = tokens[index + 1]?.toLowerCase();
    if (["a", "an", "the"].includes(lower)) {
      continue;
    }
    
    // Check for 4-word, 3-word, and 2-word compounds
    const next2 = tokens[index + 2]?.toLowerCase();
    const next3 = tokens[index + 3]?.toLowerCase();
    
    if (next && next2 && next3) {
      const comp4 = lower + " " + next + " " + next2 + " " + next3;
      if (englishToNari.has(comp4)) {
        output.push(englishToNari.get(comp4));
        index += 3;
        continue;
      }
    }
    if (next && next2) {
      const comp3 = lower + " " + next + " " + next2;
      if (englishToNari.has(comp3)) {
        output.push(englishToNari.get(comp3));
        index += 2;
        continue;
      }
    }
    if (next) {
      const comp2 = lower + " " + next;
      if (englishToNari.has(comp2)) {
        output.push(englishToNari.get(comp2));
        index += 1;
        continue;
      }
    }
    
    if (lower === "at" && next === "home") {
      output.push("al", "dom");
      index += 1;
      continue;
    }
        if (lower === "did" && next && englishToNari.has(next)) {
      output.push(englishToNari.get(next) + "a");
      index += 1;
      continue;
    }
    if (lower === "will" && next && englishToNari.has(next)) {
      output.push(englishToNari.get(next) + "u");
      index += 1;
      continue;
    }
    let nextGerund = null;
    if (next) {
      if (gerundAliases.has(next)) {
        nextGerund = gerundAliases.get(next);
      } else if (next.endsWith("ing")) {
        let base = next.slice(0, -3);
        let baseE = base + "e";
        let baseDouble = base.slice(0, -1);
        if (englishToNari.has(base)) nextGerund = englishToNari.get(base);
        else if (englishToNari.has(baseE)) nextGerund = englishToNari.get(baseE);
        else if (next.length > 4 && base[base.length - 1] === base[base.length - 2] && englishToNari.has(baseDouble)) nextGerund = englishToNari.get(baseDouble);
      }
    }

    if (["am", "is", "are"].includes(lower) && nextGerund) {
      output.push("du", nextGerund);
      index += 1;
      continue;
    }

    let lowerGerund = null;
    if (gerundAliases.has(lower)) {
      lowerGerund = gerundAliases.get(lower);
    } else if (lower.endsWith("ing")) {
      let base = lower.slice(0, -3);
      let baseE = base + "e";
      let baseDouble = base.slice(0, -1);
      if (englishToNari.has(base)) lowerGerund = englishToNari.get(base);
      else if (englishToNari.has(baseE)) lowerGerund = englishToNari.get(baseE);
      else if (lower.length > 4 && base[base.length - 1] === base[base.length - 2] && englishToNari.has(baseDouble)) lowerGerund = englishToNari.get(baseDouble);
    }

    if (lowerGerund) {
      output.push("du", lowerGerund);
      continue;
    }
    let translated = englishAliases.get(lower) || englishToNari.get(lower);
    if (!translated && (lower.endsWith("s") || lower.endsWith("es"))) {
      let base = lower.endsWith("es") ? lower.slice(0, -2) : lower.slice(0, -1);
      if (englishToNari.has(base)) {
        let nariBase = englishToNari.get(base);
        translated = nariBase + "i";
      } else if (lower.endsWith("es") && englishToNari.has(lower.slice(0, -1))) {
        let nariBase = englishToNari.get(lower.slice(0, -1));
        translated = nariBase + "i";
      }
    }
    if (!translated && lower.endsWith("ed")) {
      let base = lower.slice(0, -2);
      let baseE = base + "e";
      let baseDouble = base.slice(0, -1);
      if (englishToNari.has(base)) {
        translated = englishToNari.get(base) + "a";
      } else if (englishToNari.has(baseE)) {
        translated = englishToNari.get(baseE) + "a";
      } else if (lower.length > 3 && base[base.length - 1] === base[base.length - 2] && englishToNari.has(baseDouble)) {
        translated = englishToNari.get(baseDouble) + "a";
      }
    }
    output.push(translated || `·${lower}`);
  }
  return joinTokens(output);
}

function translateNariToEnglish(text) {
  return joinTokens(tokenize(text).map((token) => {
    if (punctuation.has(token)) return token;
    const lower = token.toLowerCase();
    if (nariToEnglish.has(lower)) return nariToEnglish.get(lower);
    const tense = readTense(lower);
    if (tense) return tense;
    const plural = readPlural(lower);
    if (plural) return plural;
    return `·${lower}`;
  }));
}

function readTense(token) {
  if (token.length < 3) return "";
  const last = token.at(-1);
  const base = token.slice(0, -1);
  if (!nariToEnglish.has(base)) return "";
  const english = nariToEnglish.get(base);
  if (last === "a") return `did ${english}`;
  if (last === "u") return `will ${english}`;
  return "";
}

function tokenize(text) {
  return text.match(/[A-Za-z0-9-]+|[.,!?;:]/g) || [];
}

function joinTokens(tokens) {
  return tokens.reduce((line, token) => punctuation.has(token)
    ? `${line}${token}`
    : `${line}${line ? " " : ""}${token}`, "");
}

function loadDrill() {
  const lessonDrills = data.lessons.flatMap((lesson) =>
    lesson.drills.map((drill) => ({ ...drill, mode: lesson.title }))
  );
  const vocabPool = rows
    .filter((row) => !["Official Core", "Grammar Aliases"].includes(row.category) && row.english.length > 2)
    .map((row) => {
      const toNari = Math.random() < 0.5;
      return {
        mode: row.category,
        prompt: toNari ? `Translate to Nari: ${row.english}` : `What does ${row.nari} mean?`,
        answer: toNari ? row.nari : row.english,
      };
    });
  const allDrills = [...grammarDrills, ...lessonDrills, ...vocabPool];
  currentDrill = allDrills[Math.floor(Math.random() * allDrills.length)];
  drillMode.textContent = currentDrill.mode;
  drillPrompt.textContent = currentDrill.prompt;
  drillAnswer.value = "";
  drillFeedback.textContent = "Type your answer, then check it.";
  drillFeedback.className = "";
}

function checkCurrentDrill() {
  if (!currentDrill) loadDrill();
  const given = normalizeAnswer(drillAnswer.value);
  const expected = normalizeAnswer(currentDrill.answer);
  if (!given) {
    drillFeedback.textContent = "Try an answer first.";
    drillFeedback.className = "is-warn";
    return;
  }
  if (given === expected) {
    drillFeedback.textContent = `Correct: ${currentDrill.answer}`;
    drillFeedback.className = "is-correct";
  } else {
    drillFeedback.textContent = `Not quite. Answer: ${currentDrill.answer}`;
    drillFeedback.className = "is-warn";
  }
}

function normalizeAnswer(value) {
  return value.toLowerCase().trim().replace(/[.!?]/g, "").replace(/\s+/g, " ");
}

function readPlural(token) {
  if (token.length < 2 || !token.endsWith("i")) return "";
  const base = token.slice(0, -1);
  if (!nariToEnglish.has(base)) return "";
  return nariToEnglish.get(base) + "s";
}

function getRequestedTab() {
  const hash = location.hash.replace("#", "");
  return tabIds.includes(hash) && hash !== "" ? hash : "home";
}

function showTab(tabId) {
  tabPanels.forEach((panel) => {
    panel.classList.toggle("is-active", panel.id === tabId);
  });
  tabLinks.forEach((link) => {
    link.classList.toggle("is-active", link.dataset.tabLink === tabId);
  });
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function showStoryLevel(level) {
  storyPanels.forEach((panel) => {
    panel.classList.toggle("is-active", panel.id === `${level}StoryGrid`);
  });
  storyTabs.forEach((button) => {
    button.classList.toggle("is-active", button.dataset.storyLevel === level);
  });
  localStorage.setItem("nari_story_tab", level);
}

// --- Word Match Game ---
let matchSelected = null;
let matchPairs = [];
let matchMatched = 0;

function loadMatch() {
  const pool = rows.filter((r) => !r.english.includes(" ") && r.english.length > 2);
  const picked = shuffle(pool).slice(0, 6);
  matchPairs = picked;
  matchSelected = null;
  matchMatched = 0;
  matchScore.textContent = "0 matched";
  matchFeedback.textContent = "Tap a Nari word, then tap its English meaning.";

  const nariTiles = picked.map((r) => ({ text: r.nari, key: r.english, side: "nari" }));
  const engTiles  = picked.map((r) => ({ text: r.english, key: r.english, side: "eng" }));
  const allTiles  = shuffle([...nariTiles, ...engTiles]);

  matchGrid.innerHTML = allTiles.map((t) => `
    <button class="match-tile" data-key="${escapeHtml(t.key)}" data-side="${t.side}">${escapeHtml(t.text)}</button>
  `).join("");
}

matchGrid.addEventListener("click", (e) => {
  const tile = e.target.closest(".match-tile");
  if (!tile || tile.classList.contains("is-correct")) return;

  if (!matchSelected) {
    tile.classList.add("is-selected");
    matchSelected = tile;
    return;
  }

  if (matchSelected === tile) {
    tile.classList.remove("is-selected");
    matchSelected = null;
    return;
  }

  const sameKey = tile.dataset.key === matchSelected.dataset.key;
  const diffSide = tile.dataset.side !== matchSelected.dataset.side;

  if (sameKey && diffSide) {
    tile.classList.add("is-correct");
    matchSelected.classList.remove("is-selected");
    matchSelected.classList.add("is-correct");
    matchMatched += 1;
    matchScore.textContent = `${matchMatched} matched`;
    if (matchMatched === matchPairs.length) {
      matchFeedback.textContent = "Perfect! All matched. Start a new round!";
    }
    matchSelected = null;
  } else {
    tile.classList.add("is-wrong");
    matchSelected.classList.add("is-wrong");
    const prev = matchSelected;
    window.setTimeout(() => {
      tile.classList.remove("is-wrong", "is-selected");
      prev.classList.remove("is-wrong", "is-selected");
    }, 500);
    matchSelected = null;
  }
});

// --- Builder Game ---
let currentBuildSentence = null;

function loadBuilder() {
  buildDropzone.className = "build-dropzone";
  buildFeedback.textContent = "";
  buildDropzone.innerHTML = "";
  buildWordBank.innerHTML = "";
  checkBuildBtn.style.display = "block";
  nextBuildBtn.style.display = "none";
  
  const lessonPool = data.lessons.flatMap(l => l.examples);
  const storyPool = data.stories.flatMap(s => s.nari.map((n, i) => [n, s.english[i]]));
  const pool = [...lessonPool, ...storyPool].filter(ex => ex[0].split(" ").length > 2);
  
  if (!pool.length) return;
  const picked = pool[Math.floor(Math.random() * pool.length)];
  const nariText = picked[0].replace(/[.!?]/g, "");
  currentBuildSentence = { nari: nariText, english: picked[1] };
  
  buildPrompt.textContent = currentBuildSentence.english;
  
  let words = shuffle(nariText.split(" "));
  // Add some distractors
  const distractors = shuffle(["e", "su", "na", "be", "ta", "mi", "lisi", "ko", "dat"]).slice(0, 3);
  const allChips = shuffle([...words, ...distractors]);
  
  allChips.forEach(word => {
    const chip = document.createElement("button");
    chip.className = "build-chip";
    chip.type = "button";
    chip.textContent = word;
    chip.addEventListener("click", () => {
      if (chip.parentElement === buildWordBank) {
        buildDropzone.appendChild(chip);
      } else {
        buildWordBank.appendChild(chip);
      }
    });
    buildWordBank.appendChild(chip);
  });
}

checkBuildBtn.addEventListener("click", () => {
  if (!currentBuildSentence) return;
  const answer = Array.from(buildDropzone.children).map(c => c.textContent).join(" ");
  if (answer === currentBuildSentence.nari) {
    buildDropzone.classList.add("is-correct");
    buildFeedback.textContent = "Correct!";
    checkBuildBtn.style.display = "none";
    nextBuildBtn.style.display = "block";
  } else {
    buildDropzone.classList.remove("is-wrong");
    void buildDropzone.offsetWidth; // trigger reflow for animation
    buildDropzone.classList.add("is-wrong");
    buildFeedback.textContent = "Not quite. The correct sentence is: " + currentBuildSentence.nari;
    nextBuildBtn.style.display = "block";
  }
});

nextBuildBtn.addEventListener("click", loadBuilder);

let clozeState = "checking";

function loadCloze() {
  const lessonClozes = data.lessons.flatMap((lesson) =>
    lesson.examples
      .filter((example) => example[0].split(" ").length > 2)
      .map((example) => {
        const nariLine = example[0].replace(/[.!?]/g, "");
        const parts = nariLine.split(" ");
        const index = Math.min(parts.length - 1, Math.max(1, Math.floor(Math.random() * parts.length)));
        const answer = parts[index];
        parts[index] = "___";
        return { sentence: `${parts.join(" ")}.`, answer, hint: example[1] };
      })
  );
  const allClozes = [...clozeDrills, ...lessonClozes];
  currentCloze = allClozes[Math.floor(Math.random() * allClozes.length)];
  clozePrompt.textContent = currentCloze.sentence;
  clozeEnglish.textContent = currentCloze.hint;
  clozeAnswer.value = "";
  clozeAnswer.disabled = false;
  clozeFeedback.textContent = "Recall the missing word before checking.";
  clozeFeedback.className = "";
  clozeState = "checking";
  checkCloze.textContent = "Check";
  clozeAnswer.focus();
}

let choiceDirection = "en-nari";
function loadChoice() {
  const pool = rows.filter((row) =>
    !["Official Core", "Grammar Aliases"].includes(row.category) &&
    !row.english.includes(" ") &&
    row.english.length > 2
  );
  currentChoice = pool[Math.floor(Math.random() * pool.length)];
  if (choiceDirection === "en-nari") {
    const distractors = shuffle(pool.filter((row) => row.nari !== currentChoice.nari))
      .slice(0, 3).map((row) => row.nari);
    const options = shuffle([currentChoice.nari, ...distractors]);
    choicePrompt.textContent = `Choose the Nari word for: ${currentChoice.english}`;
    choiceOptions.innerHTML = options.map((option) => `
      <button class="choice-option" type="button" data-choice="${escapeHtml(option)}">${escapeHtml(option)}</button>
    `).join("");
  } else {
    const distractors = shuffle(pool.filter((row) => row.english !== currentChoice.english))
      .slice(0, 3).map((row) => row.english);
    const options = shuffle([currentChoice.english, ...distractors]);
    choicePrompt.textContent = `What does "${currentChoice.nari}" mean?`;
    choiceOptions.innerHTML = options.map((option) => `
      <button class="choice-option" type="button" data-choice="${escapeHtml(option)}">${escapeHtml(option)}</button>
    `).join("");
  }
  choiceFeedback.textContent = "Pick one answer.";
}

choiceOptions.addEventListener("click", (event) => {
  const button = event.target.closest("[data-choice]");
  if (!button || !currentChoice) return;
  const correctValue = choiceDirection === "en-nari" ? currentChoice.nari : currentChoice.english;
  const correct = button.dataset.choice === correctValue;
  button.classList.add(correct ? "is-correct" : "is-wrong");
  choiceFeedback.textContent = correct
    ? `Correct! ${currentChoice.english} = ${currentChoice.nari}`
    : `Not quite. ${currentChoice.english} = ${currentChoice.nari}`;
  window.setTimeout(loadChoice, 900);
});

function shuffle(items) {
  return [...items].sort(() => Math.random() - 0.5);
}





function checkClozeAnswer() {
  if (clozeState === "next") {
    loadCloze();
    return;
  }
  if (!currentCloze) loadCloze();
  const given = normalizeAnswer(clozeAnswer.value);
  const expected = normalizeAnswer(currentCloze.answer);
  
  if (given === expected) {
    clozeFeedback.textContent = "Correct!";
    clozeFeedback.className = "is-correct";
  } else {
    clozeFeedback.textContent = `Not quite. Answer: ${currentCloze.answer}`;
    clozeFeedback.className = "is-warn";
  }
  
  clozeState = "next";
  checkCloze.textContent = "Next";
  clozeAnswer.value = currentCloze.answer;
  clozeAnswer.disabled = true;
  clozePrompt.textContent = currentCloze.sentence.replace("___", currentCloze.answer);
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

try { renderVocabulary(); } catch (e) { console.error("renderVocabulary failed", e); }
try { translateText(); } catch (e) { console.error("translateText failed", e); }
try { loadDrill(); } catch (e) { console.error("loadDrill failed", e); }
try { loadCloze(); } catch (e) { console.error("loadCloze failed", e); }
try { loadChoice(); } catch (e) { console.error("loadChoice failed", e); }
try { initFlashCategories(); } catch (e) { console.error("initFlashCategories failed", e); }

try {
  const savedPracticeTab = localStorage.getItem("nari_practice_tab");
  if (savedPracticeTab) showPracticeMode(savedPracticeTab);
} catch (e) { console.error("practice tab init failed", e); }

try {
  const savedStoryTab = localStorage.getItem("nari_story_tab");
  if (savedStoryTab) showStoryLevel(savedStoryTab);
} catch (e) { console.error("story tab init failed", e); }

try { loadMatch(); } catch (e) { console.error("loadMatch failed", e); }

function goTab(id) {
  showTab(id);
  history.pushState(null, "", "#" + id);
}

function homeTranslate(text) {
  const out = document.querySelector("#homeTranslateOutput");
  if (!out) return;
  if (!text.trim()) {
    out.textContent = "Nari translation appears here";
    out.classList.remove("hp-has-result");
    return;
  }
  const words = text.trim().split(/\s+/);
  const parts = words.map(w => {
    const lower = w.toLowerCase().replace(/[^a-z]/g, "");
    if (!lower) return "";
    if (englishToNari.has(lower)) return englishToNari.get(lower);
    // try plural: if ends in 's', look up without s and add Nari plural suffix -i
    if (lower.endsWith("s") && lower.length > 2) {
      const singular = lower.slice(0, -1);
      if (englishToNari.has(singular)) return englishToNari.get(singular) + "i";
    }
    // skip unknowns cleanly
    return null;
  }).filter(p => p !== null && p !== "");
  const result = parts.join(" ").trim();
  if (result) {
    out.textContent = result;
    out.classList.add("hp-has-result");
  } else {
    out.textContent = "No matches yet - try common words like 'run', 'water', 'friend'";
    out.classList.remove("hp-has-result");
  }
}

showTab(getRequestedTab());
"""
    (ROOT / "script.js").write_text(js, encoding="utf-8")


def main() -> None:
    entries = build_entries()
    if len(entries) < 1000:
        raise SystemExit(f"Expected at least 1000 entries, got {len(entries)}")
    write_vocabulary(entries)
    write_grammar()
    write_data(entries)
    write_html()
    write_css()
    write_script()
    print(f"Generated Nari site with {len(entries)} vocabulary entries.")


if __name__ == "__main__":
    main()

input()



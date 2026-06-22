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
    "hello": "yo",
    "yes": "ye",
    "no": "nah",
    "okay": "ok",
    "thanks": "thx",
}


OFFICIAL.update({
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
    "ask": "asa",
    "answer": "anisa",
    "call": "kala",
    "join": "jona",
    "leave": "leva",
    "sell": "sela",
    "pay": "paya",
    "use": "uza",
    "try": "tira",
    "find": "fina",
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
    "door": "dora-n",
    "window": "wina-n",
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
    "tree": "tira-n",
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
    "silver": "siva-met",
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
    "sole": "sola-foot",
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
    "cold illness": "koda-sik",
    "allergy": "alerga",
    "bandage": "banda",
    "clinic": "klinika",
    "pharmacy": "farma",
    "toilet": "toila",
    "toothbrush": "tuth-brus",
    "toothpaste": "tuth-pas",
    "shampoo": "shampa",
    "deodorant": "deoda",
    "mirror": "mira-gla",
    "wallet": "wala",
    "receipt": "resita",
    "appointment": "aponta",
    "medicine pill": "medina-pil",
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
app audio battery browser camera channel charger chat code database download email file folder image keyboard laptop link login media message microphone mouse network password photo podcast printer profile screen search server tablet text upload website
""",
    "Money and Shopping": """
bank bill budget cash coin cost credit debt discount dollar fee gift income market price purchase rent sale saving shop store tax trade wallet receipt refund coupon checkout aisle cart basket appointment
""",
    "Time and Calendar": """
April August December February Friday January July June March Monday November October Saturday September Sunday Thursday Tuesday Wednesday century decade holiday minute moment month noon season second spring summer sunrise sunset week weekend winter year
""",
    "Feelings and Qualities": """
able angry awake calm careful clever comfortable confident cool curious cute dangerous dead dear dry empty fair false familiar fresh funny gentle glad healthy honest ill jealous kind lazy lonely loud lucky nervous normal open patient poor proud quiet rare rich serious sharp sick soft sweet tired useful warm wet wild wise wrong
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


def official_category(english: str) -> str:
    key = english.lower()
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
    "rain jacket": ("rain-jak", "clothing"),
    "sun glasses": ("sol-gala", "clothing"),
    "video call": ("vida-kala", "technology"),
    "online book": ("neta-buka", "technology"),
    "phone charger": ("tel-zuma", "technology"),
    "school bag": ("skul-bag", "school"),
    "coffee cup": ("kafa-kup", "food"),
    "water bottle": ("ven-botel", "food"),
    "work day": ("vora-day", "time"),
    "home town": ("dom-town", "place"),
    "story book": ("stori-buka", "media"),
    "night sky": ("nit-sky", "nature"),
    "sea wind": ("sea-wind", "nature"),
    "city road": ("siti-road", "travel"),
    "market price": ("mara-prisa", "money"),
    "family name": ("fam-nam", "people"),
    "heart beat": ("hart-bit", "body"),
    "first aid": ("first-ed", "health"),
    "ice cream": ("aisu-krem", "food"),
    "bus station": ("bus-station", "travel"),
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

sol + gala = sol-gala

sunglasses

rain + jak = rain-jak

rain jacket

vida + kala = vida-kala

video call

==================================================
33. INFORMAL SPEECH

yo = hello
ye = yes
nah = no
ok = okay
thx = thanks

==================================================
34. INTERNET SLANG

omg = oh my god
ong = on god
fr = for real
idk = I do not know
tbh = to be honest
imo = in my opinion
gg = good game
ez = easy
np = no problem
lol = laugh out loud
bruh = disbelief
rip = unfortunate

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
            "Mi opa wina-n e sena sol ovra tira-n.",
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
            "Mi su banda e medina-pil.",
            "Afta du day, rista be mor guda.",
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
    base = base.strip("-")
    candidate = base
    used = {entry["nari"] for entry in entries.values()}
    if candidate in used and not allow_duplicate_nari:
        stem = re.sub(r"[^a-z0-9]", "", category.lower())[:3] or "x"
        index = 2
        candidate = f"{base}-{stem}"
        while candidate in used:
            index += 1
            candidate = f"{base}-{stem}{index}"
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
      <a href="#translator" data-tab-link="translator">Translator</a>
      <a href="#practice" data-tab-link="practice">Practice</a>
      <a href="#stories" data-tab-link="stories">Stories</a>
      <a href="#grammar" data-tab-link="grammar">Rules</a>
      <a href="#vocabulary" data-tab-link="vocabulary">Vocabulary</a>
    </nav>
  </header>

  <main id="top">
    <section class="hero shell intro-panel" aria-hidden="true">
      <div class="hero-copy glass-panel">
        <p class="eyebrow">Minimal grammar, practical words</p>
        <h1>Nari</h1>
        <p class="lede">A polished quick-use language with stable grammar, readable stories, a translator, and a vocabulary rebuilt with less English-looking word shapes.</p>
        <div class="hero-actions">
          <a class="button primary" href="#translator">Translate</a>
          <a class="button secondary" href="#vocabulary">Browse words</a>
        </div>
      </div>
      <aside class="stats glass-panel" aria-label="Language stats">
        <div>
          <strong id="wordCount">1000+</strong>
          <span>vocabulary entries</span>
        </div>
        <div>
          <strong>39</strong>
          <span>grammar notes</span>
        </div>
        <div>
          <strong>4</strong>
          <span>short stories</span>
        </div>
      </aside>
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
        <button id="nextDrill" class="button secondary" type="button">Next drill</button>
      </div>
      <div class="practice-layout">
        <article class="practice-card glass-panel">
          <p id="drillMode" class="eyebrow">Translation drill</p>
          <h3 id="drillPrompt">Translate: my book</h3>
          <label class="practice-answer">
            <span>Your answer</span>
            <input id="drillAnswer" type="text" autocomplete="off" placeholder="Type in Nari">
          </label>
          <div class="practice-actions">
            <button id="checkDrill" class="button primary" type="button">Check</button>
            <p id="drillFeedback">Use the trainer to practice forms from the grammar and vocabulary.</p>
          </div>
        </article>
        <aside class="practice-card glass-panel">
          <p class="eyebrow">Focus</p>
          <ul class="practice-list">
            <li>Possessive pronouns: <span class="nari">mai</span>, <span class="nari">tai</span>, <span class="nari">mui</span></li>
            <li>Tense: <span class="nari">ko</span>, <span class="nari">koa</span>, <span class="nari">kou</span></li>
            <li>Word order: subject, verb, object</li>
            <li>Vocabulary recall from the full word bank</li>
          </ul>
        </aside>
      </div>
      <div class="flashcard-panel glass-panel">
        <div>
          <p class="eyebrow">Flashcards</p>
          <h3 id="flashPrompt">Loading card</h3>
          <p id="flashAnswer">Reveal the answer when ready.</p>
        </div>
        <div class="practice-actions">
          <button id="revealFlash" class="button primary" type="button">Reveal</button>
          <button id="gotFlash" class="button secondary" type="button">Got it</button>
          <button id="missFlash" class="button secondary" type="button">Missed</button>
          <p id="flashStats">0 reviewed</p>
        </div>
      </div>
      <div class="cloze-panel glass-panel">
        <div>
          <p class="eyebrow">Cloze recall</p>
          <h3 id="clozePrompt">mi ___ al dom.</h3>
          <p id="clozeHint">Fill the missing Nari word from context.</p>
        </div>
        <label class="practice-answer">
          <span>Missing word</span>
          <input id="clozeAnswer" type="text" autocomplete="off" placeholder="Type one word">
        </label>
        <div class="practice-actions">
          <button id="checkCloze" class="button primary" type="button">Check</button>
          <button id="nextCloze" class="button secondary" type="button">Next cloze</button>
          <p id="clozeFeedback">Active recall beats rereading.</p>
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
          <p><span class="nari">vida-kala</span> video call.</p>
          <p><span class="nari">sol-gala</span> sunglasses.</p>
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
const rows = data.entries;
const tabIds = ["translator", "practice", "stories", "grammar", "vocabulary"];
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
const flashPrompt = document.querySelector("#flashPrompt");
const flashAnswer = document.querySelector("#flashAnswer");
const revealFlash = document.querySelector("#revealFlash");
const gotFlash = document.querySelector("#gotFlash");
const missFlash = document.querySelector("#missFlash");
const flashStats = document.querySelector("#flashStats");
const clozePrompt = document.querySelector("#clozePrompt");
const clozeHint = document.querySelector("#clozeHint");
const clozeAnswer = document.querySelector("#clozeAnswer");
const checkCloze = document.querySelector("#checkCloze");
const nextCloze = document.querySelector("#nextCloze");
const clozeFeedback = document.querySelector("#clozeFeedback");

const englishToNari = new Map(rows.map((row) => [row.english.toLowerCase(), row.nari]));
const nariToEnglish = new Map(rows.map((row) => [row.nari.toLowerCase(), row.english.toLowerCase()]));
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
let reviewedCards = 0;
let missedCards = 0;
let currentCloze = null;

const grammarDrills = [
  { mode: "Possessive pronouns", prompt: "Translate: my book", answer: "mai buka" },
  { mode: "Possessive pronouns", prompt: "Translate: your house", answer: "tai dom" },
  { mode: "Possessive pronouns", prompt: "Translate: our phone", answer: "mui tel" },
  { mode: "To be", prompt: "Translate: I am at home", answer: "mi be al dom" },
  { mode: "Possession with ov", prompt: "Translate: book of me", answer: "buka ov mi" },
  { mode: "Tense", prompt: "Translate: I went home", answer: "mi koa dom" },
  { mode: "Tense", prompt: "Translate: I will go tomorrow", answer: "mi kou la tomd" },
  { mode: "Negation", prompt: "Translate: I do not know", answer: "mi na ni" },
  { mode: "Word order", prompt: "Translate: she reads a book", answer: "lis re buka" },
  { mode: "Modals", prompt: "Translate: you must study", answer: "ta musu suma" },
  { mode: "Continuous action", prompt: "Translate: we are working", answer: "mu du vora" },
  { mode: "Colors", prompt: "Translate to Nari: blue", answer: "sanu" },
  { mode: "Colors", prompt: "Translate to Nari: turquoise", answer: "turka" },
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
];

wordCount.textContent = data.entryCount.toLocaleString();

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

const categories = ["All", ...Array.from(new Set(rows.map((row) => row.category))).sort()];
categoryChips.innerHTML = categories.map((category) => `
  <button class="chip${category === "All" ? " is-active" : ""}" type="button" data-category="${escapeHtml(category)}">
    ${escapeHtml(category)}
  </button>
`).join("");

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
revealFlash.addEventListener("click", revealFlashcard);
gotFlash.addEventListener("click", () => scoreFlashcard(false));
missFlash.addEventListener("click", () => scoreFlashcard(true));
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

function renderVocabulary() {
  const filtered = getFilteredRows();
  const visible = filtered.slice(0, state.limit);
  vocabRows.innerHTML = visible.length ? visible.map((row) => `
    <tr>
      <td>${escapeHtml(row.nari)}</td>
      <td>${escapeHtml(row.english)}</td>
      <td>${escapeHtml(row.category)}</td>
    </tr>
  `).join("") : `
    <tr>
      <td colspan="3" class="empty-cell">No matching words yet. Try a broader search or another category.</td>
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
    if (lower === "at" && next === "home") {
      output.push("al", "dom");
      index += 1;
      continue;
    }
    if (["am", "is", "are"].includes(lower) && gerundAliases.has(next)) {
      output.push("du", gerundAliases.get(next));
      index += 1;
      continue;
    }
    if (gerundAliases.has(lower)) {
      output.push(gerundAliases.get(lower));
      continue;
    }
    output.push(englishAliases.get(lower) || englishToNari.get(lower) || `·${lower}`);
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
  const useGrammar = Math.random() < 0.65;
  if (useGrammar) {
    currentDrill = grammarDrills[Math.floor(Math.random() * grammarDrills.length)];
  } else {
    const pool = rows.filter((row) => row.category !== "Official Core" && !row.english.includes(" "));
    const row = pool[Math.floor(Math.random() * pool.length)];
    currentDrill = {
      mode: "Vocabulary recall",
      prompt: `Translate to Nari: ${row.english}`,
      answer: row.nari,
    };
  }
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

function getRequestedTab() {
  const hash = location.hash.replace("#", "");
  return tabIds.includes(hash) ? hash : "translator";
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
}

function loadFlashcard() {
  const usefulCategories = new Set([
    "Body and Health",
    "Colors",
    "Food and Drink",
    "Home and Daily Life",
    "Common Verbs",
    "People and Society",
    "Technology and Media",
    "Money and Shopping",
  ]);
  const pool = rows.filter((row) =>
    usefulCategories.has(row.category) &&
    !row.english.includes(" ") &&
    row.english.length > 2
  );
  currentFlash = pool[Math.floor(Math.random() * pool.length)];
  flashPrompt.textContent = currentFlash.english;
  flashAnswer.textContent = "Reveal the answer when ready.";
}

function revealFlashcard() {
  if (!currentFlash) loadFlashcard();
  flashAnswer.textContent = currentFlash.nari;
}

function scoreFlashcard(missed) {
  reviewedCards += 1;
  if (missed) missedCards += 1;
  flashStats.textContent = `${reviewedCards} reviewed, ${missedCards} missed`;
  loadFlashcard();
}

function loadCloze() {
  currentCloze = clozeDrills[Math.floor(Math.random() * clozeDrills.length)];
  clozePrompt.textContent = currentCloze.sentence;
  clozeHint.textContent = currentCloze.hint;
  clozeAnswer.value = "";
  clozeFeedback.textContent = "Recall the missing word before checking.";
  clozeFeedback.className = "";
}

function checkClozeAnswer() {
  if (!currentCloze) loadCloze();
  const given = normalizeAnswer(clozeAnswer.value);
  const expected = normalizeAnswer(currentCloze.answer);
  if (given === expected) {
    clozeFeedback.textContent = `Correct: ${currentCloze.answer}`;
    clozeFeedback.className = "is-correct";
  } else {
    clozeFeedback.textContent = `Not quite. Answer: ${currentCloze.answer}`;
    clozeFeedback.className = "is-warn";
  }
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

renderVocabulary();
translateText();
loadDrill();
loadFlashcard();
loadCloze();
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




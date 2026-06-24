const data = window.NARI_DATA;
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

const data = window.NARI_DATA;
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

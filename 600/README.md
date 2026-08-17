# 600 — Daily Discovery (GitHub Pages)

**Live site:** `https://<your-username>.github.io/600/` (after deploy)

## What it does

- **600-word essay** every day, unlocking at **3:00 PM Korea time**
- **5 advanced vocabulary words** — click or 🔊 to hear pronunciation
- **Comprehension quiz** with hints, first-try tracking, report card
- **Share button** — copies ~100-word WhatsApp message
- **7-day strip** — future days greyed with titles only
- **Sunday 8:00 AM KST** — GitHub Action generates a fresh week (no repeats)

## Deploy to GitHub Pages

### Option A — Repo named `600` (cleanest URL)

```bash
cd omi4th
git init
git add 600/ .github/workflows/600-*.yml
git commit -m "Add 600 daily reading app"
gh repo create 600 --public --source=. --push
```

Then in GitHub → **Settings → Pages → Build: GitHub Actions**

### Option B — Subfolder in existing repo

Push `omi4th` repo; the deploy workflow publishes the `600/` folder as the site root when triggered.

## Local preview

```bash
cd 600
npx --yes serve .
# Open http://localhost:3000
```

## Regenerate week manually

```bash
node 600/scripts/generate-week.js
```

## Add more essays (no repeats)

1. Add new objects to `600/scripts/essay-bank.json` (unique `id`, unique vocab words)
2. Run `generate-week.js` or wait for Sunday cron
3. `state.json` tracks used essay IDs, words, and topics

## Files

| Path | Purpose |
|------|---------|
| `index.html` | App shell |
| `js/app.js` | Unlock logic, quiz, share, speech |
| `data/week.json` | Current week's 7 essays |
| `data/state.json` | Used words/topics/essays |
| `scripts/essay-bank.json` | Master essay library |
| `scripts/generate-week.js` | Weekly generator |
| `TENETS.md` | Design principles |

## Automations

| Workflow | Schedule | Action |
|----------|----------|--------|
| `600-weekly-refresh.yml` | Sun 8 AM KST | Generate + commit new week |
| `600-deploy-pages.yml` | On push to main | Deploy to GitHub Pages |

Daily 3 PM rotation is **client-side** (KST) — no server needed.

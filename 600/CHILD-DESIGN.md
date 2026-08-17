# Child Design Principles — 600 App

Reviewed against research from developmental psychology, literacy education, and children's UX.

## Curiosity (Hidi & Renninger)

- **Mystery hook before reading** — "Before you read…" curiosity question opens a knowledge gap
- **Wonder pauses in story** — every 3 paragraphs, a "Pause — what surprised you?" prompt
- **Family questions** — relatedness (SDT): ask grandparents/parents

## Cognitive load (Sweller)

- **4-step journey** — Wonder → Words → Story → Quiz (never all at once)
- **One quiz question per screen** — working memory friendly for age 9
- **Vocab carousel** — one word card at a time on phone/tablet

## Autonomy & competence (Self-Determination Theory)

- Kid chooses when to move forward ("Let's go!", "I'm ready for the quiz")
- Progress bar shows reading % and top journey bar shows step completion
- Green ✓ on completed days — visible mastery

## Growth mindset (Dweck)

- Wrong answers: "Scientists miss things all the time" — never shame
- Second wrong: story-based hint with answer embedded — success guaranteed
- Celebrate completion, not perfection

## Responsive / tablet UX

- `clamp()` fluid typography — readable on phone, iPad, desktop
- Week strip: horizontal scroll + snap on mobile; grid on desktop
- 48px+ tap targets (Apple HIG / WCAG)
- Bottom nav on mobile/tablet; hidden on desktop
- `100dvh`, safe-area insets for notched phones
- `prefers-reduced-motion` respected

## Voice

- Prioritises natural voices (Samantha, Karen, Google UK Female)
- Slower rate, slightly higher pitch — warmer for children
- Separate flows: word, encourage, hint, celebrate

## PWA

- Add to Home Screen → standalone app feel
- White/black high-contrast — clean, not babyish

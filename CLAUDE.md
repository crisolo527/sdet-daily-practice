# SDET Daily Practice — Project Context

## Who I am

I'm a mid-level SDET (Software Developer in Test) working daily practice to grow into a senior/staff SDET or QA Architect role. This repo is both a learning log and a portfolio artifact I can point to from my resume/LinkedIn.

## Background context (for calibrating question difficulty/relevance)

I work with an internal AI test-case generation tool (Python/Streamlit based), YouTrack for ticketing, and Squash TM for test case management. I'm also involved in agentic testing pipeline evaluation work (multi-agent validation pipelines, LLM-output evaluation frameworks like DeepEval, MCP-based tool integrations). Phase 4 questions below should build on this real experience rather than starting from scratch.

## Format

- Daily: 1 technical/coding lesson \+ 1 process/conceptual QA lesson, each followed by a hands-on exercise.
- Lesson-first, not cold-quiz: each day teaches the concept with a worked example *before* asking me to apply it. I'm building from limited footing, so I need the concept explained and demonstrated first, not just prompted blind.
- Weekly theme: each week focuses on one topic (e.g. "API testing", "flaky tests") so the two daily lessons reinforce each other instead of being disconnected trivia.
- Time budget: \~10 min for the coding exercise, \~15-20 min for the conceptual one (written as a short paragraph, not just thought about).
- Technical files go in their real file extension (`.py`, `.js`, etc.) so the repo doubles as a runnable code sample, not just prose. Structure:
  1. **Concept + pattern** — brief note on the technique being practiced.
  2. **Worked example** — one fully-solved example, commented, showing the technique applied.
  3. **Your exercise** — a related but different problem, TODO stubs only (not a repeat of the worked example — the point is to build the muscle, not copy the pattern).
- Conceptual files go in markdown; mermaid diagrams welcome if sketching architecture helps. Structure:
  1. **Concept** — short plain-language explanation.
  2. **Worked example** — one fully-solved example applying the concept.
  3. **Your turn** — a related question for me to answer in my own words.
  4. **Answer** — where I write my response.

## Repo structure

sdet-daily-practice/

  README.md                        \<- index/table of contents, links to each week

  phase-1-foundations/

    week-01-\<topic\>/

      day1-technical.py

      day1-conceptual.md

      day2-technical.py

      day2-conceptual.md

  phase-2-automation-architecture/

  phase-3-infrastructure-nfr/

  phase-4-specialization-leadership/

## Current position

Update this line every time you move forward — Claude Code should not have to infer it from folder contents alone.

**Phase 1, Week 1 — not yet started.**

## The 4-phase progression plan

### Phase 1 — Foundations reinforcement

Goal: no gaps under you before you build up.

- Technical: DS/algorithms with a testing lens — write a function *and* its test suite; debug a broken function via test-first thinking.  
- Conceptual: equivalence partitioning, boundary value analysis, test pyramid vs. testing trophy, risk-based test prioritization.

### Phase 2 — Automation architecture & frameworks

Goal: go from "writes tests" to "designs test systems."

- Technical: Page Object Model and its critiques, custom test fixtures, API test clients, contract testing basics (Pact-style), test data builders/factories.  
- Conceptual: mock vs. real dependencies, flaky test root-causing, structuring a test suite for a 10-person team, test ownership models.

### Phase 3 — Infrastructure, CI/CD, and non-functional testing

Goal: the stuff that separates mid from senior SDET.

- Technical: CI pipeline stages, parallelizing test runs, basic load-testing scripts, security testing fundamentals (OWASP-style categories).  
- Conceptual: shift-left vs. shift-right strategy, observability for test failures, cost/speed/ coverage tradeoffs, advocating for quality investment to non-QA stakeholders.

### Phase 4 — Specialization \+ leadership

- Technical: designing an AI-assisted test generation pipeline, evaluating LLM output quality, agent-based test validation architecture.  
- Conceptual: system design interviews framed around test infrastructure ("design a test execution platform for 500 engineers"), mentoring/leading QA process change, writing an ADR for a testing tool choice.

## File & commit checkpoints

- **Starting a day:** when I say "give me today's question," create `dayN-technical.<ext>` and `dayN-conceptual.md` in the current week folder immediately, even before I've answered — they act as the placeholder/prompt.
- **Finishing a day:** when I say "I finished day N," confirm both files are saved and non-empty before reviewing. Then commit with message `day N: <topic> - technical + conceptual`.
- **Finishing a week:** update the README.md index, then commit `week N complete: <theme>`.
- **Finishing a phase:** update "Current position" below, commit `phase N complete`. If `progress-log.md` doesn't exist yet at the repo root, create it (with a one-line header). Append a short retro entry (2-3 sentences: what was hard, what to revisit) — draft it from our conversation and let me edit before committing.
- **Missed days:** don't backfill or guilt-trip me about gaps — just resume at the next day when I'm ready.
- Time budgets above are loose targets, not hard stops — some days will run faster or slower depending on difficulty. Don't flag or comment on time spent.

## Link to the portfolio framework project

I'm also building a separate flagship repo: a full-stack Python test automation framework (pytest + Playwright + GitHub Actions + Allure, targeting a public demo e-commerce site), structured as a 6-module course (setup → API testing → UI/E2E → AI agent testing → CI/CD → reporting/polish).

- Before generating today's question, check whether it overlaps with the module I'm currently on in that framework repo (e.g. a Phase 2 "Page Object Model" daily question while I'm on framework Module 3).
- **If it overlaps:** don't create throwaway daily practice files for it. Instead, prompt me to apply the answer directly inside the framework repo (real code, real progress) — then just log a one-line pointer in the day's conceptual file noting it was done there instead, with the framework file path.
- **If it doesn't overlap:** proceed as normal — create the day's files in `sdet-daily-practice/` per the checkpoints below.
- Flag Phase 4 outputs (ADRs, system design answers, AI-pipeline write-ups) explicitly when generated — these and the framework repo are the primary resume/portfolio candidates.
- `progress-log.md` tracks both: daily-practice phase retros AND framework module-completion entries, so there's one combined checkpoint log instead of two separate ones.



- When I say "give me today's question," generate 1 technical \+ 1 conceptual question matching my current phase/week/theme above, and create the day's files in the right week folder (see checkpoints above).  
- When I say "I finished day N," review my answer files, give feedback, and propose the next day's question set (staying within the current week's theme until I say to move on).  
- Keep the README.md index up to date as new weeks are added.  
- Remind me to update "Current position" above when a week/phase completes.
- Follow the file & commit checkpoints above without me having to ask each time.

## Glossary

`glossary.md` at the repo root is a running term/definition table (markdown,
easy to export as CSV) covering vocabulary introduced across all conceptual
lessons — I study it on mobile via RemNote (imported as flashcards).

- Whenever a day's conceptual lesson introduces a new term (in the Concept
  section), append it to `glossary.md` as part of creating that day's files —
  don't wait for me to ask.
- Include it in the day's commit rather than a separate one.


# Day 3 — Conceptual

**Theme:** Test fundamentals (Week 1)
**Time budget:** ~15-20 min

## 1) Concept

**Risk-based test prioritization** means you don't test everything equally
hard — you decide *how much* testing effort a feature/area deserves based
on its risk, where risk is roughly:

  risk ≈ likelihood of failure × impact if it fails

"Likelihood" considers things like: how complex/new is the code, how often
does it change, how many people touch it, has it broken before. "Impact"
considers: how many users does it affect, is it revenue/compliance/safety
critical, how visible is the failure (silent data corruption vs. a loud
crash), how hard is it to recover from.

This matters because test time is always finite. Risk-based prioritization
is the deliberate answer to "what do I test first / most / at all" — as
opposed to testing whatever's easiest to test, or spreading effort evenly
across features regardless of how much any one of them actually matters.

## 2) Worked example

Imagine you're testing an e-commerce checkout flow with three features
shipping this sprint:
1. Payment processing (charges a real credit card)
2. A "recently viewed items" carousel on the homepage
3. A new discount-code redemption feature

Risk assessment:
- **Payment processing**: high likelihood of subtle bugs (integrates with
  an external gateway, handles many edge cases like declined cards/partial
  refunds) and catastrophic impact if wrong (charge the wrong amount, charge
  twice, or fail to charge while shipping the order) → highest priority,
  deserves deep EP/BVA coverage, integration tests against a sandboxed
  gateway, and manual exploratory testing before release.
- **Discount codes**: new feature (higher likelihood of bugs than proven
  code) but moderate impact (wrong discount is bad but recoverable, and
  blast radius is smaller than a payment failure) → solid test coverage,
  but doesn't need the same exhaustive treatment as payment.
- **Recently viewed carousel**: low likelihood (simple, well-understood UI
  pattern) and low impact (cosmetic — nobody's order breaks if this glitches)
  → light smoke testing is enough; not worth deep edge-case coverage.

Risk-based prioritization is why a mid-level SDET wouldn't spend equal time
on all three — it's a conscious tradeoff, not a shortcut.

## 3) Your turn

Think about the multi-agent validation/agentic testing pipeline work you've
mentioned (LLM-output evaluation, MCP-based tool integrations). Pick two
components from that kind of system that you think carry meaningfully
different risk levels (e.g. the step that calls the LLM vs. the step that
formats output for a downstream system, or a validation agent vs. a
logging/telemetry step). Walk through your risk reasoning for each —
likelihood and impact — and say what different level/kind of testing effort
each one deserves as a result.

Write a short paragraph or two — not just bullet points.

## Answer

(write your response here)
# Day 2 — Conceptual

**Theme:** Test fundamentals (Week 1)
**Time budget:** ~15-20 min

## 1) Concept

The **test pyramid** is a model for how to allocate testing effort across
layers: lots of fast, cheap **unit tests** at the base, fewer **integration
tests** in the middle, and a small number of slow, expensive **end-to-end
(E2E) tests** at the top. The shape argues for cost/speed reasons — unit
tests are fast and pinpoint failures precisely, E2E tests are slow, flaky,
and expensive to maintain, so you want as few of them as still gives you
confidence.

The **testing trophy** (popularized by Kent C. Dodds) is a reaction to that
model for modern apps, especially ones with a lot of integration surface
(APIs, UI components wired together, third-party services). It reshapes the
pyramid into a trophy: still relatively few E2E tests at the top and a
small base of unit tests, but the *bulk* of testing effort sits in
**integration tests** in the middle — because for many real systems, bugs
live at the seams between units, not inside a single function, and heavily
unit-testing every small piece can give false confidence while missing
integration-level breakage.

Neither model is universally "correct" — the right shape depends on where
your system's bugs actually tend to live and how expensive each test layer
is to write/maintain/run in your specific stack.

## 2) Worked example

Say you're testing a checkout flow: `validate_cart()` (pure logic),
`PaymentService.charge()` (calls a payment gateway), and `POST /checkout`
(API endpoint wiring cart validation + payment + order creation).

Pyramid-style allocation:
- Unit tests: `validate_cart()` edge cases (empty cart, invalid coupon,
  negative quantity) — dozens of fast tests.
- Integration tests: a handful verifying `POST /checkout` calls
  `PaymentService` correctly with a mocked gateway.
- E2E tests: one or two full browser-driven checkouts against a staging
  environment.

Trophy-style allocation for the same feature would keep the unit tests for
pure logic like `validate_cart()`, but invest much more heavily in
integration tests — e.g. spinning up the real API with a sandboxed/test
payment gateway and hitting `POST /checkout` directly for a wide range of
scenarios (declined card, expired coupon, out-of-stock item) — because the
riskiest bugs are in how validation, payment, and order creation interact,
not in any single function alone. E2E stays minimal, reserved for a couple
of true "does the whole system work" smoke checks.

## 3) Your turn

Think about the AI test-case generation tool or the agentic testing
pipeline work you've described (multi-agent validation, LLM-output
evaluation). Does that system's risk profile look more like a pyramid or a
trophy to you — i.e., where do you think bugs are most likely to actually
originate: inside a single function/component, at the integration seams
between components (e.g. between an LLM call and the pipeline logic
consuming its output), or only visible end-to-end? Explain your reasoning,
and describe what an appropriate test-layer allocation might look like for
that system.

Write a short paragraph or two — not just bullet points.

## Answer

In our AI test case generation tool, I think the system is closer to a test trophy. This is beacuse the logic is that we integrate three main systems together for this tool to work. First, it is retrieving the YouTrack tickets which is what the test cases will be based off of and we have to retrieve and pass that data to the LLM. Then, we have to correctly pass the results of the LLM in a specific format for the Squash API that creates and holds the test cases. Finally this is done through a UI wich the user provides info for us to do all of this. There are many interconnected parts including recording specific records in our database. I have expecrienced many issues and resolved many of them some including the UI breaking because we forgot to handle an error validation case from anywhere in the backend logic. Other errors would be hidden an the UI says it is correct but it is actually breaking in the backend because no test cases were output from the LLM side but the run was successful. Mostly integration tests from all the interconnected parts were the primary issues we've found.

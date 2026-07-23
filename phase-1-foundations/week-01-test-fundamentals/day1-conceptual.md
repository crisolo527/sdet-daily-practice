# Day 1 — Conceptual

**Theme:** Test fundamentals (Week 1)
**Time budget:** ~15-20 min

## 1) Concept

**Equivalence partitioning (EP)** is the idea that you can't (and shouldn't)
test every possible input — instead you group inputs into "partitions" that
the system under test *should* treat the same way, and test one
representative value from each group. A partition can be a valid group
(inputs that should succeed) or an invalid group (inputs that should be
rejected).

**Boundary value analysis (BVA)** is a refinement of EP: bugs disproportionately
hide at the *edges* between partitions (off-by-one errors, `<` vs `<=`,
empty-input handling), so instead of picking any representative value from a
partition, you deliberately test the value right at a boundary, one just
below it, and one just above it.

They're not competing techniques — EP tells you *where the groups are*, BVA
tells you *which values inside those groups are worth testing first*.

## 2) Worked example

Take a function `set_password(pw: str) -> bool` with the spec: "password
must be 8-20 characters."

Equivalence partitions:
- too short (< 8 chars) — invalid
- valid length (8-20 chars) — valid
- too long (> 20 chars) — invalid

Boundaries (the interesting edges between those partitions):
- length 7 (just under) — invalid
- length 8 (lower boundary) — valid
- length 20 (upper boundary) — valid
- length 21 (just over) — invalid

Notice EP alone might tempt you to test one "too short" case like length 3
and call it done. BVA pushes you to test length 7 specifically, because
that's the value most likely to expose an off-by-one bug like `if len(pw) <
8` accidentally written as `if len(pw) <= 8`.

## 3) Your turn

Using the `is_balanced()` function from today's technical exercise as your
example: what are its equivalence partitions, and does it have any
meaningful "boundaries" the way a numeric range does? (Hint: BVA doesn't
only apply to numbers — think about what "edge cases" mean for a string/
structural problem instead of a numeric one.)

Then, describe one real situation from your own testing work (the AI
test-case generation tool, an API you've tested, anything) where skipping
EP or BVA let a bug slip through, or where applying it caught something a
happy-path test would have missed.

Write a short paragraph or two — not just bullet points.

## Answer

pt.1 

For the is_balanced function its equivalence partitions are different from the first string example in the sense that the main partitions are the presence of matching brackets(True), incomplete or broken brackets(False), or no brackets at all(True). The bondary value analysis of these partitions are an empty string(True), a single pair of completed brackets(True), a single open bracket(False), and a single closing bracket(False).

pt.2

At work, I applied equivalence partitioning and boundary analysis to make sure that the test case generation tool we have was still backwards compatible after we updated a feature. For example, we moved off of a requirement where tickets had to be formatted a certain way before generating test cases. This improved the tool but I had to make sure the partitions were covered so that both the past feature and new feature were covered properly. The partitions were to be that the ticket was not formatted at all like the previous requiement had, the ticket had some formatting from the past, and the ticket had the full formatted version as before. Essentially, all partitions still had to work through the tool after our overall improvements removing that hard requirement.

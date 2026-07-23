"""
Phase 1, Week 1 — Day 1 (Technical)
Theme: Test fundamentals (equivalence partitioning / boundary value analysis)
Time budget: ~10 min

=====================================================================
1) CONCEPT + PATTERN
=====================================================================
Equivalence partitioning (EP) splits a function's possible inputs into
groups ("partitions") that the function *should* treat the same way.
Instead of testing every possible input, you test one representative
value from each partition.

Boundary value analysis (BVA) then zooms in on the edges *between*
partitions — off-by-one errors love to hide exactly there. For any
partition with a numeric or length-based edge, test the boundary value,
one below it, and one above it.

The pattern for turning a function into a test suite:
  1. Read the spec, list the input partitions (valid groups, invalid
     groups, edge/empty groups).
  2. For each partition, pick one representative value.
  3. For each boundary between partitions, add boundary-value tests.
  4. Write one assert per case, and name the test after the partition
     it covers so failures are self-explanatory.

=====================================================================
2) WORKED EXAMPLE
=====================================================================
Function under test: clamp(value, low, high) -> int
Returns `value` restricted to the inclusive range [low, high].

Partitions:
  - value below low        -> should return low
  - value above high        -> should return high
  - value inside range      -> should return value unchanged
Boundaries:
  - value == low            -> should return low (boundary itself is valid)
  - value == high           -> should return high (boundary itself is valid)
  - value == low - 1        -> just outside, should clamp to low
  - value == high + 1       -> just outside, should clamp to high
"""


def clamp(value: int, low: int, high: int) -> int:
    if value < low:
        return low
    if value > high:
        return high
    return value


# --- worked example test suite ---

def test_clamp_below_range():
    # partition: value below low
    assert clamp(-5, 0, 10) == 0


def test_clamp_above_range():
    # partition: value above high
    assert clamp(15, 0, 10) == 10


def test_clamp_inside_range():
    # partition: value inside range
    assert clamp(5, 0, 10) == 5


def test_clamp_at_low_boundary():
    # boundary: value == low
    assert clamp(0, 0, 10) == 0


def test_clamp_at_high_boundary():
    # boundary: value == high
    assert clamp(10, 0, 10) == 10


def test_clamp_just_below_low():
    # boundary: value == low - 1
    assert clamp(-1, 0, 10) == 0


def test_clamp_just_above_high():
    # boundary: value == high + 1
    assert clamp(11, 0, 10) == 10


"""
=====================================================================
3) YOUR EXERCISE
=====================================================================
Implement `is_balanced(expression: str) -> bool`, which returns True if
all brackets in the string are balanced and correctly nested. Supported
bracket pairs: (), [], {}. Any other characters in the string should be
ignored.

Example:
    is_balanced("({[]})")   -> True
    is_balanced("([)]")     -> False
    is_balanced("")         -> True   (edge case — think about why)

Using the same EP/BVA pattern from the worked example above:
  1. List this function's input partitions and boundaries as a comment.
  2. Implement the function.
  3. Write a test suite covering each partition/boundary you listed —
     one test per case, named after what it covers.

This is a different problem from the worked example (string/structural
validity instead of numeric range), so don't just copy the shape of the
clamp() tests — think through is_balanced()'s own partitions first.
"""


def is_balanced(expression: str) -> bool:
    """
    Partitions:
        - expression with no brackets           -> should return True
        - expression with balanced brackets     -> should return True
        - expression with unbalanced brackets   -> should return False
    Boundaries:
        - expression == ""          -> should return True (edge case)
        - expression == "()"        -> should return True (boundary itself is valid)
        - expression == "("         -> should return False (just outside, unbalanced)
        - expression == ")"         -> should return False (just outside, unbalanced)
    """
    stack = []
    bracket_map = {
        ')': '(', 
        ']': '[', 
        '}': '{'
    }

    for char in expression:
        if char in bracket_map.values():  # opening brackets
            stack.append(char)
        elif char in bracket_map.keys():  # closing brackets
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop() 

    return len(stack) == 0


def test_is_balanced_no_brackets():
    # partition: expression with no brackets
    assert is_balanced("abc") is True

def test_is_balanced_balanced_brackets():
    # partition: expression with balanced brackets
    assert is_balanced("({[]})") is True

def test_is_balanced_unbalanced_brackets():
    # partition: expression with unbalanced brackets
    assert is_balanced("([)]") is False

def test_is_balanced_empty_string():
    # boundary: expression == ""
    assert is_balanced("") is True

def test_is_balanced_single_pair():
    # boundary: expression == "()"
    assert is_balanced("()") is True

def test_is_balanced_single_open():
    # boundary: expression == "("
    assert is_balanced("(") is False

def test_is_balanced_single_close():
    # boundary: expression == ")"
    assert is_balanced(")") is False

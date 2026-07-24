"""
Phase 1, Week 1 — Day 3 (Technical)
Theme: Test fundamentals (data structures/algorithms with a testing lens)
Time budget: ~10 min

=====================================================================
1) CONCEPT + PATTERN
=====================================================================
This week you've practiced EP/BVA (Day 1) and test-first debugging
(Day 2). Today combines both: implement a small algorithm yourself
*and* write its test suite, using the same EP/BVA process to decide
what to test — but this time there's no reference implementation to
debug against. You have to trust your own partitions to catch your
own bugs.

The pattern is the same as Day 1/2:
  1. Read the spec, list input partitions (valid/invalid/edge groups).
  2. Identify boundaries between partitions.
  3. Implement the function.
  4. Write one test per partition/boundary, run it, and fix anything
     that fails — your tests are now the spec-check, not a debugging
     aid for someone else's code.

=====================================================================
2) WORKED EXAMPLE
=====================================================================
Function under test: binary_search(sorted_list: list[int], target: int) -> int
Returns the index of `target` in `sorted_list` if present, else -1.

Partitions:
  - target present in list        -> return its index
  - target absent from list       -> return -1
  - empty list                    -> return -1
Boundaries:
  - target is first element       -> return 0
  - target is last element        -> return len(list) - 1
  - single-element list, present  -> return 0
  - single-element list, absent   -> return -1
"""


def binary_search(sorted_list, target):
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# --- worked example test suite ---

def test_binary_search_present():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_binary_search_absent():
    assert binary_search([1, 3, 5, 7, 9], 4) == -1


def test_binary_search_empty_list():
    assert binary_search([], 5) == -1


def test_binary_search_first_element():
    assert binary_search([1, 3, 5, 7, 9], 1) == 0


def test_binary_search_last_element():
    assert binary_search([1, 3, 5, 7, 9], 9) == 4


def test_binary_search_single_element_present():
    assert binary_search([5], 5) == 0


def test_binary_search_single_element_absent():
    assert binary_search([5], 1) == -1


"""
=====================================================================
3) YOUR EXERCISE
=====================================================================
Implement `first_unique_char(s: str) -> int`, which returns the index
of the first character in `s` that does not repeat anywhere else in
the string. If no such character exists, return -1.

Example (per spec):
    first_unique_char("swiss")   -> 1   ('w' is the first non-repeating char)
    first_unique_char("aabb")    -> -1  (no unique character)
    first_unique_char("")        -> -1  (edge case — think about why)

Using the same EP/BVA pattern as the worked example:
  1. List this function's input partitions and boundaries as a comment.
  2. Implement the function.
  3. Write a test suite covering each partition/boundary you listed —
     one test per case, named after what it covers.

This is a different problem from binary_search (frequency counting
over a string instead of searching a sorted list), so think through
first_unique_char()'s own partitions before writing tests.
"""


def first_unique_char(s: str) -> int:
    # TODO: implement
    pass


# TODO: partitions/boundaries as a comment here

# TODO: test_first_unique_char_...
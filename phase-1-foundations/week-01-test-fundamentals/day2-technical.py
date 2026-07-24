"""
Phase 1, Week 1 — Day 2 (Technical)
Theme: Test fundamentals (debugging via test-first thinking)
Time budget: ~10 min

=====================================================================
1) CONCEPT + PATTERN
=====================================================================
"Test-first debugging" means: when you're handed a broken function, don't
stare at the code trying to spot the bug by reading it. Instead, write a
test suite from the *spec* (as if the function didn't exist yet) using
EP/BVA. Run it against the broken implementation. The failing tests tell
you exactly which partition/boundary is wrong — turning "where's the bug"
into "which assertion failed."

The pattern:
  1. Read the spec. Ignore the existing implementation for now.
  2. List partitions and boundaries (same EP/BVA process as Day 1).
  3. Write tests for each, predicting the expected output from the spec.
  4. Run the tests against the given implementation.
  5. Whichever test fails first tells you where to look in the code —
     fix only that, then rerun everything to confirm no regressions.

=====================================================================
2) WORKED EXAMPLE
=====================================================================
Spec: find_max(nums: list[int]) -> int
Returns the largest value in a non-empty list of integers.

Given (broken) implementation:
"""


def find_max(nums):
    max_val = 0  # bug: assumes 0 is always a safe starting point
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val


# Partitions/boundaries written from the spec, before worrying about the bug:
#   - all positive numbers       -> should return the largest positive
#   - all negative numbers       -> should return the largest (least negative)
#   - mix of positive/negative   -> should return the largest overall
#   - single-element list        -> should return that element
#   - list containing zero       -> should return correctly even if max is 0

def test_find_max_all_positive():
    assert find_max([3, 7, 2]) == 7


def test_find_max_all_negative():
    # this is the one that exposes the bug: max_val starts at 0, which is
    # greater than every element, so the function wrongly returns 0.
    assert find_max([-5, -1, -9]) == -1


def test_find_max_single_element():
    assert find_max([4]) == 4


# Running these shows test_find_max_all_negative fails — that pinpoints the
# bug to the `max_val = 0` initialization, not something deeper in the loop.
# Fix: initialize max_val = nums[0] instead of 0.


"""
=====================================================================
3) YOUR EXERCISE
=====================================================================
Spec: remove_duplicates(items: list) -> list
Returns a new list with duplicate values removed, preserving the order
of first occurrence.

Example (per spec):
    remove_duplicates([1, 2, 2, 3, 1])   -> [1, 2, 3]
    remove_duplicates([])                -> []
    remove_duplicates([5])               -> [5]

Given (broken) implementation below — do NOT read it closely yet.
  1. From the spec alone, list partitions/boundaries as a comment
     (empty list, single element, all-unique, all-duplicate, mix, etc).
  2. Write a test per partition/boundary, predicting expected output
     from the spec (not from reading the code).
  3. Run the tests (e.g. `pytest day2-technical.py`) against the given
     implementation and see which one(s) fail.
  4. Fix only what the failing test(s) point to, then rerun to confirm
     everything passes.
"""


def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            result.append(item)
        seen.add(item)
    return result


# Partitions/boundaries written from the spec, before worrying about the bug:
#   - empty list                                    -> should return empty list
#   - single element in list                        -> should return the same element in the list
#   - all different elements in list                -> should return the same elements in list in the same order
#   - all duplicate elements in list                -> should return a single of the elements in the list
#   - list contains duplicates and unique elements  -> should return a list without duplicates preserving the order

def test_remove_duplicates_empty_list():
    assert remove_duplicates([]) == []

def test_remove_duplicates_single_element():
    assert remove_duplicates([1]) == [1]

def test_remove_duplicates_all_unique():
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

def test_remove_duplicates_all_duplicate():
    assert remove_duplicates([1, 1, 1]) == [1]

def test_remove_duplicates_mixed():
    assert remove_duplicates([3, 2, 2, 5]) == [3, 2, 5]

# DSA Learning Journey - Progress Tracker

## Purpose

This document is the complete context for my ongoing DSA learning
journey. If a previous conversation is lost, treat this document as the
source of truth and continue coaching from where it left off.

## Background

### Previous Attempts

-   Problems became too difficult too quickly.
-   Missing a few days often caused the plan to be abandoned.
-   Traditional topic order repeatedly stalled around Linked Lists.

## Goals

1.  Improve logical thinking.
2.  Improve problem-solving ability.
3.  Build long-term intuition for recognizing DSA patterns.
4.  Build a strong DSA foundation (interviews are secondary).

## Constraints

-   Study time: **15--30 minutes**
-   Weekly success: **3 sessions**
-   Consistency over intensity.
-   Missing days does **not** reset progress.

## Preferred Languages

-   Primary: Python
-   Secondary: Java

## Learning Philosophy

Use a **spiral curriculum**: 1. Arrays 2. Strings 3. Hash Maps / Sets 4.
Stacks 5. Queues 6. Linked Lists 7. Trees 8. Graphs 9. Heaps 10.
Recursion 11. Searching & Sorting

## Session Structure

1.  Learn (5 min)
2.  Solve (10--20 min)
3.  Reflect (2--5 min)

## Coaching Style

-   Act as a mentor.
-   Review correctness, complexity, readability, and maintainability.
-   Prefer clear production-quality code over clever tricks.
-   Increase difficulty gradually.

## Additional Rule

### The 80% Rule

End every session feeling: \> "I could probably do one more."

## Coding Philosophy

My code is frequently reused by teammates.

Prioritize: - Readability - Maintainability - Explicit logic - Low
cognitive load

Only introduce Pythonic shortcuts when they genuinely improve
readability.

------------------------------------------------------------------------

# Progress

## Current Stage

Pass 1 --- Arrays

### Session 1

**Concept:** Single-pass scan maintaining the current maximum.

**Problem:** Find the largest element without using `max()`.

**Result** - Correct O(n) / O(1) solution. - Suggested improvements: -
Initialize from the first element instead of `-sys.maxsize`. - Avoid
naming variables `list`.

### Session 2

**Concept:** Counting while scanning.

**Problem:** Count even numbers in one traversal.

**Result** - Correct O(n) / O(1) solution. - Suggested improvements: -
Use `count += 1`. - No explicit empty-list check needed. - Avoid naming
variables `list`.

## Key Learning So Far

Many beginner array problems share the same pattern:

``` text
Initialize state
↓
Scan once
↓
Update state
↓
Return state
```

The maintained state changes: - Maximum - Minimum - Count - Sum -
Average - Running total

The goal is to recognize the pattern rather than memorize problems.

## Next Session

Continue Arrays.

Topic: **Single-pass scan with accumulated state**

Examples: - Sum of elements - Sum of positive numbers - Average -
Running total

Hash Maps will be introduced after these scanning patterns become
intuitive.

## Notes for Future Coach

The learner is also an interviewer.

Optimize for: - Clear explanations - Pattern recognition -
Production-quality code - Readability before cleverness

Long-term objective: Recognize patterns such as: - Single-pass scan -
Hash Map - Sliding Window - BFS vs DFS - Graph problems

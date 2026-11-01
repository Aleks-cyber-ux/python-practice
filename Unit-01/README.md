# Unit 1 Overview

Output and input, arithmetic formulas, and working with strings (indexing, slicing, character codes).

Each row links to the problem statement. IDs follow `Unit-Chapter-Question`.

## Chapter 1 - Printing: `sep` and `end`

| Problem                            | Title            | Concept      | Skills practised                                   |
| ---------------------------------- | ---------------- | ------------ | -------------------------------------------------- |
| [01-01-01](Chapter-01/01-01-01.md) | *Print with sep* | print(): sep | One print() with several arguments; sep= parameter |
| [01-01-02](Chapter-01/01-01-02.md) | *Print with end* | print(): end | Several print() calls; end= parameter              |

## Chapter 2 - Input and f-strings

| Problem                            | Title                     | Concept                   | Skills practised                                                  |
| ---------------------------------- | ------------------------- | ------------------------- | ----------------------------------------------------------------- |
| [01-02-01](Chapter-02/01-02-01.md) | Good Evening!             | input() + f-string output | input(); string concatenation or f-string                         |
| [01-02-02](Chapter-02/01-02-02.md) | The Mysterious Invitation | input() + f-string output | Three input() calls; building one sentence from several variables |

## Chapter 3 - Project: Madlibs

| Problem                      | Title   | Concept                   | Skills practised                                                                                |
| ---------------------------- | ------- | ------------------------- | ----------------------------------------------------------------------------------------------- |
| [01-03](Chapter-03/01-03.md) | Madlibs | input() + f-string output | 10 input() prompts; descriptive variable names; f-strings; escape characters; reusing variables |

## Chapter 4 - Arithmetic formulas

| Problem                            | Title               | Concept                           | Skills practised                                                       |
| ---------------------------------- | ------------------- | --------------------------------- | ---------------------------------------------------------------------- |
| [01-04-01](Chapter-04/01-04-01.md) | The Mysterious Tile | Arithmetic formulas (single step) | int(input()); multiplication; integer output                           |
| [01-04-02](Chapter-04/01-04-02.md) | The Hidden Door     | Arithmetic formulas (single step) | float(input()); two inputs; float output                               |
| [01-04-03](Chapter-04/01-04-03.md) | The Inscription     | Arithmetic formulas (single step) | float(input()); division by 2; float output                            |
| [01-04-04](Chapter-04/01-04-04.md) | The Mystic Cube     | Arithmetic formulas (single step) | Exponent operator (\*\*3); float output                                |
| [01-04-05](Chapter-04/01-04-05.md) | The Ancient Vault   | Arithmetic formulas (single step) | Three float inputs; multiplying three values                           |
| [01-04-06](Chapter-04/01-04-06.md) | The Enchanted Seal  | Arithmetic formulas (single step) | Using a given constant (pi = 3.14159); exponent; float output          |
| [01-04-07](Chapter-04/01-04-07.md) | The Orb of Power    | Arithmetic formulas (multi-step)  | Radius from diameter; 4/3 as a fraction; exponent; order of operations |
| [01-04-08](Chapter-04/01-04-08.md) | The Twin Pillars    | Arithmetic formulas (multi-step)  | Two-term formula; reusing pi, R and H; parentheses                     |
| [01-04-09](Chapter-04/01-04-09.md) | The Fractured Cone  | Arithmetic formulas (multi-step)  | Longer formula; parentheses and precedence; three inputs               |
| [01-04-10](Chapter-04/01-04-10.md) | The End             | None (story page)                 |                                                                        |

## Chapter 5 - String indexing and slicing

| Problem                            | Title                         | Concept         | Skills practised                                       |
| ---------------------------------- | ----------------------------- | --------------- | ------------------------------------------------------ |
| [01-05-01](Chapter-05/01-05-01.md) | *Third character*             | String indexing | s[2]; zero-based indexing                              |
| [01-05-02](Chapter-05/01-05-02.md) | *Character at an index*       | String indexing | Index held in a variable; int(input())                 |
| [01-05-03](Chapter-05/01-05-03.md) | *First three characters*      | String slicing  | s[:3]                                                  |
| [01-05-04](Chapter-05/01-05-04.md) | *Second-last character*       | String indexing | Negative index s[-2]                                   |
| [01-05-05](Chapter-05/01-05-05.md) | *Last two characters*         | String slicing  | Negative slice s[-2:]                                  |
| [01-05-06](Chapter-05/01-05-06.md) | *First and last N characters* | String slicing  | Two slices joined with +; slice bounds from a variable |
| [01-05-07](Chapter-05/01-05-07.md) | *Odd-index characters*        | String slicing  | Slice with a step, s[1::2]                             |
| [01-05-08](Chapter-05/01-05-08.md) | *Reverse with a step*         | String slicing  | Negative step, s[::-n]                                 |

## Chapter 6 - Mixed: character codes, built-in functions, inserting into a string

| Problem                            | Title                                  | Concept                   | Skills practised                                                             |
| ---------------------------------- | -------------------------------------- | ------------------------- | ---------------------------------------------------------------------------- |
| [01-06-01](Chapter-06/01-06-01.md) | *Code points of neighbouring letters*  | Character codes (ord/chr) | ord(); chr(); arithmetic on code points; f-string with several values        |
| [01-06-02](Chapter-06/01-06-02.md) | *Min, max, average, cube, square root* | Built-in & math functions | min(); max(); abs(); \*\*; math.sqrt() with import math; average of 5 inputs |
| [01-06-03](Chapter-06/01-06-03.md) | *Add-word (insert into sentence)*      | String slicing            | Slice at an index and rebuild with +; three inputs                           |

## Notes

- Titles in italics are short descriptive labels added for this overview; the problem statement itself has no title (01-01-01, 01-01-02, 01-05-01, 01-05-02, 01-05-03, 01-05-04, 01-05-05, 01-05-06, 01-05-07, 01-05-08, 01-06-01, 01-06-02, 01-06-03).
- 01-04-10 is a story page with no programming task.
- 01-03 is an open-ended project with no automated tests.

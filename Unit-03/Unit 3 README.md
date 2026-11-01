# Unit 3 overview

Loops: `while`, `for`, nested loops, loop control, and loops over strings. Includes one file-writing project.

Each row links to the problem statement. IDs follow `Unit-Chapter-Question`.

## Chapter 1 - `while` loops and accumulators

| Problem                            | Title              | Concept                                       | Skills practised                                                                              |
| ---------------------------------- | ------------------ | --------------------------------------------- | --------------------------------------------------------------------------------------------- |
| [03-01-01](Chapter-01/03-01-01.md) | Rocket Launch      | while loop (counter)                          | Counter variable; decrementing; loop condition; special message instead of 0                  |
| [03-01-02](Chapter-01/03-01-02.md) | Faceless Men       | while loop (sentinel / exit condition)        | Input inside a loop; string comparison; break or loop condition; two lines of output per pass |
| [03-01-03](Chapter-01/03-01-03.md) | Infinite Questions | while loop (sentinel / exit condition)        | while True; input() inside a loop                                                             |
| [03-01-04](Chapter-01/03-01-04.md) | Kill Switch        | while loop (sentinel / exit condition)        | break; secret exit input; telling the user how to exit                                        |
| [03-01-05](Chapter-01/03-01-05.md) | Average of the 10  | Accumulator pattern (sum / product / average) | Counted loop (10 passes); running total; float input; average after the loop                  |
| [03-01-06](Chapter-01/03-01-06.md) | Sum of 1 to X      | Accumulator pattern (sum / product / average) | range(1, N+1) or while; running total; inclusive end                                          |
| [03-01-07](Chapter-01/03-01-07.md) | Prime Checker      | Prime / divisibility algorithms               | Loop with %; flag variable or break; N up to 999,999                                          |

## Chapter 2 - Project: writing a receipt file

| Problem                            | Title   | Concept            | Skills practised                                                                                                                                               |
| ---------------------------------- | ------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [03-02-01](Chapter-02/03-02-01.md) | Receipt | Writing text files | Sentinel loop (blank to finish); storing items and prices; string alignment (ljust / rjust / f-string widths); tax calculation; with open(..., 'w'); f.write() |

## Chapter 3 - `for` loops and pattern printing

| Problem                            | Title              | Concept                                       | Skills practised                                                        |
| ---------------------------------- | ------------------ | --------------------------------------------- | ----------------------------------------------------------------------- |
| [03-03-01](Chapter-03/03-03-01.md) | Happy Holidays     | for loop with range()                         | range() counting down (negative step); f-string; message after the loop |
| [03-03-02](Chapter-03/03-03-02.md) | Factorials         | Accumulator pattern (sum / product / average) | for + range; running product starting at 1                              |
| [03-03-03](Chapter-03/03-03-03.md) | Asterisk Pyramid   | Pattern printing (for loop)                   | Loop with a shrinking count; string repetition ('\*' \* n)              |
| [03-03-04](Chapter-03/03-03-04.md) | 101 Pyramid (easy) | Pattern printing (for loop)                   | String repetition of '10'; row length 2n-1; descending rows             |
| [03-03-05](Chapter-03/03-03-05.md) | 101 Pyramid (hard) | Pattern printing (for loop)                   | Same pattern plus growing left padding (' ' \* i); no trailing spaces   |

## Chapter 4 - Loop control: repeat prompts, `break`, `continue`, `random`

| Problem                            | Title                          | Concept                                | Skills practised                                                                    |
| ---------------------------------- | ------------------------------ | -------------------------------------- | ----------------------------------------------------------------------------------- |
| [03-04-01](Chapter-04/03-04-01.md) | Adding Numbers Looped (easy)   | while loop (sentinel / exit condition) | Run-again prompt; two int inputs; loop controlled by the user's answer              |
| [03-04-02](Chapter-04/03-04-02.md) | Adding Numbers Looped (medium) | Loop flow control (break / continue)   | Iteration counter; break; two exit conditions combined                              |
| [03-04-03](Chapter-04/03-04-03.md) | Adding Numbers Looped (hard)   | Loop flow control (break / continue)   | import random; random decision each pass; continue while the counter still advances |

## Chapter 5 - Nested loops

| Problem                            | Title                     | Concept                          | Skills practised                                                                  |
| ---------------------------------- | ------------------------- | -------------------------------- | --------------------------------------------------------------------------------- |
| [03-05-01](Chapter-05/03-05-01.md) | Asterisk Rectangle (easy) | Nested loops (patterns / tables) | Rows x columns; print(end=''); or string repetition                               |
| [03-05-02](Chapter-05/03-05-02.md) | Multiplication Table      | Nested loops (patterns / tables) | Row-by-column products; single spaces between values and no trailing space        |
| [03-05-03](Chapter-05/03-05-03.md) | Number Triangle (easy)    | Nested loops (patterns / tables) | Inner range that shrinks every row; countdown numbers; space-separated output     |
| [03-05-04](Chapter-05/03-05-04.md) | Prime Numbers Looped      | Prime / divisibility algorithms  | Loop inside a loop; reusing the prime test; one prime per line                    |
| [03-05-05](Chapter-05/03-05-05.md) | Number Triangle (hard)    | Nested loops (patterns / tables) | Count up then back down on one row; leading-space indentation; no trailing spaces |
| [03-05-06](Chapter-05/03-05-06.md) | Asterisk Rectangle (hard) | Nested loops (patterns / tables) | Border-versus-interior logic with conditionals; edge case when height is 2        |

## Chapter 6 - Looping over strings: ciphers

| Problem                            | Title                 | Concept                          | Skills practised                                                                                                        |
| ---------------------------------- | --------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [03-06-01](Chapter-06/03-06-01.md) | Secret Agent Messages | Looping over strings (ord / chr) | for char in string; ord/chr; modulo wrap-around; negative keys; spaces left unchanged                                   |
| [03-06-02](Chapter-06/03-06-02.md) | Enhanced Agent Cipher | Looping over strings (ord / chr) | Key that rotates among three values and only advances on letters; separate upper/lower ranges; non-letters pass through |

## Chapter 7 - Mixed loop problems

| Problem                            | Title              | Concept                          | Skills practised                                                                                                  |
| ---------------------------------- | ------------------ | -------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| [03-07-01](Chapter-07/03-07-01.md) | Fibonacci Sequence | Sequence generation (Fibonacci)  | Two-variable update or a list inside a loop; 25 terms; computing a ratio instead of hard-coding it; documentation |
| [03-07-02](Chapter-07/03-07-02.md) | Street Fighter     | Simulation with random           | while loop until a condition is met; random.randint; random turn order; hit-point tracking; per-round output      |
| [03-07-03](Chapter-07/03-07-03.md) | Times Table        | Nested loops (patterns / tables) | Header row and column; string formatting; k up to 10                                                              |
| [03-07-04](Chapter-07/03-07-04.md) | Scaled Up Icons    | Nested loops (patterns / tables) | Scale each character k times across and each line k times down; spaces matter; string repetition                  |

## Notes

- No automated tests (interactive, random or open-ended): 03-01-03, 03-01-04, 03-02-01, 03-04-01, 03-04-02, 03-04-03, 03-06-02, 03-07-01, 03-07-02.

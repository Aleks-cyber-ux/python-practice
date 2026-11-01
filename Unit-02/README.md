# Unit 2 Overview

Boolean expressions and conditionals: comparison operators, logical operators, `if`/`else`, `if`/`elif`/`else`.

Each row links to the problem statement. IDs follow `Unit-Chapter-Question`.

## Chapter 1 - Comparison operators (no `if` allowed)

| Problem                            | Title                     | Concept                               | Skills practised                                           |
| ---------------------------------- | ------------------------- | ------------------------------------- | ---------------------------------------------------------- |
| [02-01-01](Chapter-01/02-01-01.md) | More than 100             | Comparison operators (Boolean result) | > operator; printing a bool; converting input to a number  |
| [02-01-02](Chapter-01/02-01-02.md) | Check for 21              | Comparison operators (Boolean result) | Equality operator (==); int input                          |
| [02-01-03](Chapter-01/02-01-03.md) | Absolute Value Check      | Comparison operators (Boolean result) | abs(); <= operator; float input                            |
| [02-01-04](Chapter-01/02-01-04.md) | Transformation Comparison | Comparison operators (Boolean result) | Several arithmetic steps then compare; order of operations |
| [02-01-05](Chapter-01/02-01-05.md) | Grade Average Check       | Comparison operators (Boolean result) | Three inputs; average; >= operator; parentheses            |

## Chapter 2 - Logical operators: `and`, `or`, `not`

| Problem                            | Title                 | Concept                        | Skills practised                                                      |
| ---------------------------------- | --------------------- | ------------------------------ | --------------------------------------------------------------------- |
| [02-02-01](Chapter-02/02-02-01.md) | Check for 8 or 10     | Logical operators (and/or/not) | or; two equality checks; float or int input                           |
| [02-02-02](Chapter-02/02-02-02.md) | Not Equal to 8 or 10  | Logical operators (and/or/not) | or with !=; De Morgan's laws                                          |
| [02-02-03](Chapter-02/02-02-03.md) | Range Check (1 to 10) | Logical operators (and/or/not) | and; inclusive range; chained comparison 1 <= N <= 10                 |
| [02-02-04](Chapter-02/02-02-04.md) | Complex Range Check   | Logical operators (and/or/not) | and + or combined; mixing exclusive and inclusive bounds; parentheses |
| [02-02-05](Chapter-02/02-02-05.md) | Divisibility Check    | Logical operators (and/or/not) | % (modulo); and; != / not                                             |
| [02-02-06](Chapter-02/02-02-06.md) | Browser Check         | Logical operators (and/or/not) | String equality; or; case-sensitive text                              |

## Chapter 3 - `if` / `else`

| Problem                            | Title                         | Concept   | Skills practised                                                                     |
| ---------------------------------- | ----------------------------- | --------- | ------------------------------------------------------------------------------------ |
| [02-03-01](Chapter-03/02-03-01.md) | Equality Check                | if / else | Equality operator (==); two-way branch; printing one of two strings                  |
| [02-03-02](Chapter-03/02-03-02.md) | Odd or Even                   | if / else | % 2; two-way branch                                                                  |
| [02-03-03](Chapter-03/02-03-03.md) | Sentence Length Check         | if / else | len(); > ; string input                                                              |
| [02-03-04](Chapter-03/02-03-04.md) | Number Comparison             | if / else | Two float inputs; > ; two-way branch                                                 |
| [02-03-05](Chapter-03/02-03-05.md) | Profit Calculation            | if / else | Compute a value, then branch; output is a number in one branch and text in the other |
| [02-03-06](Chapter-03/02-03-06.md) | Range Inclusion Check         | if / else | and; inclusive range; three inputs; negatives and floats                             |
| [02-03-07](Chapter-03/02-03-07.md) | Triangle Angle Validity Check | if / else | Sum of three inputs; == 180                                                          |
| [02-03-08](Chapter-03/02-03-08.md) | Triangle Side Validity Check  | if / else | Three conditions joined with and (triangle inequality)                               |

## Chapter 4 - `if` / `elif` / `else`

| Problem                            | Title                      | Concept          |                                                    
| ---------------------------------- | -------------------------- | ---------------- | 
| [02-04-01](Chapter-04/02-04-01.md) | Day of the Week            | if / elif / else |
| [02-04-02](Chapter-04/02-04-02.md) | Number Sign Check          | if / elif / else | 
| [02-04-03](Chapter-04/02-04-03.md) | The Tallest Sibling        | if / elif / else | 
| [02-04-04](Chapter-04/02-04-04.md) | Fizz Buzz Single Number    | if / elif / else |
| [02-04-05](Chapter-04/02-04-05.md) | Federal Tax Bracket Finder | if / elif / else | 

## Notes

- 02-01-01 to 02-01-05 are checked automatically for the letters `if`; a solution containing them anywhere in the code fails. The point is to practise Boolean expressions before learning `if`.

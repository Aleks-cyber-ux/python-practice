# Unit 5 Overview

Functions: parameters and return values, and a menu-driven program built from functions.

Each row links to the problem statement. IDs follow `Unit-Chapter-Question`.

## Chapter 1 - Functions with parameters and return values

| Problem                            | Title                   | Concept                               | Skills practised                                                                                 |
| ---------------------------------- | ----------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------ |
| [05-01-01](Chapter-01/05-01-01.md) | Temperature Conversion  | Functions: parameters & return values | def with one parameter; return; two inverse functions (convertToCelsius, convertToFahrenheit)    |
| [05-01-02](Chapter-01/05-01-02.md) | Odd & Even              | Functions: parameters & return values | Boolean-returning functions isOdd / isEven; % ; both must return False for non-integers          |
| [05-01-03](Chapter-01/05-01-03.md) | Area & Volume           | Functions: parameters & return values | Four functions with 2-3 parameters each (area, perimeter, volume, surfaceArea)                   |
| [05-01-04](Chapter-01/05-01-04.md) | Fizz Buzz               | Functions: parameters & return values | Probably a loop plus modulo and conditionals inside a function (inferred from the title)         |
| [05-01-05](Chapter-01/05-01-05.md) | Ordinal Suffix          | Functions: parameters & return values | Returns text like '1st', '22nd', '11th'; special cases for 11-13; % 10 and % 100                 |
| [05-01-06](Chapter-01/05-01-06.md) | ASCII Table             | Functions: parameters & return values | Probably a loop with chr() printing an ASCII table (inferred from the title)                     |
| [05-01-07](Chapter-01/05-01-07.md) | Read Write File         | File read / write / append functions  | writeToFile, appendToFile, readFromFile; open modes 'w', 'a', 'r'; with; returning file contents |
| [05-01-08](Chapter-01/05-01-08.md) | Chess Square Colour     | Functions: parameters & return values | Two parameters; parity of row + column; return '' for squares off the board                      |
| [05-01-09](Chapter-01/05-01-09.md) | Find and Replace        | Functions: parameters & return values | String parameters; replacing every occurrence; case-sensitive; return the new string             |
| [05-01-10](Chapter-01/05-01-10.md) | Hours, Minutes, Seconds | Functions: parameters & return values | // and % (or divmod); building text from non-zero parts only ('1h 1m 1s'); '0s' for zero         |

## Chapter 2 - Functions without parameters: a menu program

| Problem                            | Title   | Concept                                 | Skills practised                                                                                                                                     |
| ---------------------------------- | ------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [05-02-01](Chapter-02/05-02-01.md) | Menu UI | Functions: no parameters (menu program) | Several functions that do their own input and print; menu() loop with an exit option; main(); if \_\_name\_\_ == '\_\_main\_\_'; optional docstrings |

## Notes

- 05-01-01 to 05-01-10 only link to the full problem text in an external PDF (inventwithpython.com). Most are checked by importing the student's functions.
- No automated tests (interactive, random or open-ended): 05-01-04, 05-01-06, 05-02-01.

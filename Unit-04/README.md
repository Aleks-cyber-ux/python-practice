# Unit 4 Overview

Lists, reading files into lists, list comprehension, and string methods.

Each row links to the problem statement. IDs follow `Unit-Chapter-Question`.

## Chapter 1 - Building and modifying lists in loops

| Problem                            | Title              | Concept                           | What you write                                                                 | Skills practised                                                                                                |
| ---------------------------------- | ------------------ | --------------------------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| [04-01-01](Chapter-01/04-01-01.md) | Inventory Tracker  | List membership (in)              | Build a list of apple types, then let a customer check whether one is in stock | Sentinel input loop; append(); the 'in' operator; two-phase program (manager, then customer)                    |
| [04-01-02](Chapter-01/04-01-02.md) | Name Tracker       | Building lists in loops (append)  | Collect names and genders, then print males, females, then others              | Sentinel loop; two inputs per pass; sorting entries into three lists by category; printing lists in a set order |
| [04-01-03](Chapter-01/04-01-03.md) | Dealership Tracker | Modifying lists (append / remove) | Used-car inventory manager with add, remove and print                          | Starting list; menu loop; append(); remove(); printing a list; exit option                                      |
| [04-01-04](Chapter-01/04-01-04.md) | Grant Tracker      | Building lists in loops (append)  | Sort students into 'Tuition Grant' or 'Full Tuition' lists by parents' income  | Sentinel loop; average of two incomes; if/else chooses which list; print both lists                             |
| [04-01-05](Chapter-01/04-01-05.md) | Prime Finder       | Building lists in loops (append)  | Collect all primes from 2 to 1000 into a list and print it neatly              | Prime test inside a loop; append to a list; formatted printing                                                  |
| [04-01-06](Chapter-01/04-01-06.md) | Prime Finder +     | Building lists in loops (append)  | Store the prime factorisation of every number from 2 to 1000 in a list         | Nested loops; repeated division; list of lists (factors per number)                                             |

## Chapter 2 - Reading text files into lists

| Problem | Title | Concept | What you write | Skills practised |
| --- | --- | --- | --- | --- |
| [04-02-01](Chapter-02/04-02-01.md) | Pizza Toppings | Reading text files | Read toppings from a file, sort them, print them | open() / with; reading lines; strip(); append to a list; sort(); print |
| [04-02-02](Chapter-02/04-02-02.md) | Memestocks | Reading text files | Total the numbers in gme-buy.txt | Reading lines; int(); running total |
| [04-02-03](Chapter-02/04-02-03.md) | Bird Tally | Reading text files | Count birds per species in bird-store.txt | Counting occurrences per category; fixed output order; ', '-joined output |

## Chapter 3 - List comprehension

| Problem | Title | Concept | What you write | Skills practised |
| --- | --- | --- | --- | --- |
| [04-03-01](Chapter-03/04-03-01.md) | Even Indexer | List comprehension | Print the even-index items of a given list | Comprehension that filters by index (range step or enumerate); one item per line |
| [04-03-02](Chapter-03/04-03-02.md) | Peculiar Numbers | List comprehension | Build a list of the odd numbers from a given list | Comprehension with an if filter (% 2) |
| [04-03-03](Chapter-03/04-03-03.md) | Divisibility List | List comprehension | Multiples of 5 that are not multiples of 7 among 1-250 | range(); compound filter (% 5 == 0 and % 7 != 0) |
| [04-03-04](Chapter-03/04-03-04.md) | Car Manufacturers | List comprehension | Keep the car makes that contain an 'a' | Filtering strings with 'in'; case-sensitive match |
| [04-03-05](Chapter-03/04-03-05.md) | Censor | List comprehension | Replace each vowel (including y) in a string with a random symbol | Conditional expression inside a comprehension (x if ... else y); random symbol; ' '.join() |
| [04-03-06](Chapter-03/04-03-06.md) | The One That He Removed | List comprehension | Pull the capitalised words out of a sentence | str.split(); build a list with a plain loop first, then a comprehension; capital-letter test; printing a list as a Python list |

## Chapter 4 - String Methods

| Problem                            | Title               | Concept                    | Skills practised                                             |
| ---------------------------------- | ------------------- | -------------------------- | ------------------------------------------------------------ |
| [04-04-01](Chapter-04/04-04-01.md) | Greeter             | String methods & operators | Capitalising only the first letter (.capitalize()); f-string |
| [04-04-02](Chapter-04/04-04-02.md) | Dash40              | String methods & operators | str.center(40, '-')                                          |
| 04-04-03                           | *Repeat five times* | String methods & operators | String repetition with \*                                    |
| [04-04-04](Chapter-04/04-04-04.md) | Uppercase Question  | String methods & operators | .upper(); concatenation                                      |
| [04-04-05](Chapter-04/04-04-05.md) | Word Breaker        | String methods & operators | '-'.join(word)                                               |
| [04-04-06](Chapter-04/04-04-06.md) | Location Finder     | String methods & operators | .lower(); .find(); .rfind()                                  |

## Notes

- Titles in italics are short descriptive labels added for this overview; the problem statement itself has no title (04-04-03).
- 04-02-01 to 04-02-03 read the `.txt` files in `Chapter-02/problem txt files/`.
- 04-04-03 has tests in `tests/04-04-03/` but no problem statement `.md` file.
- No automated tests (interactive, random or open-ended): 04-01-01, 04-01-02, 04-01-03, 04-01-04, 04-01-05, 04-01-06, 04-03-05.

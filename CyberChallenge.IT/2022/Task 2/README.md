## CyberChallenge.IT 2022 - Programming test

Date: 11/02/2024

Difficulty: Medium

Status: Pending

# Range Cover (cover)

In this task you are given in input _N_ different ranges and a number _K_. Each range is defined as a pair
of integers [start, end], where both start and end are included in the range. You goal is to count how
many integers are contained in exactly _K_ of these ranges.
For example, given _K_ = 3and _N_ = 6ranges: [3, 10], [0, 5], [6, 13], [1, 15], [13, 19] and [15, 18], only 10
integers are covered exactly by _K_ = 3ranges, in particular:

- 3 is covered by the ranges: [3, 10], [0, 5] and [1, 15]
- 4 is covered by the ranges: [3, 10], [0, 5] and [1, 15]
- 5 is covered by the ranges: [3, 10], [0, 5] and [1, 15]
- 6 is covered by the ranges: [3, 10], [6, 13] and [1, 15]
- 7 is covered by the ranges: [3, 10], [6, 13] and [1, 15]
- 8 is covered by the ranges: [3, 10], [6, 13] and [1, 15]
- 9 is covered by the ranges: [3, 10], [6, 13] and [1, 15]
- 10 is covered by the ranges: [3, 10], [6, 13] and [1, 15]
- 13 is covered by the ranges: [6, 13], [1, 15] and [13, 19]
- 15 is covered by the ranges: [1, 15], [13, 19] and [15, 18]
All the over indexes are covered by less then _K_ = 3ranges.

## Input data

The first line of the input contains two space-separated integers **N** and **K** representing the number of
ranges available and the number of index of overlapping ranges to found.
The next **N** lines contains two space-separated integers each, representing the starting and the ending
point of the coordinates (included).

## Output data

The output must contains only one integer, representing how many index are covered by exactly **K**
ranges.

## Scoring

For each of the test cases the program will be tested, the following constraints are met:

- Subtask 1 (40 points): _N_ = 10and ranges are between 0 and 10.
- Subtask 2 (40 points): _N_ = 100and ranges are between 0 and10 000.
- Subtask 3 (20 points): _N_ = 10 000and ranges are between 0 and 1015.


## Examples

```
input output
6 3
3 10
0 5
6 13
1 15
13 19
15 18
```
### 10

## Explanation

The numbers covered with 3 different ranges are: 3, 4, 5, 6, 7, 8, 9, 10, 13 and 15.



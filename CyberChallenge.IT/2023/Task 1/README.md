# CyberChallenge.IT 2023 - Programming Test

Date: 31/01/2024

Difficulty: Easy

Status: Solved

## Problem 1 - “Pretest” [40 points]

It’s pretest time for the CyberChallenge.IT 2023 edition!

As every year, the pretest is a multiple choice test, withQquestions with 4 possible answers (A, B, C, D) each,
of which one and only one is correct.

The organizers want to write a software to automatically grade the tests of theNparticipating candidates,
giving them 1 point for each correct answer and 0 points for each wrong or missing one.

Given the number of questionsQand candidatesN, the list of correct answers (in the form of a string with
lengthQ), andNstrings representing the answers given by each candidate, compute the number of points
scored for each of them.

## Problem Details

Input

The input consists ofN+ 2 lines:

- Line 1: The numbersQandN, separated by a space.
- Line 2: The list of correct answers, as a string ofQuppercase letters in the set{A, B, C, D}.
- Lines 3,... , N+ 2: a string ofQcharacters in the set{A, B, C, D, ?}, where? denotes a missing answer.

Output

The output must containNlines. In linei, you should output a single integer with the number of points scored
by thei-th candidate, in the same order as in the input.

Scoring

Your program will be tested on a number of testcases grouped in subtasks. In order to obtain the score associated
to a subtask, you need to correctly solve all its testcases.

- Subtask 1 [20 points]:N= 1, 1≤Q≤1000.
- Subtask 2 [20 points]: 1≤N≤1000, 1≤Q≤1000.

Examples

```
INPUT OUTPUT
```
```
10 3
CBBDACCCBC
D?ABCD?DDB
AB?ACCBAAA
B?CCBA?C?D
```
```
0
2
1
```


CyberChallenge.IT 2023 - Programming Test

Explanation

From the first line, we know that there are 10 questions and 3 participants. The answers of the first participant
are all different from the correct ones or missing, so their score is 0. The second one only matches on the second
and sixth question, so their score is 2. The same goes for the third one, who gave the right answer only for
question 8, therefore their score is 1.




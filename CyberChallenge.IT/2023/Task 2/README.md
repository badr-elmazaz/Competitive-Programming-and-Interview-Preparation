# CyberChallenge.IT 2023 - Programming Test

Date: 31/01/2024

Difficulty: Medium

Status: Solved

## Problem 2 - “Who’s the winner?” [60 points]

The local selection of the CyberChallenge.IT program is an individual CTF competition in jeopardy-style.

Each of theMplayers is faced withNtasks, each of them worth a fixed amount of pointsP 1 , ..., PN. Each
task has a correct answer, called theflag, that must be submitted by players in order to get the task’s points.
There are no penalties for wrong submissions and, obviously, a player can solve a task only once (which means
that resubmissions of the same flag will not modify the player’s score).

At the end of the competition, the player who scored the most points is the winner. In case of a draw, the
“submission time” of a player is taken into account, that is, the timestamp of the last submission that modified
the player’s score. In this case, the player with lower submission time is considered the winner. So, the final
scoreboard is computed by number of points in descending order, then submission time in ascending order.
Finally, if there are still “draw” situations, the players are ordered by their player id, in ascending order (in
particular, this is applied to players with score equal to 0, for which the submission time is not set).

Given the number of playersM, tasksN and total submissionsSduring the competition, the list of tasks
with their numerical id, amount of points and the correct flag, and the list of submissions with the associated
submitted flag, timestamp and player id, can you determine the final scoreboard?

Note: tasks are numbered from 1 toN, while players are numbered from 1 toMfor convenience.
Note: submissions are given in random order.

## Problem Details

Input

The input consists ofN+S+ 1 lines:

- Line 1: the numbersM,NandS, separated by a space.
- Lines 2,... , N+ 1: the description of the tasks. Each of these lines will have 3 space-separated values,
    namely the task id (a unique integer between 1 andN), the correct flag (a string consisting only in
    uppercase and lowercase letters of length 10), and the number of points associated to the task (a positive
    integer up to 1000).
- LinesN+ 2,... , N+S+ 1: the description of the submissions. Each of these lines will have 4 space-
    separated values, namely the player id, the task id for which the submission was made, the flag submitted
    (a string of length 10) and the timestamp of the submission (a positive integer up to 10^6 ).

Output

The output must containMlines, with two space-separated values each. Thei-th line must contain the player
id of the player ini-th position and the associated number of points.

Scoring

Your program will be tested on a number of testcases grouped in subtasks. In order to obtain the score associ-
ated to a subtask, you need to correctly solve all its testcases.

- Subtask 1 [30 points]: 1≤M≤10, 1≤N≤10, 1≤S≤100.
- Subtask 2 [30 points]: 1≤M≤300, 1≤N≤300, 1≤S≤50000.


Examples

```
INPUT OUTPUT
```
```
5 2 6
1 EfnccJSqUyOsYGO 50
2 XWMsVGHynvrEspF 100
2 2 XWMsVGHynvrEspF 7
2 1 EfnccJSqUyOsYGO 4
4 1 EfnccJSqUyOsYGO 10
1 1 EfnccJSqUyOsYGO 5
1 2 bWWinauoIIDfKpz 6
1 1 EfnccJSqUyOsYGO 25
```
```
2 150
1 50
4 50
3 0
5 0
```
Explanation

From the first line, the competition has 5 players, 2 tasks and 6 total submissions. Task 1 is worth 50 points
and its flag isEfnccJSqUyOsYGO, while task 2 is worth 100 points and its flag isXWMsVGHynvrEspF. Let’s go
through the submissions:

- Player 2 submitted a correct answer to task 2 at time 7. So their total number of points is now 100 and
    their submission time is 7.
- Player 2 submitted a correct answer to task 1 at time 4. So their score goes up to 150. Notice that, since
    the submission for task 1 happened before the one for task 2, the submission time is unchanged.
- Player 4 submitted a correct answer to task 1 at time 10. So their total number of points is now 50 and
    their submission time is 10.
- Player 1 submitted a correct answer to task 1 at time 5. So their total number of points is now 50 and
    their submission time is 5.
- Player 1 submitted awronganswer to task 2 at time 6. So both their score and penalty time remain
    unchanged.
- Player 1 submitted a correct answer to task 1 at time 25. However, they already solved that task before,
    so both their score and penalty time remain unchanged.

At the end, player 2 is the only one with both tasks solved, being so in first position. Players 1 and 4 both
solved only one task, so they are both at 50 points, but player 1 is in second place because of submission time
(5 for player 1 and 10 for player 4). Both players 3 and 5 did not manage to get any points, so they are ordered
by their id, with player 3 finishing in position 4 and player 5 in position 5.



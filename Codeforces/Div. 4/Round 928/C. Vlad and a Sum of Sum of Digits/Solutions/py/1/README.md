# [C. Vlad and a Sum of Sum of Digits](https://codeforces.com/contest/1926/problem/C)

Date: 20/02/2024

Status: Pending

## Description:

time limit per test

0.5 seconds

memory limit per test

256 megabytes

input

standard input

output

standard output

Please note that the time limit for this problem is only 0.5 seconds per test.

Vladislav wrote the integers from 11 to n�, inclusive, on the board. Then he replaced each integer with the sum of its digits.

What is the sum of the numbers on the board now?

For example, if n=12�=12 then initially the numbers on the board are:

1,2,3,4,5,6,7,8,9,10,11,12.1,2,3,4,5,6,7,8,9,10,11,12.

Then after the replacement, the numbers become:

1,2,3,4,5,6,7,8,9,1,2,3.1,2,3,4,5,6,7,8,9,1,2,3.

The sum of these numbers is 1+2+3+4+5+6+7+8+9+1+2+3=511+2+3+4+5+6+7+8+9+1+2+3=51. Thus, for n=12�=12 the answer is 5151.

Input

The first line contains an integer t� (1≤t≤1041≤�≤104) --- the number of test cases.

The only line of each test case contains a single integer n� (1≤n≤2⋅1051≤�≤2⋅105) --- the largest number Vladislav writes.

Output

For each test case, output a single integer --- the sum of the numbers at the end of the process.

Example

input

Copy

7

12

1

2

3

1434

2024

200000

output

Copy

51
1
3
6
18465
28170
4600002
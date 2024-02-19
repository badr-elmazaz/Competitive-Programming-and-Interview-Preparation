# [B. Vlad and Shapes](https://codeforces.com/contest/1926/problem/B)

Date: 19/02/2024

Status: Solved

## Description:

time limit per test

1 second

memory limit per test

256 megabytes

input

standard input

output

standard output

Vladislav has a binary square grid of n×n�×� cells. A triangle or a square is drawn on the grid with symbols 11. As he is too busy being cool, he asks you to tell him which shape is drawn on the grid.

-   A triangle is a shape consisting of k� (k>1�>1) consecutive rows, where the i�-th row has 2⋅i-12⋅�-1 consecutive characters 11, and the central 1s are located in one column. An upside down triangle is also considered a valid triangle (but not rotated by 90 degrees).

![](https://espresso.codeforces.com/db242fa9b991f493bbca9ab6358c4e076e7cbbf8.png)Two left pictures contain examples of triangles: k=4�=4, k=3�=3. The two right pictures don't contain triangles.

-   A square is a shape consisting of k� (k>1�>1) consecutive rows, where the i�-th row has k� consecutive characters 11, which are positioned at an equal distance from the left edge of the grid.

![](https://espresso.codeforces.com/c91a4bbd6d4165c4b64471361fe556bda28b2d94.png)Examples of two squares: k=2�=2, k=4�=4.

For the given grid, determine the type of shape that is drawn on it.

Input

The first line contains a single integer t� (1≤t≤1001≤�≤100) --- the number of test cases.

The first line of each test case contains a single integer n� (2≤n≤102≤�≤10) --- the size of the grid.

The next n� lines each contain n� characters 00 or 11.

The grid contains exactly one triangle or exactly one square that contains all the 11s in the grid. It is guaranteed that the size of the triangle or square is greater than 11 (i.e., the shape cannot consist of exactly one 1).

Output

For each test case, output "SQUARE" if all the 11s in the grid form a square, and "TRIANGLE" otherwise (without quotes).

Example

input



6

3

000

011

011

4

0000

0000

0100

1110

2

11

11

5

00111

00010

00000

00000

00000

10

0000000000

0000000000

0000000000

0000000000

0000000000

1111111110

0111111100

0011111000

0001110000

0000100000

3

111

111

111

output



SQUARE
TRIANGLE
SQUARE
TRIANGLE
TRIANGLE
SQUARE
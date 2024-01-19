# Pairs with Specific Difference
----

Date: 18/01/2024

Difficulty: Easy

Status: Solved

## Description:

Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

**Note**: the order of the pairs in the output array should maintain the order of the y element in the original array.

```
input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]
```

```
input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []
```
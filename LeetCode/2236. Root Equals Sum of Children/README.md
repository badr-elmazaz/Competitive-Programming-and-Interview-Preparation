# [2236\. Root Equals Sum of Children](https://leetcode.com/problems/root-equals-sum-of-children/)

Date: 05/11/2022

Difficulty: Easy

Status: Solved

## Description:

You are given the `root` of a binary tree that consists of exactly `3` nodes: the root, its left child, and its right child.

Return `true` *if the value of the root is equal to the sum of the values of its two children, or *`false`* otherwise*.

Example 1:

![](https://assets.leetcode.com/uploads/2022/04/08/graph3drawio.png)

Input: root = [10,4,6]
Output: true
Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
10 is equal to 4 + 6, so we return true.

Example 2:

![](https://assets.leetcode.com/uploads/2022/04/08/graph3drawio-1.png)

Input: root = [5,3,1]
Output: false
Explanation: The values of the root, its left child, and its right child are 5, 3, and 1, respectively.
5 is not equal to 3 + 1, so we return false.

Constraints:

-   The tree consists only of the root, its left child, and its right child.
-   `-100 <= Node.val <= 100`
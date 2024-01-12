

"Status: X"

"problem url: https://www.hackerrank.com/challenges/find-strings/problem"

#imports

import math
import os
import random
import re
import sys


def union_two_lists(a: list, b: list) -> list:
    union_list = []
    for i in a:
        if i not in union_list:
            union_list.append(i)
    for j in b:
        if j not in union_list:
            union_list.append(j)
    return union_list


def create_sorted_substrings(string: str) -> list[str]:
    to_return = []
    string = ''.join(sorted(string))
    for i in range(0, len(string)):
        to_return.append(string[i])
        prev = string[i]
        for j in range(i + 1, len(string)):
            prev = prev + string[j]
            to_return.append(prev)
    return to_return

def create_sub_strings(string: str) -> list[str]:
    string_split = [s for s in string]
    string_split.sort()
    string = ""
    for s in string_split:
        string += s
    substrings = []
    support = set()
    for i in range(len(string)):
        prev = string[i]
        if prev not in support:
            # if prev not in substrings:
            substrings.append(prev)
            support.add(prev)
        for j in range(i + 1, len(string)):

            prev = prev + string[j]
            # if prev not in substrings:
            if prev not in support:
                substrings.append(prev)
                support.add(prev)

    return substrings


import heapq


def remove_duplicates_from_ordered_list(list_: list) -> list:

    return_list = [s for i, s in enumerate(list_) if i != len(list_) - 1 and s != list_[i + 1]]
    if list_[-1] != list_[-2]:
        return_list.append(list_[-1])
    return return_list

from heapq import merge
def findStrings(w: list[str], queries: list[int]):
    lists = [create_sorted_substrings(word) for word in w]
    union_list = list(merge(*lists))
    union_list=remove_duplicates_from_ordered_list(union_list)
    ans = []
    for k in queries:
        if k - 1 < len(union_list):
            ans.append(union_list[k - 1])
        else:
            ans.append("INVALID")

    return ans

# def findStrings(w: list[str], queries: list[int]):
#     subs = [create_sub_strings(string) for string in w]
#     union_list = []
#     # helping_hash_set = set()
#     # for sub in subs:
#     #     for string in sub:
#     #         # if string not in helping_hash_set:
#     #         if string not in union_list:
#     #             # helping_hash_set.add(string)
#     #             union_list.append(string)
#     union_list = list(heapq.merge(*subs))
#     union_list = remove_duplicates_from_ordered_list(union_list)
#     ans = []
#     for k in queries:
#         if k - 1 < len(union_list):
#             ans.append(union_list[k - 1])
#         else:
#             ans.append("INVALID")
#
#     return ans
# Complete the 'findStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY w
#  2. INTEGER_ARRAY queries
#



if __name__ == '__main__':
    create_sorted_substrings("abcd")
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    w_count = int(input().strip())

    w = []

    for _ in range(w_count):
        w_item = input()
        w.append(w_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = findStrings(w, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

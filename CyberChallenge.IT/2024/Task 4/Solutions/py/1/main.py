#!/bin/env python3

import sys

# Se vuoi leggere/scrivere da file decommenta qua
# fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
# fout = open("output.txt", "w")  # File di output fornito dalla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
fin = sys.stdin  # File di input fornito dalla piattaforma
fout = sys.stdout  # File di output fornito dalla piattaforma



def create_lps_array(pattern: str) -> list[int]:
    # n = len(pattern)
    # Time complexity:  O(n)
    # Space complexity: O(n)
    
    
    m = len(pattern)

    # longest proper prefix which is also suffix
    lps = [0] * m

    length, i = 0, 1

    while i < m:
        # if the current character matches the character at the length index
        if pattern[i] == pattern[length]:
            lps[i] = length + 1
            # increment both length and i
            i += 1
            length += 1

        elif length != 0:
            length = lps[length - 1]

        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(text: str, pattern: str, logs: bool = False) -> list[int]:
    # n = len(n)
    # m = len(m)
    # Time complexity:  O(n + m)
    # Space complexity: O(m)
    
    
    n, m = len(text), len(pattern)

    lps = create_lps_array(pattern)
    print("lps", lps)

    if logs:
        print(f"LPS array for pattern {pattern}: {lps}")

    match_indices = []

    i, j = 0, 0

    while i < n:
        current_text_char = text[i]
        current_pattern_char = pattern[j]
        if current_text_char == current_pattern_char:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        if j == m:
            if logs:
                print(f"Pattern found at index {i - j}")
            match_indices.append(i - j)
            j = lps[j - 1]

    return match_indices


def count_patterns(N, M, alph, s):
    kmp_search(s, s)
    return
    count = 0
    current_substr = ""
    i = 0
    while i < len(s):
        current_substr += s[i]
        print("current", current_substr)
        
        occurrences = kmp_search(s, current_substr)
        print("occurencies", occurrences)
        
        if occurrences and len(occurrences) >= len(s) / len(current_substr) and occurrences[-1] + len(current_substr) == len(s):
            # print("found", current_substr)
            count += 1
        i += 1

    return count





T = int(fin.readline().strip())
o = []
for _ in range(T):
    N, M = map(int, fin.readline().strip().split())
    alph = fin.readline().strip()
    s = fin.readline().strip()
    o.append(count_patterns(N, M, alph, s))


#print("########## OUTPUT ##########")
for num in o:
    print(num)    
    
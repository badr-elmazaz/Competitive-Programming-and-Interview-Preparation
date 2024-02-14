#!/bin/env python3

import sys

# Se vuoi leggere/scrivere da file decommenta qua
# fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
# fout = open("output.txt", "w")  # File di output fornito dalla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
fin = sys.stdin  # File di input fornito dalla piattaforma
fout = sys.stdout  # File di output fornito dalla piattaforma






def count_patterns(N, M, alph, s):
    count = 0
    current_substr = ""
    i = 0
    while i < len(s):
        current_substr += s[i]
        print("current", current_substr)
        
        occurrences = search(s, current_substr)
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
    
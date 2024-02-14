#!/bin/env python3

import sys

# Se vuoi leggere/scrivere da file decommenta qua
# fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
# fout = open("output.txt", "w")  # File di output fornito dalla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
fin = sys.stdin  # File di input fornito dalla piattaforma
fout = sys.stdout  # File di output fornito dalla piattaforma


def find_subsets(N, D, S):
    # SCRIVI QUA IL TUO CODICE
    return 0

T = int(fin.readline().strip())

for _ in range(T):
    N, D = map(int, fin.readline().strip().split())
    S = list(map(int, fin.readline().strip().split()))
    assert len(S) == N
    print(find_subsets(N, D, S))
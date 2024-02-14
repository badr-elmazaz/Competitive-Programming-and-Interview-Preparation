#!/bin/env python3

import sys

# Se vuoi leggere/scrivere da file decommenta qua
# fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
# fout = open("output.txt", "w")  # File di output fornito dalla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
fin = sys.stdin  # File di input fornito dalla piattaforma
fout = sys.stdout  # File di output fornito dalla piattaforma

def emulate(code):

    # SCRIVI QUA IL TUO CODICE
    values = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0
    }

    hashmap = {}

    i = 0
    
    while i < len(code):
        splitted_line = code[i].split()
        if "lab" in splitted_line:
            label = splitted_line[-1]
            hashmap[label] = i
        elif "jmp" in splitted_line:
            label = splitted_line[-1]
            var = splitted_line[1]
            num = int(splitted_line[2])
            if values[var] == num:
                i = hashmap[label]
        else:
            var = splitted_line[1]
            num = int(splitted_line[2])
            operation = splitted_line[0]
            if operation == "add":
                values[var] += num
            elif operation == "sub":
                values[var] -= num
            else:
                values[var] *= num
            

        
        i += 1

    total = sum(values.values())

    return total

N = int(fin.readline().strip())
code = []

for i in range(N):
    code.append(fin.readline().strip())

print(emulate(code))
from string import ascii_lowercase
from collections import defaultdict


def main():
    t = int(input())

    while t:
        alphabet = list(reversed(ascii_lowercase))

        n = int(input())

        trace = map(int, input().split())

        alphabet_table = defaultdict(int)
        new_chars_found = []

        res = []

        for num in trace:
            if num == 0:
                char = alphabet.pop()
                new_chars_found.append(char)

            else:
                idx_char = alphabet_table[num]
                alphabet_table[num] += 1
                char = new_chars_found[idx_char]

            res.append(char)

        res = "".join(res)

        print(res)

        t -= 1


if __name__ == "__main__":
    main()

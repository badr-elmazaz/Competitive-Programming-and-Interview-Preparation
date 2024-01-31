

def main():
    # q = num of questions
    # n = num of users
    # Time Complexity: O(n * q)
    # Space Complexity: O(n + q)

    q, n = map(int, input().split())

    correct = input()

    users_answers = []

    results = [0] * n

    while n:
        users_answers.append(input())
        n -= 1

    for i in range(q):
        correct_ans = correct[i]
        for j in range(len(users_answers)):
            if users_answers[j][i] == correct_ans:
                results[j] += 1

    print(*results, sep="\n")





if __name__ == "__main__":
    main()
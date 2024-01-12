ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3

WIN_SCORE = 6
DRAW_SCORE = 3


def get_input():
    with open("./input.txt") as f:
        return f.read().splitlines()


def get_score1(play: str) -> int:
    # a=x=rock=1, b=y=paper=2, c=z=scissors=3
    player1, player2 = play.split(" ")
    if player1 == "A":
        if player2 == "X":
            return DRAW_SCORE + ROCK_SCORE
        if player2 == "Y":
            return WIN_SCORE + PAPER_SCORE
        return SCISSORS_SCORE
    elif player1 == "B":
        if player2 == "Y":
            return DRAW_SCORE + PAPER_SCORE
        if player2 == "Z":
            return WIN_SCORE + SCISSORS_SCORE
        return ROCK_SCORE
    elif player1 == "C":
        if player2 == "Z":
            return DRAW_SCORE + SCISSORS_SCORE
        if player2 == "X":
            return WIN_SCORE + ROCK_SCORE
        return PAPER_SCORE


def get_score2(play: str) -> int:
    # x=lose, y=draw, z=win
    player1, player2 = play.split(" ")
    if player2 == "X":
        if player1 == "A":
            return SCISSORS_SCORE
        if player1 == "B":
            return ROCK_SCORE
        return PAPER_SCORE
    elif player2 == "Y":
        if player1 == "A":
            return DRAW_SCORE + ROCK_SCORE
        if player1 == "B":
            return DRAW_SCORE + PAPER_SCORE
        return DRAW_SCORE + SCISSORS_SCORE
    elif player2 == "Z":
        if player1 == "A":
            return WIN_SCORE + PAPER_SCORE
        if player1 == "B":
            return WIN_SCORE + SCISSORS_SCORE
        return WIN_SCORE + ROCK_SCORE


def solve1() -> int:
    """
    First part of the challenge
    """
    plays = get_input()
    total = 0
    for play in plays:
        total += get_score1(play)
    print(total)


def solve2() -> int:
    """
    Second part of the challenge
    """
    plays = get_input()
    total = 0
    for play in plays:
        total += get_score2(play)
    print(total)


if __name__ == "__main__":
    solve1()
    solve2()

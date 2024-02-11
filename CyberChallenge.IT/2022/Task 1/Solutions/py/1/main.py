from string import punctuation


def is_psw_valid(psw: str, old_psw: str) -> bool:
    # check len psw, min 8 max 16
    if not 8 <= len(psw) <= 16:
        return False

    # check contains upper and lower case
    # check for at least one digit and one special character
    is_there_upper = False
    is_there_lower = False
    is_there_digit = False
    is_there_special_char = False

    for char in psw:
        if char.isupper():
            is_there_upper = True
        if char.islower():
            is_there_lower = True
        if char.isdigit():
            is_there_digit = True
        if char in punctuation:
            is_there_special_char = True
        if (
            is_there_upper
            and is_there_lower
            and is_there_digit
            and is_there_special_char
        ):
            break
    else:
        return False

    # check consecutive identical characters
    for i in range(1, len(psw)):
        if psw[i] == psw[i - 1]:
            return False

    # check not be derivable by deleting, substituting or adding exactly one character from the old password
    old_psw_set = set(old_psw)
    psw_set = set(psw)

    if len(psw_set.difference(old_psw_set)) < 2:
        return False

    return True


def main():
    n = int(input())

    while n:
        new_psw, old_psw = input().split()

        status = int(is_psw_valid(new_psw, old_psw))
        print(status)

        n -= 1


if __name__ == "__main__":
    main()

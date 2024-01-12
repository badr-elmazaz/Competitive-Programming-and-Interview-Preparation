

def get_input():
    with open("./input.txt") as f:
        return f.read().splitlines()


        
def get_common_char(s1: str, s2: str)->str:
    # sort them so it the search will be more efficient
    s1_sorted=''.join(sorted(s1))
    s2_sorted=''.join(sorted(s2))
    for c1 in s1_sorted:
        for c2 in s2_sorted:
            if( c1==c2 ):
                return c1
            if( c1<c2 ):
                break

def get_char_value(c: str)->int:
    if(c.isupper()):
        return ord(c)-ord("A")+27
    return ord(c)-ord("a")+1



def solve1():
    inputs = get_input()

    sum = 0

    for i in inputs:
        first_half, second_half = i[:len(i)//2], i[len(i)//2:]
        common_char = get_common_char(first_half, second_half)
        sum += get_char_value(common_char)
    print(sum)


def remove_duplicates(string: str)->str:
    # string is sorted
    string_without_duplicates = ""
    for i in range(len(string)):
        if( i == len(string)-1 ):
            string_without_duplicates+=string[i]
        elif( string[i] !=string[i+1] ):
            string_without_duplicates+=string[i]
    return string_without_duplicates
        

def get_common_char_generic(args: list[str]):
    # get common char using a dictionary
    dictionary = {}
    for i in range(len(args)):
        string_sorted = ''.join(sorted(args[i]))
        args[i] = remove_duplicates(string_sorted)
    for string in args:
        for c in string:
            if c in dictionary:
                dictionary[c]+=1
                if dictionary[c]==3:
                    return c
            else:
                dictionary[c]=1


def solve2():
    inputs = get_input()

    sum = 0

    for i in range(0, len(inputs), 3):
        common_char = get_common_char_generic([inputs[i], inputs[i+1], inputs[i+2]])
        sum+=get_char_value(common_char)
    print(sum)



if __name__ == "__main__":
    solve1()
    solve2()

import os
import hashlib

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(path: str) -> list[int]:
    with open(path) as f:
        return f.readlines()
    
def get_md5(string: str) -> str:
    md5_hash = hashlib.md5(string)
        # Return the hexadecimal digest of the hash
    return md5_hash.hexdigest()


def solve_part_one():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    solution = 0
    
    prefix = inputs[0].replace("\n", "")
    
    PASSWORD_LEN = 8
    
    password = ""
    
    i = 0
    
    
    while len(password)<PASSWORD_LEN:
        
        number_str = prefix+str(i)            
        # Encode the string to bytes
        encoded_number = number_str.encode()
        md5 = get_md5(encoded_number)
        if md5.startswith("0"*5):
            password+=md5[5]
        i+=1
    
    solution = password
           
    
    print("Solution Part 1:", solution)

def solve_part_two():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    solution = 0
    
    prefix = inputs[0].replace("\n", "")
    
    password_char_found = 0
    PASSWORD_LEN = 8
    
    password = ["" for i in range(0, 8)]
    
    i = 0
    
    
    while password_char_found<PASSWORD_LEN:
        number_str = prefix+str(i)            
        # Encode the string to bytes
        encoded_number = number_str.encode()
        md5 = get_md5(encoded_number)
        if md5.startswith("0"*5):
                if md5[5].isdigit():
                    position = int(md5[5])
                    if position<8 and password[position] == "":
                        password[position] = md5[6]
                        password_char_found+=1
            
        i+=1
    
    solution = "".join(password)
    
    print("Solution Part 2:", solution)


def main():
    solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()
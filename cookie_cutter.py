from colorama import just_fix_windows_console
import sys
import os

RED = "\033[1;31m"
GREEN = "\033[1;32m"
DEFAULT = "\033[0m"

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def get_platform():
    print("Select a platform:")
    print()
    platforms = {
        "Advent of Code": "Advent-of-Code",
        "Algoexpert": "Algoexpert",
        "Codeforces": "Codeforces",
        "Codechef": "Codechef",
        "HackerRank": "HackerRank",
        "Leetcode": "Leetcode",
        "Project Euler": "Project Euler",
        "Pramp": "Pramp",
    }
    
    sorted_platforms = sorted(platforms.keys())
    
    
    for i, dir in enumerate(sorted_platforms):
        print(f"\t{i+1}. {dir}")
        
    print()
    
    print("Select a platform: ", end="")
    platform = int(input(GREEN))
    print(DEFAULT)
    
    if platform < 1 or platform > len(platforms):
        print(RED + "Error. You choose an invalid platform number." + DEFAULT)
        sys.exit(1)
        
    return platforms[sorted_platforms[platform - 1]]


def get_problem_name():
    print("Enter the problem name: ", end="")
    problem_name = input(GREEN)
    print(DEFAULT)
    if not problem_name:
        print(RED + "Error. You must enter a problem name." + DEFAULT)
        sys.exit(1)
    
    return problem_name

def create_files(directory: str, problem_name: str, programming_language: str):
    current_dir = os.path.join(CURRENT_DIR, directory)
    if not os.path.exists(current_dir):
        print("Directory does not exist.")
        sys.exit(1)
    # create directory
    problem_dir = os.path.join(current_dir, problem_name)
    if not os.path.exists(problem_dir):
        os.mkdir(problem_dir)
    
    # create md file
    md_file = os.path.join(problem_dir, "README.md")
    if not os.path.exists(md_file):
        with open(md_file, "w") as f:
            f.write(f"# {problem_name}")
        
    # create solution directory
    solution_dir = os.path.join(problem_dir, "Solutions")
    if not os.path.exists(solution_dir):
        os.mkdir(solution_dir)
    
    # create programming language directory
    programming_language_dir = os.path.join(solution_dir, programming_language)
    if not os.path.exists(programming_language_dir):
        os.mkdir(programming_language_dir)
    
    # create num directory
    # get all directories in programming language directory
    next_solution_num = max([int(dir) for dir in os.listdir(programming_language_dir) if dir.isdigit()] or [0]) + 1
    next_solution_num_dir = os.path.join(programming_language_dir, str(next_solution_num))
    
    os.mkdir(next_solution_num_dir)
    
    # create solution file
    solution_file = os.path.join(next_solution_num_dir, f"main.{programming_language}")
    if os.path.exists(solution_file):
        print(RED)
        print("File already exists.")
        print(DEFAULT)
        sys.exit(1)
    with open(solution_file, "w") as f: 
        f.write("")
    


def get_programming_language():
    print("Select a programming language:")
    programming_languages = {
        "Python": "py",
        "Java": "java",
        "C++": "cpp",
        "C": "c",
        "Javascript": "js",
        "Go": "go",
        "Rust": "rs",
        "Ruby": "rb",
        "lua": "lua",
        "Scala": "scala",
        "Kotlin": "kt",
        "Swift": "swift",
        "Typescript": "ts",
    }
    sorted_programming_languages = sorted(programming_languages.keys())
    
    
    for i, dir in enumerate(sorted_programming_languages):
        print(f"\t{i+1}. {dir}")
        
    print()
    
    print("Select a Programming Language: ", end="")
    programming_language = int(input(GREEN))
    print(DEFAULT)
    
    if programming_language < 1 or programming_language > len(programming_languages):
        print(RED + "Error. You choose an invalid platform number." + DEFAULT)
        sys.exit(1)
        
    return programming_languages[sorted_programming_languages[programming_language - 1]]
    
    
def main():
    try:
        just_fix_windows_console()
        directory = get_platform()
        problem_name = get_problem_name()
        programming_language = get_programming_language()
        create_files(directory, problem_name, programming_language)
        sys.exit(0)
    except Exception as e:
        print(RED + f"Error: {e}" + DEFAULT)
        sys.exit(1)
    
    

if __name__ == "__main__":
    main()
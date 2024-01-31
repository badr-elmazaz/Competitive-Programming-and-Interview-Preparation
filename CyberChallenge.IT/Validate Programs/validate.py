import os
import sys

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def main():
    input_path = os.path.join(THIS_FOLDER, 'input')
    if not os.path.exists(input_path):
        print("'input' folder not found")
        print("Create it and put the correct input files in it")
        os.mkdir(input_path)
        sys.exit(1)
    output_path = os.path.join(THIS_FOLDER, 'output')
    if not os.path.exists(output_path):
        print("'output' folder not found")
        print("Create it and put the correct output files in it")
        os.mkdir(output_path)
        sys.exit(1)
    program_path = os.path.join(THIS_FOLDER, 'program')
    if not os.path.exists(program_path):
        print("'program' folder not found")
        print("Create it and put the correct program in it")
        os.mkdir(program_path)
        sys.exit(1)
    program_file_path = os.path.join(program_path, 'main.py')
    if not os.path.exists(program_file_path):
        print("'main.py' file not found in 'program' folder")
        sys.exit(1)
    
    passed = 0
    failed = 0
    for input_file in os.listdir(input_path):
        if input_file.endswith(".txt"):
            input_file_path = os.path.join(input_path, input_file)
            output_file_path = os.path.join(output_path, input_file.replace("input", "output"))
            
            # run python program and get output with os
            command = f"""python "{program_file_path}" < "{input_file_path}" """
            with os.popen(command) as process:
                output_program = process.read()
                
            # compare output_program with output_file
            with open(output_file_path, 'r') as f:
                output_file = f.read()
                
            if output_program.strip() == output_file.strip():
                print(f"{input_file} PASSED")
                passed += 1
            else:
                print(f"{input_file} FAILED")
                print(f"Program output:\n{output_program}")
                print(f"Correct output:\n{output_file}")
                failed += 1
                
    print()
    print(f"Tests Passed: {passed}/{passed + failed}\nTests Failed: {failed}/{passed + failed}")
    if not failed:
        sys.exit(1)
    
    



if __name__ == "__main__":
    main()
    sys.exit(0)
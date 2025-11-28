#!/usr/bin/python3
import sys
import os

# 2. invoke: get the option from command
def get_command_line_args():
    option = sys.argv[1]

    # 9. incorrect syntax
    if option not in ['-a', '-s', '-l', '-v']:
        print("this option doesn't exist")
        sys.exit(1)
        
    if option == '-l':
        if len(sys.argv) != 4:  
            print("it misses an argument")
            sys.exit(1)
        name = sys.argv[2]
        argument_file = sys.argv[3]
    else:
        if len(sys.argv) < 3:  
            print("it misses the argument file")
            sys.exit(1)
        name = None
        argument_file = sys.argv[2]

    # file: readable and exist
    if not os.path.isfile(argument_file) or not os.access(argument_file, os.R_OK):
            print(f"Error: The file '{argument_file}' does not exist or is not readable.")
            sys.exit(1)

    process_option(option, argument_file, name)

# option
def process_option(option, argument_file, name):
    if option == '-a':
        print_installed_packages(argument_file)
    elif option == '-s':
        print_total_size(argument_file)
    elif option == '-l' and name:
        print_package_info(argument_file, name)
    elif option == '-v':
        print_student()
    else:
        print(f"Unsupported option: {option}")
        sys.exit(1)

# 4. option "-a"        
def print_installed_packages(argument_file):
    with open(argument_file, 'r') as file: #open and read the file
        lines = file.readlines()

    if lines:
        print("Installed packages:")
        for line in lines:
            if line.strip():  # not empty
                print(line.split(',')[1]) # split to many words by ","
    else:
        print("No packages installed")

# 5. option "-s"
def print_total_size(argument_file):
    with open(argument_file, 'r') as file:
        lines = file.readlines()

    total = 0
    for line in lines:
        if line.strip():
            total = total + int(line.split(',')[3])
    
    print(f"Total size in kilobytes: {total}")

# 6. option '-l name'
def print_package_info(argument_file, name):
    with open(argument_file, 'r') as file:
        lines = file.readlines()
    
    found = False 
    for line in lines:
        if line.strip():  
            fields = line.split(',')
            if fields[1].strip() == name: 
                print(f"Package: {fields[1].strip()}")
                print(f"Category: {fields[0].strip()}")
                print(f"Description: {fields[2].strip()}")
                print(f"Size in kilobytes: {fields[3].strip()}")
                found = True
                break 
    if not found:
        print("No installed package with this name")

# 7. option '-v'
def print_student():
    print("Name: J")
    print("Surname: G")
    print("Student ID: 211111")
    print("Date of Completion: 17/10/2024")

get_command_line_args() #get the option and file


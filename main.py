"""
    This program sorts files in the specified directory by file extension.
"""

import os
import shutil
import glob
import sys

# main_directory = "test_dir"
graphics_dir = "graphics"
archives_dir = "archives"
documents_dir = "documents"

# File extension lists by category.
graphics = ['.png', '.jpg', '.jpeg', '.bmp']
archives = ['.tar', '.zip', '.7zip', '.rar', '.iso', '.bin']
documents = ['.fb2', '.pdf', '.doc', '.docx', '.xml', '.txt', '.md']

# List of all files in main directory.
files_of_main_dir = []


# Go to the main directory.
def go_to_the_main_directory(main_directory):
    try:
        os.chdir(main_directory)
    except OSError:
        print("Main directory does not exist. Program complete.")
    else:
        print("\nThe work is conducted in the directory: ", main_directory, "\n")
        print("List of all files located in this directory: \n", glob.glob('*.*'))
        # Compile a list of all files in main directory.
        files_of_main_dir.clear()
        files_of_main_dir.extend(glob.glob('*.*'))
        print("\nCount of files in main directory: ", len(files_of_main_dir))

        # Creating directories for sorting.


def create_directories():
    if not os.path.exists(graphics_dir):
        os.makedirs(graphics_dir)
    if not os.path.exists(archives_dir):
        os.makedirs(archives_dir)
    if not os.path.exists(documents_dir):
        os.makedirs(documents_dir)
    print("\nDirectories for sorting files ready.")

    # Sort of files.


def sort_of_files():
    for i in sorted(files_of_main_dir):
        for k in graphics:
            if i.endswith(k):
                shutil.move(i, graphics_dir)
                files_of_main_dir.clear()
                files_of_main_dir.extend(glob.glob('*.*'))
    for i in sorted(files_of_main_dir):
        for k in archives:
            if i.endswith(k):
                shutil.move(i, archives_dir)
                files_of_main_dir.clear()
                files_of_main_dir.extend(glob.glob('*.*'))
    for i in sorted(files_of_main_dir):
        for k in documents:
            if i.endswith(k):
                shutil.move(i, documents_dir)
                files_of_main_dir.clear()
                files_of_main_dir.extend(glob.glob('*.*'))
    # print(files_of_main_dir)
    # files_of_main_dir.clear()
    print("Sorting is complete.\n")


# go_to_the_main_directory()
# create_directories()
# sort_of_files()


# Main menu of program.
while True:
    try:
        x = int(input('''\nSelect the desired action:
                    0 - Clear console.
                    1 - List all files in the selected directory.
                    2 - Start sorting.
                    3 - Stop the program.\n'''))
        break
    except ValueError:
        os.system('cls')
        print("Oops!  That was no valid number.  Try again...")
if x == 0:
    os.system('cls')
elif x == 1:
    main_directory = input('input main directory: ')
    go_to_the_main_directory(main_directory)
elif x == 2:
    main_directory = input('input main directory: ')
    go_to_the_main_directory(main_directory)
    create_directories()
    sort_of_files()
elif x == 3:
    print("\nProgram stopped.\n")
    sys.exit(0)
else:
    os.system('cls')
    print("Invalid input. Repeat input.\n")

import os
import shutil
import glob


"""
    This program sorts files in the specified directory by file extension.
"""


main_directory = "D:\\test_dir"
graphics_dir = main_directory + r"\graphics"
archives_dir = main_directory + r"\archives"
documents_dir = main_directory + r"\documents"

 # File extension lists by category.
graphics = ['.png', '.jpg', '.jpeg', '.bmp']
archives = ['.tar', '.zip', '.7zip', '.rar', '.iso', '.bin']
documents = ['.fb2', '.pdf', '.doc', '.docx', '.xml', '.txt', '.md']

 # List of all files in main directory.
files_of_main_dir = []
 
 # Go to the main directory. 
def go_to_the_main_directory():
    try:
        os.chdir(main_directory)
    except OSError:
        print("Main directory does not exist. Program complete.")
    else:
        print("\nThe work is conducted in the directory: ", main_directory, "\n")
        print("List of all files located in this directory: \n", glob.glob('*.*'))
         # Compile a list of all files in main directory.
        files_of_main_dir.extend(glob.glob('*.*'))

 # Creating directories for sorting.
def create_directories():
    if os.path.exists(graphics_dir):
        pass
    else:
        os.makedirs(graphics_dir)
    if os.path.exists(archives_dir):
        pass
    else:
        os.makedirs(archives_dir)
    if os.path.exists(documents_dir):
        pass
    else:
        os.makedirs(documents_dir)
    print("\nDirectories for sorting files ready.\n")

 # Sort of files.
def sort_of_files():
    for i in files_of_main_dir:
         # Sort of graphics.
        for k in graphics:
            if i.endswith(k):
                shutil.move(i, graphics_dir)
         # Sort of archives.
        for k in archives:
            if i.endswith(k):
                shutil.move(i, archives_dir)
         # Sort of documents.
        for k in documents:
            if i.endswith(k):
                shutil.move(i, documents_dir)
                                                                                                                                                  
go_to_the_main_directory()
create_directories()
sort_of_files()

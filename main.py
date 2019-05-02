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
        # print("Main directory does not exist. Program complete.")
        # На этом месте программа падает, если предпологается выход, можно добавить exit()
        # А вообще зачем оно выходит?
        # Оно может предложить попробовать другой каталог
        print("Main directory does not exist. Try again.")
        return False
        # Добавляем возврат значения, для контроля наличия каталога

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
        os.mkdir(graphics_dir)
        # Мы создаем только один каталог каждый раз, поэтому метод изменём с makedirs на mkdir
    if not os.path.exists(archives_dir):
        os.mkdir(archives_dir)
    if not os.path.exists(documents_dir):
        os.mkdir(documents_dir)
    print("\nDirectories for sorting files ready.")


# Sort of files.
def sort_of_files():
    for i in files_of_main_dir:
        # https://ru.stackoverflow.com/questions/540082/%d0%9e%d0%bf%d1%80%d0%b5%d0%b4%d0%b5%d0%bb%d0%b5%d0%bd%d0%b8%d0%b5-%d1%80%d0%b0%d1%81%d1%88%d0%b8%d1%80%d0%b5%d0%bd%d0%b8%d1%8f-%d1%84%d0%b0%d0%b9%d0%bb%d0%b0-%d0%b2-python
        filename, file_extension = os.path.splitext(i)
        # На питоне не обязательно писать явный for, более "питоник" просто спросить есть ли это в том:  
        if file_extension in graphics:
            shutil.move(i, graphics_dir)
        elif file_extension in archives:
            shutil.move(i, archives_dir)
        elif file_extension in documents:
            shutil.move(i, documents_dir)

        # Смотри тему сложности алгоритмов, почему плохо много форов и сортировок

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
        # Вот тут нужно удалить break, чтобы избавиться от лишней функции и её рекурсивных вызовов
    except ValueError:
        os.system('cls' if os.name=='nt' else 'clear')
        print("Oops!  That was no valid number.  Try again...")
        continue

    if x == 0:
        os.system('cls' if os.name=='nt' else 'clear')
    elif x == 1:
        main_directory = input('input main directory: ')
        go_to_the_main_directory(main_directory)
        continue
        # continue нужны для того чтобы нижеследующее пропускалось и программа переходила к следующей итерации while
    elif x == 2:
        main_directory = input('input main directory: ')
        if go_to_the_main_directory(main_directory): # Проверяем существование каталога по возврящённому значению
            create_directories()
            sort_of_files()
        continue
    elif x == 3:
        print("\nProgram stopped.\n")
        # sys.exit(0) Есть ли тут смысл использовать sys? Мне кажется подходит обычный exit, но я не знаю в чём между ними разница
        exit(0)
    else: # До этой точки программа не доходила, т.к. падала на if x == 0: NameError: name 'x' is not defined, решается добавлением continue в except ValueError:
        # Строка изменена для мультиплатформенности
        os.system('cls' if os.name=='nt' else 'clear')
        print("Invalid input. Repeat input.\n")
=======
def main():
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
    main()

main()

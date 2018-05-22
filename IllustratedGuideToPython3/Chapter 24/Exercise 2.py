# Exercise: Find a package in the Python standard library for listing directory contents. Using
# that package, write a function that accepts a directory name. The function should get
# all the files in that directory and print out a report of the count of files by extension
# type.

import os

eotb_path = 'E:\\Eye of the Beholder'

def directory_info(path):
    print("Collecting information about:", path)
    file_count = 0

    for (directory, sub_directories, files) in os.walk(path):
        file_count += len(files)
        
        for file in files:
            print(os.path.join(directory, file))

    print("Total Files:", file_count)
    return None



directory_info(eotb_path)

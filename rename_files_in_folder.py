
# Python program to rename all file
# names in your directory
import os

def change_names(files_location, rename_to):
    os.chdir(files_location)
    print(os.getcwd())

    for count, f in enumerate(os.listdir()):
        f_name, f_ext = os.path.splitext(f)
        f_name = rename_to + str(count)
    
        new_name = f'{f_name}{f_ext}'
        os.rename(f, new_name)
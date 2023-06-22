import os
import shutil

def locate_parsed_files(filename: str):
    if filename.__contains__('PARSED'):
        print(f'Error file : {filename} already parsed')
        return False
    else:
        return True


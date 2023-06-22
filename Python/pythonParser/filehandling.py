import os
import pandas as pd
import sqlite3 as db
import shutil

def file_approach(file_name_attr: str):
    file = open(file_name_attr)
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    print(file_dir)

def find_files(abs_path: str, file_names_attr: list):
    for path, dirs, files in os.walk(abs_path):
        for f in files:
            file_names_attr.append(os.path.join(path, f))
            print(f)
    print(f"Found {len(file_names_attr)} files in folder")


def skip(skipper: list, df_test: pd.DataFrame):
    for i in range(find_last_row(df_test) + 1, len(df_test)):
        skipper.append(i)
    df_test = df_test.drop(labels=skipper, inplace=True)
    print("Dropped None val rows")

def find_last_row(df_test: pd.DataFrame):
    col = [df_test.loc[df_test[1] == 'завершен'][1].index]
    print('Found last row of DataFrame')
    return col[-1][-1]



from filehandling import *
from filemanipulation import *
from datetime import datetime
import sqlite3 as db

if __name__ == "__main__":
    file_names = []
    startTime = datetime.now()
    absolute_path = '/Users/dantes/Desktop/Reestrs'
    find_files(absolute_path, file_names)
    index_list: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    skippers: list = [0, 1, 2, 3]
    db_table = 'reestrs'

    for filename in file_names:
        if filename.endswith(".xlsx") and locate_parsed_files(filename):
            df = pd.read_excel(f"{filename}", names=index_list)
            period = df[1][1]
            total: str = f'{df[9][len(df) - 3]}.{df[10][len(df) - 3]}'
            skip(skippers, df)
            with db.connect('pythonDB') as con:
                result = con.execute(f"""Insert into reestr_index(filename, total_sum, period)
                    values ('{filename[30:len(filename)]}', '{total}', '{period}')""")
                try:
                    df.to_sql(name=db_table, con=con, if_exists='append')
                except Exception as e:
                    print(e)

            checked_filename = filename[0:filename.find('trs/') + 4] + 'PARSED_' + filename[
                                                                                   filename.find('trs/') + 4: len(
                                                                                       filename)]
            os.renames(filename, checked_filename)

            print(f'{filename} has been parsed and renamed to {checked_filename}')
        else:
            print("File is already parsed or not excel format extentsion")

    # TODO: user context manager
    print(f"FINISHED: {datetime.now() - startTime} secs")


# later
# SQL Lite to Oracle
# logging to file
# Index tables

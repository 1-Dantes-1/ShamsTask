import datetime
from datetime import date
import pandas as pd
import sqlite3 as db
def find_last_row():
    col = [df.loc[df[1] == 'завершен'][1].index]
    return col[-1][-1]

filename = 'solidar_reestr'
names: int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
df = pd.read_excel(f'{filename}.xlsx', names=names)
rows_to_delete = [0, 1, 2, 3]
for i in range(find_last_row() + 1, len(df)):
    rows_to_delete.append(i)

df2 = df.drop(labels=rows_to_delete)

con = db.connect('pythonDB')
cur = con.cursor()


try:
    df2.to_sql(name='reestrs', con=con, if_exists='append')
except Exception as e:
    print(e)

def find_period():
    substring = "ЗА ПЕРИОД С"
    mask = df[df.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    answer: str = f'{mask.values[0][0]}'
    return answer

def find_total_sum():
    substring = "ИТОГО"
    mask = df[df.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]
    answer: str = f'{mask.values[0][8]}.{mask.values[0][9]}'
    return answer

cur.execute(
    f"Insert into reestr_index(filename, total_sum, period) values('{filename}','{find_total_sum()}','{find_period()}');"
)

con.close()







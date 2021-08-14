import re
import sqlite3
s = 'klmnk926725842'
s = re.sub('klmnk','', s)
print(s)
conn = sqlite3.connect('db_2.db')
c = conn.cursor()
select = "SELECT name FROM sqlite_master WHERE type='table';"
l = c.execute(select).fetchall()
# for i in l:
    # if i[0][0] == 'k':
        # print(i)

from time import sleep
from threading import Thread
from schedule import *
import schedule
import time
import datetime
import sqlite3

now = datetime.datetime.now()
conn = sqlite3.connect('C:/Users/Admin/PycharmProjects/TAS/bot/bot_tas.db')
c = conn.cursor()

select = "SELECT * FROM mail"

l = c.execute(select).fetchall()
for i in l:
    print(i[0])



def scheduler(hello):
    now = datetime.datetime.now()
    print(now)


schedule.every(1).minute.do(scheduler, now)

while True:
    schedule.run_pending()
    time.sleep(1)

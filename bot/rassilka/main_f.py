import sched
from datetime import datetime
import os
import sqlite3
import schedule
import time
from time import sleep
import timedelta


now = datetime.now()


def get_all_time():
    conn = sqlite3.connect('C:/Users/Admin/PycharmProjects/TAS/bot/bot_tas.db')
    c = conn.cursor()
    select = "SELECT * FROM mail"
    l = c.execute(select).fetchall()
    time_for_mailing = []
    for i in l:
        time_for_mailing.append(i)
    return time_for_mailing


def check_files(name):

    path = "C:/Users/Admin/PycharmProjects/TAS/files/"
    path = path + name + '/scanWorks/'
    path = path 
    c = os.path.getctime(path)

    for dirpath, dirnames, filenames in os.walk(path):

        break
    print(dirnames)
    files = []
    for i in dirnames:
        s = path + i
        c = int(os.path.getctime(s))
    

        time = datetime.fromtimestamp(c).strftime('%Y-%m-%d %H:%M:%S')
        print(i)
        # year = datetime.fromtimestamp(c).strftime('%Y')
        # month = datetime.fromtimestamp(c).strftime('%m')
        # day = datetime.fromtimestamp(c).strftime('%d')
        # hour = datetime.fromtimestamp(c).strftime('%H')
        # minute = datetime.fromtimestamp(c).strftime('%M')
        # second = datetime.fromtimestamp(c).strftime('%S')
        # print(c)
        files.append((i, c))
    
        
        
    # print(files)
    files.sort(key=lambda tup: tup[1])

    print(files)
    #так ну массив отсортили, оформить как функцию, распараллелить процесс на каждого учителя


def scheduler(hello):
    conn = sqlite3.connect('C:/Users/Admin/PycharmProjects/TAS/bot/bot_tas.db')
    c = conn.cursor()


    now = datetime.now()
    time_for_mailing = get_all_time()
    # print(time_for_mailing[0][0].split(':'))
    hour = now.hour
    minute = now.minute
    # print(hour, minute)
    for i in time_for_mailing:
        s = i
        table = i[0].split(':')
        # print(table, 'g[g[')

        #damn заменить на hour and minute
        if table[0] == '12' and table[1] == '55':
            print(table)
            name_of_teacher = s[1]
            print(name_of_teacher)
            select = f"SELECT * FROM {name_of_teacher}"
            l = c.execute(select).fetchall()


            for j in range(0, len(l)):
                count = l[j][-1].find('None x')
                print(count)

                if count != -1:
                    stroka = l[j][-1][0:count]

                    print(stroka, l[j][1])

                else:
                    print(l[j][-1], l[j][1])


        #должны смотреть таблицу с именем учителя


    #тут смотрим таблицу с учителем, после чего чекаем дни учеников и рассылаем

scheduler('hello')

# schedule.every(4).seconds.do(scheduler, now)
# while True:
#     schedule.run_pending()
#     sleep(1)
# check_files('Zharskiy_Egor_Aleksandrovich')
# get_all_time()
import telebot
from telebot import types
import sqlite3
import datetime
import time
import random
import colorama
from getmac import get_mac_address as gma
from colorama import Fore, Back, Style
colorama.init()
mac_a = gma()



#получение инфы о системе


conn = sqlite3.connect("db_second.db")
c = conn.cursor()
sql = "SELECT system from cpu_inf WHERE num=1"
l = c.execute(sql).fetchall()
q = "SELECT * FROM cpu_inf"
all = c.execute(q).fetchall()
#print(mac_a == l[0][0])

if l[0][0] != mac_a:
    #вставка в бд новой инфы о cpu, если не совпадает
    for i in all:
        if i[0] == 1:
            q = "UPDATE cpu_inf set system = ? WHERE num = ?"

    sql = "INSERT INTO cpu_inf(system)  WHERE num=1 values(?)"
    data = (mac_a, 1)
    c.execute(q, data)
    conn.commit() # каждый раз создает новую строку
    #вставка токена + вставка тичесркого айди
    print(Fore.RED + 'Введите token бота, который будет использоваться для работы с учащимися.')
    #print()

    token = input(Style.RESET_ALL)
    q = "UPDATE   cpu_inf set token = ? WHERE num = ?"

    data = (token, 1)
    c.execute(q, data)
    conn.commit()
    #teacher id
    print(Fore.RED + "Введите ваш id в Telegram, чтобы пересылать вам вопросы от учеников"
                     "(о том, как узнать свой id вы можете почитать в интернете.")
    #print()

    t_id = input(Style.RESET_ALL)
    q = "UPDATE   cpu_inf set teacher_id = ? WHERE num = ?"
    data = (t_id, 1)
    c.execute(q, data)
    conn.commit()
    print(Style.RESET_ALL)
    print(Back.BLUE + 'Token бота: ' + token)
    print('Ваш id: ' + t_id)
    print(Style.RESET_ALL + 'Введите "да", если вся информация введена корректно, в противном случае выведите "нет"'
                '. Будьте внимательны, так как информацию невозможно будет изменить.')
    que = input()
    if que == "нет":
        print(Fore.RED + 'Введите token бота, который будет использоваться для работы с учащимися.')
        # print()

        token = input(Style.RESET_ALL)
        q = "UPDATE   cpu_inf set token = ? WHERE num = ?"

        data = (token, 1)
        c.execute(q, data)
        conn.commit()
        # teacher id
        print(Fore.RED + "Введите ваш id в Telegram, чтобы пересылать вам вопросы от учеников"
                         "(о том, как узнать свой id вы можете почитать в интернете.")
        # print()

        t_id = input(Style.RESET_ALL)
        q = "UPDATE   cpu_inf set teacher_id = ? WHERE num = ?"
        data = (t_id, 1)
        c.execute(q, data)
        conn.commit()
        print(Style.RESET_ALL)
        print(Back.BLUE + 'Token бота: ' + token + 'token')
        print('Ваш id: ' + t_id + 'id')
        print(Style.RESET_ALL + 'Введите "да", если вся информация введена корректно, в противном случае выведите "нет"'
                                '. Будьте внимательны, так как информацию невозможно будет изменить.')
        #que = input()


now = datetime.datetime.now()
_connection = None
s = open('zadachi.txt', 'r')
w = []
for line in s:
    w.append(line)
#заменить токен на тот, что будут вставлять сами пользователи
choose = "SELECT token FROM cpu_inf WHERE num=?"
data = (1,)
ch = c.execute(choose, data).fetchone()[0]
#print(ch)
bot = telebot.TeleBot(ch)
@bot.message_handler(commands=['answer'])
def check(message):
    id = int(message.from_user.id)

    conn = sqlite3.connect('db_second.db')
    c = conn.cursor()
    sql = "SELECT teacher_id FROM cpu_inf WHERE num=?"
    data = (1,)
    teacher_id = c.execute(sql, data).fetchone()[0]

    teacher_id = int(teacher_id)
    if id != teacher_id:
        bot.send_message(message.from_user.id, 'Я не знаю что ответить 😢')
    else:
        bot.send_message(message.from_user.id, 'ответьте на сообщение')
        bot.register_next_step_handler(message, reply)
def reply(message):
    conn = sqlite3.connect('db_second.db')
    c = conn.cursor()
    sql = "SELECT teacher_id from cpu_inf WHERE num=?"
    data = (1, )
    teach_id = c.execute(sql, data).fetchone()[0]


    #mess = {}
    mess = message.reply_to_message.text
    mess = mess.split('\n')
    repl = mess[-1]

    #первое - куда пересылаешь, второе - откуда пересланно, третье - айди самого сообщения
    print(repl[repl.find(':') + 1:], teach_id, message.message_id)
    bot.forward_message(repl[repl.find(':') + 1:], teach_id, message.message_id)





    #print(message)



@bot.message_handler(commands=['help'])
def appeal(message): #appeal - обращение

    global identifier


    identifier = int(message.from_user.id)
    x = "отправь два сообщения : в первом укажи проблему, номер задачи, во втором отправь свой код," \
        " если потребуется, а иначе введи вместо исходного кода NO "
    bot.send_message(message.from_user.id, x)
    bot.register_next_step_handler(message, problem)
def problem(message):
    global teacher_id
    global text
    conn = sqlite3.connect('db_second.db')
    c = conn.cursor()
    sql = "SELECT teacher_id FROM cpu_inf WHERE num=?"
    data = (1,)
    teacher_id = c.execute(sql, data).fetchone()[0]
    #print(teacher_id)

    text = message.text
    #print(text)
    bot.register_next_step_handler(message, second_problem)


def second_problem(message):
    global name
    global teacher_id
    global text2
    global  first_name
    global last_name
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name


    print(name)
    text2 = message.text
    #print(text2 + '=text2')


    send_message_to_teacher()
def send_message_to_teacher():
    global identifier
    global name
    global teacher_id
    global text2
    global first_name
    global last_name

    full_name = name
    if text2.lower() == 'no':
        text2 = "Исходного кода не прилагается."
    finished_mess = 'Сообщение от: ' + first_name + ' ' + last_name + '\n' + text + '\n' + text2 + '\n' + 'user id:'+ str(identifier)
    print(identifier)
    bot.send_message(teacher_id, finished_mess)
    print(teacher_id)
    #тут уже идет пересылка сообщения учителю  + проверка наличия исходного кода...


@bot.message_handler(commands=['start'])
def getId(message):
    id = int(message.from_user.id)
    conn = sqlite3.connect("db_second.db")
    c = conn.cursor()

    sql = "SELECT * from id_login"
    l = c.execute(sql).fetchall()

    ok = True
    for i in l:
        if int(i[0] == id):
            ok = False

    if ok:
        print("Adding new user", id)
        sql = "INSERT INTO id_login(id) values(?)"
        c.execute(sql, (id,))
        conn.commit()
    else:
        print("User", id, "already exist")

    conn.close()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("задача 1")
    item2 = types.KeyboardButton("задача 2")
    item3 = types.KeyboardButton("задача 3")
    item4 = types.KeyboardButton("задача 4")
    item5 = types.KeyboardButton("задача 5")
    markup.add(item1, item2, item3, item4, item5)
    #sti = open('C:/Users/User/PycharmProjects/static/sticker.webp', 'rb')

    #bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id,

                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, тот самый бот, что будет тебе сбрасывать материал по задачам с сайта и будет высылать тебе каждый день новые для самостоятельного их решения:)"
                     "нажав на кнопки, ты получишь некоторую информацию по каждой из задач.".format(

                         message.from_user, bot.get_me()),

                     parse_mode='html', reply_markup=markup)


logins = []
login = ""
name = ''
surname = ''
age = 0


@bot.message_handler(commands=['login'])
def start(message):
    bot.send_message(message.chat.id,
                     "вышли мне свои ФИО acmp, чтобы учитель мог следить за твоими успехами в решении задач.(учитывая "
                     "верхние и нижние регистры)")
    bot.register_next_step_handler(message, get_log)


def get_log(message):
    conn = sqlite3.connect("db_second.db")
    c = conn.cursor()
    ids = int(message.from_user.id)
    print(ids)
    global logins
    global login

    login = message.text
    print(login)
    question = 'запомню.'

    bot.send_message(message.chat.id, text=question)
    sqlite_select_query = """SELECT * from users"""
    c.execute(sqlite_select_query)
    records = c.fetchall()
    # print("Total rows are:  ", len(records))
    # print("Printing each row")
    name = '+_)(*?:%;№"!!"№;%:?*()_+ёёЪ]][][][{}":'

    second = login
    id = ids

    for row in records:

        # print(row[0], '    ', row[1])
        if row[0] == id:
            if row[1] != name:
                sql = "UPDATE users set  Name =  ?  where id = ? "
                data = (second, id)
                c.execute(sql, data)
                conn.commit()
                print('успешно.')

        elif row[0] != id:
            select = "SELECT * FROM users"
            l = c.execute(select).fetchall()
            flag = True
            for i in l:
                if i[0] == id:
                    flag = False

            if flag:
                sql = "INSERT INTO users values(?, ?)"
                data = (id, second)
                c.execute(sql, data)
                conn.commit()
            else:
                pass
    conn.close()


@bot.message_handler(commands=['days'])
def start(message):
    bot.send_message(message.from_user.id,
                     "введи названия дней недели, в которые тебе удобнее всего получать рассылку(например: "
                     "понедельник среда пятница)")
    bot.register_next_step_handler(message, get_name)  # следующий шаг – функция get_name


# else:
#   ...#bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message):  # получаем фамилию
    global name, id
    day = message.text.split()
    # print(day)
    for i in range(len(day)):
        day[i] = day[i].lower()
        # print(day[i])
    # day = ["Понедельник", "Среда", "Пятница"]
    days = {"понедельник": u'0', "вторник": u"1", "среда": u"2", "четверг": u"3", "пятница": u"4", "суббота": u"5",
            "воскресенье": u"6"}
    c = list(set(day) & set(days))
    id = int(message.from_user.id)
    res = []
    for i in c:
        res.append(int(days[i]))
    res.sort(reverse=False)
    print(res)

    conn = sqlite3.connect('db_second.db')
    c = conn.cursor()

    select = "SELECT * FROM days"
    l = c.execute(select).fetchall()
    kol = 0
    for i in l:
        if i[0] == id:
            kol += 1
    for i in range(kol):
        sql = "DELETE FROM days WHERE id = ?"
        data = (id,)
        c.execute(sql, data)
        conn.commit()
        print('готово.')

    for i in range(len(res)):
        id = int(message.from_user.id)
        sql = "INSERT INTO days(id, days) values(?, ?)"
        data = (id, res[i])
        c.execute(sql, data)
        conn.commit()
        print('успешно.')
    text = 'запомню.'
    bot.send_message(message.from_user.id, text=text)

    # rassilka
    select = "SELECT * FROM today_send_out"
    id = []
    l = c.execute(select).fetchall()
    for i in l:
        id.append(i[0])
    for i in l:
        print(i)
        for j in id:
            if j == i[0]:
                sql = "DELETE FROM today_send_out WHERE id=?"
                data = (j,)
                c.execute(sql, data)
    conn.commit()
    select = "SELECT * FROM days"
    l = c.execute(select).fetchall()
    days = []
    for i in l:
        if i[1] == str(now.weekday()):
            days.append(i[0])
    print(days)
    select = "SELECT * FROM today_send_out"
    sql = "INSERT INTO today_send_out(id) values(?)"

    for i in range(len(days)):
        id = days[i]
        data = (id,)
        c.execute(sql, data)
    conn.commit()
    text = 'вроде добавил.'
    bot.send_message(message.from_user.id, text=text)

    # print(name)
    # bot.send_message(message.from_user.id, 'число второго дня')


'''def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'число третьего дня')
    bot.register_next_step_handler(message, get_login)'''

'''def get_login(message):
    idk = int(message.from_user.id)
    conn = sqlite3.connect("db_second.db")
    global age

    age = str(message.text)  # проверяем, что возраст введен корректно
    question = 'понял принял'
    bot.send_message(message.from_user.id, text=question)
    day = [str(name), str(surname), str(age)]
    days = {"понедельник": u'0', "вторник": u"1", "среда": u"2", "четверг": u"3", "пятница": u"4", "суббота": u"5",
            "воскресенье": u"6"}
    c = list(set(day) & set(days))
    all_days = []
    for i in c:
        print(i)  # all_days.append(i)
    c = conn.cursor()

    sql = "INSERT INTO days(id, days) values(?, ?)"
    vau = 1
    c.execute(sql, (idk, vau))
    conn.commit()'''


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':

        if message.text.lower() == 'привет':
            bot.send_message(message.chat.id, 'Привет! Надеюсь , что ты достаточно смотивирован для работы!')
        elif message.text.lower() == "пока":
            bot.send_message(message.chat.id, "Я тебя не отпускал, прощается он..")
        elif message.text.lower() == 'задача 1':
            bot.send_message(message.chat.id, "Та полезная литература, что поможет разобраться.")
            time.sleep(0.5)
            bot.send_message(message.chat.id, "Для языка Pascal:http://labs-org.ru/pascal-5/; ")
            time.sleep(0.5)
            bot.send_message(message.chat.id, "Для C++:"
                                              "https://code-live.ru/post/cpp-arrays/; ")
            time.sleep(0.5)
            bot.send_message(message.chat.id, " Для Python:"
                                              "https://otus.ru/nest/post/522/")
        elif message.text.lower() == 'задача 2':
            bot.send_message(message.chat.id, "Та полезная литература, что поможет разобраться.")
            time.sleep(0.5)
            bot.send_message(message.chat.id, "Для языка Pascal:http://labs-org.ru/pascal-5/; ")
            time.sleep(0.5)
            bot.send_message(message.chat.id, "Для C++:"
                                              "https://code-live.ru/post/cpp-arrays/; ")
            time.sleep(0.5)
            bot.send_message(message.chat.id, " Для Python:"
                                              "https://otus.ru/nest/post/522/")
        elif message.text.lower() == 'задача 3':
            bot.send_message(message.chat.id, "Та полезная литература, что поможет разобраться.")
            time.sleep(0.5)
            bot.send_message(message.chat.id, "Для языка Pascal:http://labs-org.ru/pascal-5/; ")
            time.sleep(0.5)
            bot.send_message(message.chat.id, "Для C++:"
                                              "https://code-live.ru/post/cpp-arrays/; ")
            time.sleep(0.5)
            bot.send_message(message.chat.id, " Для Python:"
                                              "https://otus.ru/nest/post/522/")
            time.sleep(0.5)
            markup = types.InlineKeyboardMarkup(row_width=2)
        elif message.text.lower() == 'задача 5':
            bot.send_message(message.chat.id, "Для Pascal:"
                                              "http://labs-org.ru/pascal-10/")
            time.sleep(0.5)
            bot.send_message(message.chat.id, "Для С++:"
                                              "https://code-live.ru/post/cpp-array-tutorial-part-2/")
            time.sleep(0.5)
            bot.send_message(message.chat.id, "Для  Python: "
                                              "https://labs-org.ru/python-8/")
        elif message.text.lower() == 'задача 4':
            bot.send_message(message.chat.id,
                             "Для решения этой задачи, помимо знания работы массивов, вам также нужно знать сортировки.")
            bot.send_message(message.chat.id, "Сортировка для Pascal:"
                                              "https://pas1.ru/bubbles")
            time.sleep(0.5)
            bot.send_message(message.chat.id, "Сортировка для C++:"
                                              "https://codelessons.ru/cplusplus/algoritmy/puzyrkovaya-sortirovka-v-c-glavnye-momenty.html")
            time.sleep(0.5)
            bot.send_message(message.chat.id, "Сортировка на Python:"
                                              "https://tproger.ru/translations/python-sorting/")

            # item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            # item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            # markup.add(item1, item2)

            # bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


def send_message_to_user(message):
    conn = sqlite3.connect("db_second.db")
    c = conn.cursor()

    sql = "SELECT * from users"
    l = c.execute(sql).fetchall()

    for i in l:
        try:

            bot.send_message(i[0], message)
        except:
            pass
    conn.close()


mas = []

k = 0

# while k <= 1:


# RUN

   # bot.register_next_step_handler(message, answer() )
#def answer(message):
  #  return 1


bot.polling(none_stop=True)
